# инструкция по работе с файлом "Makefile" – https://bytes.usc.edu/cs104/wiki/makefile/
.DEFAULT_GOAL := all
# обновление сборки Docker-контейнера
build:
	docker compose build

# генерация документации
docs-html:
	docker compose run --workdir /docs app /bin/bash -c "make html"

# запуск форматирования кода
format:
	docker compose run --workdir / app /bin/bash -c "black src docs/source/*.py; isort src/*.py docs/source/*.py"

# запуск статического анализа кода (выявление ошибок типов и форматирования кода)
lint:
	docker compose run --workdir / app /bin/bash -c "pylint src; flake8 src; mypy src; black --check src"

# запуск автоматических тестов
test:
	docker compose run app pytest --cov=/src --cov-report html:htmlcov --cov-report term --cov-config=/src/tests/.coveragerc -vv
# запуск автоматических тестов с отображением покрытия кода
run:
	docker compose run app python main.py --help

run-gost:
	docker compose run app python main.py --citation gost --path_input /media/input.xlsx --path_output /media/output.docx

run-apa:
	docker compose run app python main.py --citation apa --path_input /media/input.xlsx --path_output /media/output.docx

# запуск всех функций поддержки качества кода
all: format lint test
