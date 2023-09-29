from fastapi import Request, UploadFile
from fastapi.responses import JSONResponse

from crud import create_values_for_project, create_version_and_projects
from engine import app
from exceptions import EmptyRowException, LimitBreakException, BdSaveException
from parse import parse_excel


@app.post('/')
async def upload_file(file: UploadFile):
    raw_data = await parse_excel(file.file)
    half_done_data = await create_version_and_projects(raw_data)
    await create_values_for_project(half_done_data)
    return JSONResponse('Запись в базу данных прошла успешно', 201)


@app.exception_handler(EmptyRowException)
async def empty_row_error(request: Request, exc: EmptyRowException):
    return JSONResponse('Все значения в строчке не могут быть пустыми', 400)


@app.exception_handler(LimitBreakException)
async def over_limit(request: Request, exc: LimitBreakException):
    return JSONResponse(
        ('Превышен лимит на допустимое количество строк/'
         'столбцов. Установленные лимиты можно посмотреть в '
         'модуле constants.'),
        400
    )


@app.exception_handler(BdSaveException)
async def unknown_error(request: Request, exc: BdSaveException):
    return JSONResponse('Произошла ошибка при записи в бд.')
