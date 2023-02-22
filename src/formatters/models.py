"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):
    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str


class ThesisModel(BaseModel):
    """
    Модель диссертации:

    .. code-block::

        ThesisModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            degree="кандидат",
            field="информатика",
            field_code="08.00.00",
            city="СПб.",
            year=2020,
            pages=999,
        )
    """

    author: str
    title: str
    degree: str
    field: str
    field_code: str
    city: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class RegulationActModel(BaseModel):
    """
    Модель нормативного акта:

    .. code-block::

        RegulationActModel(
            type="постановление",
            title="Наука как искусство",
            accept_date="01.01.2021",
            number="01.01.01",
            official_source="Официальный источник",
            publication_year=2021,
            version=1,
            article_number=1,
            edition="3-е",
        )
    """

    type: str
    title: str
    accept_date: str
    number: str
    official_source: str
    publication_year: int = Field(..., gt=1900)
    version: int
    article_number: int
    edition: str
