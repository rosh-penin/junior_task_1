from pandas import DataFrame, Series

from constants import COLUMNS_LIMIT, ROWS_LIMIT
from exceptions import EmptyRowException, LimitBreakException


async def validate_length(rows: DataFrame, columns: DataFrame.columns) -> None:
    """
    Проверяет что количество строк и столбцов не превышает заданные лимиты.
    Rows это сам DataFrame, который через len() подсчитывает нужное
    количество строк.
    """
    try:
        assert len(rows) <= ROWS_LIMIT
        assert len(columns) <= COLUMNS_LIMIT
    except AssertionError:
        raise LimitBreakException


async def non_empty_row(row: Series) -> None:
    """
    Если в строке два или меньше значений - это проблема.
    Два значения относятся к Коду и Названию проекта.
    """
    try:
        assert row.count() > 2
    except AssertionError:
        raise EmptyRowException
