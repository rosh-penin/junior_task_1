from uuid import uuid4

from engine import Session
from exceptions import BdSaveException
from models import FileVersionModel, ProjectModel, ValueModel


async def create_version_and_projects(data: dict) -> dict | None:
    """
    Функция заполнения SQL-таблиц данными из обработанного Pandas файла.
    В этой функции создаются версия файла и проекты, связанные с ней.
    Уникальность каждой версии файла придается через uuid4.
    """
    with Session() as session:
        session.begin()
        new_dict: dict[ProjectModel, list[dict]] = {}
        try:
            while True:
                version = str(uuid4())
                if not session.query(FileVersionModel.version).filter_by(
                    version=version
                ).first():
                    version = FileVersionModel(version=version)
                    session.add(version)
                    break
            for key, values_all in data.items():
                project = ProjectModel(
                    code=key[0],
                    name=key[1],
                    version_version=version.version
                )
                new_dict[project] = values_all
                session.add(project)
        except Exception:
            session.rollback()
            raise BdSaveException
        else:
            session.commit()
        return new_dict


async def create_values_for_project(data: dict) -> None:
    """
    Функция заполнения SQL-таблиц данными из обработанного Pandas файла.
    В этой функции создаются данные для каждого связанного проекта.
    """
    with Session() as session:
        session.begin()
        try:
            for key, values_all in data.items():
                for values in values_all:
                    session.add(ValueModel(
                        **values,
                        project=key
                    ))
        except Exception:
            session.rollback()
            raise BdSaveException
        else:
            session.commit()
