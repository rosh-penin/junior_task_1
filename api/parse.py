import numpy as np
from pandas import read_excel

from constants import SHEET_NAME
from validators import non_empty_row, validate_length


async def parse_excel(file) -> dict:
    readed_file = read_excel(
        file,
        sheet_name=SHEET_NAME
    ).replace({np.nan: None})
    zipped_file = list(zip(
        readed_file['Unnamed: 0'].iloc[1:],
        readed_file['Unnamed: 1'][1:]
    ))
    await validate_length(readed_file, readed_file.columns)
    result: dict = {}
    for index, row in readed_file.iloc[1:].iterrows():
        await non_empty_row(row)
        project_tuple_as_key = zipped_file[index - 1]
        values_for_project: list = []
        for cl_idx in range(2, len(readed_file.columns), 2):
            values_for_project.append({
                'date': readed_file.columns[cl_idx].date(),
                'plan_val': row.iloc[cl_idx],
                'fact_val': row.iloc[cl_idx + 1]
            })
        result[project_tuple_as_key] = values_for_project
    return result
