from flask import Blueprint
from extensoes.tasks import celery, add

bp = Blueprint('tasks', __name__)


@bp.route('/add')
def add(x=2, y=4):
    resultado = celery.send_task('tasks.add', args=[x, y])
    resultado = add.delay(4,5)
    return f'Resultado da soma: {resultado.get()}'
