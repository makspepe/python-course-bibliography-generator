"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    RegulationActModel,
    ThesisModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class APABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year) $title ($edition) $city: $publishing_house, $pages p."
        )

    def substitute(self) -> str:

        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template("$website ($access_date) $article $link")

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APACollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year) $article_title, $collection_title $city: $publishing_house, $pages p."
        )

    def substitute(self) -> str:

        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )


class APAThesis(BaseCitationStyle):
    """
    Форматирование для диссертаций.
    """

    data: ThesisModel

    @property
    def template(self) -> Template:
        return Template(
            "$author ($year) $title / $city, $pages p."
        )

    def substitute(self) -> str:
        logger.info('Форматирование диссертации "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class APARegulationAct(BaseCitationStyle):
    data: RegulationActModel

    @property
    def template(self) -> Template:
        return Template(
            "($publication_year) $title, $type, $official_source, $number, edited $edition"
        )

    def substitute(self) -> str:
        logger.info('Форматирование законодательного акта "%s" ...', self.data.title)

        return self.template.substitute(self.data.dict())


class APACitationFormatter(BaseCitationFormatter):
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        InternetResourceModel.__name__: APAInternetResource,
        ArticlesCollectionModel.__name__: APACollectionArticle,
        RegulationActModel.__name__: APARegulationAct,
        ThesisModel.__name__: APAThesis,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
