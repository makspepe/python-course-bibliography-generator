import pytest

from formatters.base import BaseCitationFormatter
from formatters.styles.apa import APACitationFormatter
from formatters.styles.gost import GOSTCitationFormatter
from main import CitationEnum, get_citation_type
from renderer import APARenderer, GOSTRenderer, Renderer


@pytest.mark.parametrize(
    "citation, renderer, formatter",
    [
        (CitationEnum.GOST, GOSTRenderer, GOSTCitationFormatter),
        (CitationEnum.APA, APARenderer, APACitationFormatter),
    ],
)
def test_get_formatted(
    citation: str, renderer: Renderer, formatter: BaseCitationFormatter
) -> None:
    """
    Тестирование получения форматированной строки
    """
    real_formatter, real_renderer = get_citation_type(citation)
    assert real_renderer == renderer
    assert real_formatter == formatter
