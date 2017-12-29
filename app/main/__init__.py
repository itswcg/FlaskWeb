from flask import Blueprint

main = Blueprint('main', __name__)

from . import forms, views
from ..models import Permission

@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)