"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    RegulationActModel,
    ThesisModel,
)


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date="01.01.2021",
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )


@pytest.fixture
def regulation_act_fixture() -> RegulationActModel:
    """
    Фикстура модели закона.
    :return: RegulationActModel
    """

    return RegulationActModel(
        type="Федеральный закон",
        title="Наука как искусство",
        accept_date="01.01.2021",
        number="123",
        official_source="Научный журнал",
        publication_year=2020,
        version=1,
        article_number=2,
        edition="01.01.2021",
    )


@pytest.fixture
def thesis_fixture() -> ThesisModel:
    """
    Фикстура модели диссертации.

    :return: ThesisModel
    """

    return ThesisModel(
        author="Иванов И.М.",
        title="Наука как искусство",
        degree="д-р. / канд.",
        field="экон.",
        field_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=999,
    )
