from standard_features import build_standard
from separate_text import __separate__
from openpyxl import load_workbook
from peewee import fn
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from types import NoneType
from database.models.norma import Norma

subquery = (Norma.select(fn.MIN(Norma.id)).group_by(Norma.codigo))

duplicates = (Norma.select().where(Norma.id.not_in(subquery)))

for duplicate in duplicates:
    duplicate.delete_instance()