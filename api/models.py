from datetime import date as dt_date

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from engine import Base, engine


class FileVersionModel(Base):
    """ORM модель для таблицы с версиями импортированных файлов."""
    __tablename__ = 'fileversions'
    version: Mapped[str] = mapped_column(primary_key=True)
    projects: Mapped[list['ProjectModel']] = relationship(
        back_populates='version'
    )


class ProjectModel(Base):
    """ORM модель для таблицы с кодом и названием проекта."""
    __tablename__ = 'projects'
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[int]
    name: Mapped[str] = mapped_column(String(100))
    version_version: Mapped[str] = mapped_column(ForeignKey(
        'fileversions.version',
        ondelete='CASCADE'
    ))
    version: Mapped['FileVersionModel'] = relationship(
        back_populates='projects'
    )
    values: Mapped[list['ValueModel']] = relationship(
        back_populates='project'
    )
    UniqueConstraint('code', 'name', 'version',
                     name='unique_project_for_version')


class ValueModel(Base):
    """ORM модель для таблицы с данными проекта."""
    __tablename__ = 'values'
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[dt_date]
    plan_val: Mapped[float] = mapped_column(nullable=True)
    fact_val: Mapped[float] = mapped_column(nullable=True)
    project_id: Mapped[int] = mapped_column(ForeignKey(
        'projects.id',
        ondelete='CASCADE'
    ))
    project: Mapped['ProjectModel'] = relationship(back_populates='values')
    UniqueConstraint('date', 'project', name='only_one_date_for_project')


Base.metadata.create_all(engine)
