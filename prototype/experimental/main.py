"""PetPass AI — versão experimental."""

import sys

from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QImageReader, QRegularExpressionValidator
from openai import OpenAIError
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from openai_service import OpenAIConfigurationError, OpenAIService


class IntelligentSummaryWindow(QWidget):
    def __init__(self, summary: str) -> None:
        super().__init__()
        self.setWindowTitle("Resumo Inteligente")

        layout = QVBoxLayout(self)
        summary_text = QTextEdit()
        summary_text.setReadOnly(True)
        summary_text.setPlainText(summary)
        layout.addWidget(summary_text)

        close_button = QPushButton("Fechar")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.resize(520, 400)


class EmergencySheetWindow(QWidget):
    def __init__(self, data: dict[str, str]) -> None:
        super().__init__()
        self.setWindowTitle("Ficha de Emergência")

        layout = QVBoxLayout(self)
        sections = (
            (
                "PET",
                (
                    ("Nome", "Nome do Pet"),
                    ("Espécie", "Espécie"),
                    ("Raça", "Raça"),
                    ("Sexo", "Sexo"),
                    ("Idade", "Idade"),
                    ("Peso", "Peso"),
                ),
            ),
            (
                "TUTOR",
                (
                    ("Nome", "Nome do Tutor"),
                    ("Telefone", "Telefone"),
                    ("Contato de Emergência", "Contato de Emergência"),
                ),
            ),
            (
                "INFORMAÇÕES MÉDICAS",
                (
                    ("Alergias", "Alergias"),
                    ("Medicamentos em uso", "Medicamentos em uso"),
                    ("Doenças conhecidas", "Doenças conhecidas"),
                    ("Vacinas", "Vacinas"),
                    ("Observações", "Observações"),
                ),
            ),
        )

        self.displayed_data: dict[str, dict[str, str]] = {}
        for section_name, section_fields in sections:
            section = QGroupBox(section_name)
            section_layout = QFormLayout(section)
            self.displayed_data[section_name] = {}
            for label, data_key in section_fields:
                value = data[data_key]
                self.displayed_data[section_name][label] = value
                section_layout.addRow(label, QLabel(value))
            layout.addWidget(section)

        generate_summary_button = QPushButton("Gerar Resumo com IA")
        generate_summary_button.clicked.connect(self.generate_ai_summary)
        layout.addWidget(generate_summary_button)

        close_button = QPushButton("Fechar")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.resize(480, 650)

    def generate_ai_summary(self) -> None:
        try:
            summary = OpenAIService().generate_emergency_summary(
                self.displayed_data
            )
        except OpenAIConfigurationError as error:
            QMessageBox.warning(self, "Resumo Inteligente", str(error))
            return
        except OpenAIError:
            QMessageBox.warning(
                self,
                "Resumo Inteligente",
                "Não foi possível gerar o resumo com IA.",
            )
            return

        self.intelligent_summary_window = IntelligentSummaryWindow(summary)
        self.intelligent_summary_window.show()


class PetRegistrationWindow(QWidget):
    """Cadastro rastreado a FNMVP-001/RQMVP-001 e GP-PP-09D."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Cadastro do Pet")
        self.saved_data: dict[str, str] | None = None

        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.fields: dict[str, QWidget] = {}
        for field_name in ("Nome do Pet", "Raça", "Cor"):
            field = QLineEdit()
            self.fields[field_name] = field
            form_layout.addRow(field_name, field)

        species_field = QComboBox()
        species_field.addItems(("", "Cão", "Gato"))
        self.fields["Espécie"] = species_field
        form_layout.insertRow(1, "Espécie", species_field)

        sex_field = QComboBox()
        sex_field.addItems(("", "Macho", "Fêmea", "Não informado"))
        self.fields["Sexo"] = sex_field
        form_layout.insertRow(3, "Sexo", sex_field)

        age_field = QLineEdit()
        age_field.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"[1-9]\d*"))
        )
        self.fields["Idade"] = age_field
        form_layout.insertRow(4, "Idade", age_field)

        weight_field = QLineEdit()
        weight_field.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(
                    r"(?:[1-9]\d*(?:[.,]\d*)?|0[.,]\d*[1-9]\d*|[.,]\d*[1-9]\d*)"
                )
            )
        )
        self.fields["Peso"] = weight_field
        form_layout.insertRow(5, "Peso", weight_field)

        photo_field = QLineEdit()
        photo_field.setReadOnly(True)
        self.fields["Foto"] = photo_field
        photo_layout = QHBoxLayout()
        photo_layout.addWidget(photo_field)
        select_photo_button = QPushButton("Selecionar Foto")
        select_photo_button.clicked.connect(self.select_photo)
        photo_layout.addWidget(select_photo_button)
        form_layout.addRow("Foto", photo_layout)

        layout.addLayout(form_layout)

        tutor_section = QGroupBox("Tutor")
        tutor_form_layout = QFormLayout(tutor_section)
        for field_name in (
            "Nome do Tutor",
            "Telefone",
            "Contato de Emergência",
        ):
            field = QLineEdit()
            self.fields[field_name] = field
            tutor_form_layout.addRow(field_name, field)

        layout.addWidget(tutor_section)

        medical_section = QGroupBox("Informações Médicas")
        medical_form_layout = QFormLayout(medical_section)
        for field_name in (
            "Alergias",
            "Medicamentos em uso",
            "Doenças conhecidas",
            "Vacinas",
            "Observações",
        ):
            field = QLineEdit()
            self.fields[field_name] = field
            medical_form_layout.addRow(field_name, field)

        layout.addWidget(medical_section)

        buttons_layout = QHBoxLayout()
        save_button = QPushButton("Salvar")
        cancel_button = QPushButton("Cancelar")
        save_button.clicked.connect(self.save)
        cancel_button.clicked.connect(self.close)
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(cancel_button)
        layout.addLayout(buttons_layout)

        self.resize(480, 650)

    def select_photo(self) -> None:
        photo_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Foto",
        )
        if photo_path:
            photo_field = self.fields["Foto"]
            if isinstance(photo_field, QLineEdit):
                photo_field.setText(photo_path)

    def field_value(self, field_name: str) -> str:
        field = self.fields[field_name]
        if isinstance(field, QComboBox):
            return field.currentText()
        if isinstance(field, QLineEdit):
            return field.text()
        return ""

    def set_field_error(self, field_name: str, has_error: bool) -> None:
        field = self.fields[field_name]
        field.setStyleSheet(
            "border: 2px solid #c62828;" if has_error else ""
        )

    def pet_validation_errors(self) -> dict[str, str]:
        errors: dict[str, str] = {}

        if not self.field_value("Nome do Pet").strip():
            errors["Nome do Pet"] = "Nome do Pet é obrigatório."
        if self.field_value("Espécie") not in ("Cão", "Gato"):
            errors["Espécie"] = "Espécie é obrigatória: selecione Cão ou Gato."
        if not self.field_value("Raça").strip():
            errors["Raça"] = "Raça é obrigatória."

        age = self.field_value("Idade").strip()
        if age and (not age.isdigit() or int(age) <= 0):
            errors["Idade"] = "Idade deve ser um número inteiro positivo."

        weight = self.field_value("Peso").strip()
        if weight:
            try:
                valid_weight = float(weight.replace(",", ".")) > 0
            except ValueError:
                valid_weight = False
            if not valid_weight:
                errors["Peso"] = "Peso deve ser um número decimal positivo."

        photo = self.field_value("Foto").strip()
        if photo and not QImageReader.canRead(photo):
            errors["Foto"] = "Foto deve ser um arquivo de imagem."

        for field_name in (
            "Nome do Pet",
            "Espécie",
            "Raça",
            "Sexo",
            "Idade",
            "Peso",
            "Cor",
            "Foto",
        ):
            self.set_field_error(field_name, field_name in errors)

        return errors

    def save(self) -> None:
        pet_errors = self.pet_validation_errors()
        if pet_errors:
            QMessageBox.warning(
                self,
                "Cadastro do Pet",
                "Cadastro não realizado:\n" + "\n".join(pet_errors.values()),
            )
            return

        missing_fields = [
            field_name
            for field_name in ("Nome do Tutor",)
            if not self.field_value(field_name).strip()
        ]
        if missing_fields:
            QMessageBox.warning(
                self,
                "Cadastro do Pet",
                "Preencha os campos obrigatórios: "
                + ", ".join(missing_fields)
                + ".",
            )
            return

        self.saved_data = {
            field_name: self.field_value(field_name)
            for field_name in self.fields
        }
        QMessageBox.information(
            self,
            "Cadastro do Pet",
            "Cadastro realizado com sucesso.",
        )
        self.emergency_sheet_window = EmergencySheetWindow(self.saved_data)
        self.emergency_sheet_window.show()


def open_registration_window(main_window: QWidget) -> None:
    registration_window = PetRegistrationWindow()
    main_window.registration_window = registration_window
    registration_window.show()


def build_window() -> QWidget:
    window = QWidget()
    window.setWindowTitle("PETPASS AI")

    layout = QVBoxLayout(window)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    for text in (
        "PETPASS AI",
        "Ficha Inteligente para Pets",
        "Sistema em desenvolvimento experimental.",
    ):
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

    new_registration_button = QPushButton("Novo Cadastro")
    new_registration_button.clicked.connect(
        lambda: open_registration_window(window)
    )
    layout.addWidget(new_registration_button)

    window.resize(480, 240)
    return window


def main() -> int:
    app = QApplication(sys.argv)
    window = build_window()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
