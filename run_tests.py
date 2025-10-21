import pytest

#lista de archivos de pruebas a ejecutar
test_files={
    "tests/tc-001.py",
    "tests/tc-002.py"#,"tests/tc-003.py","tests/tc-004.py"
}

#Argumentos para ejecutar las pruebas: archivos + reportes html
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)