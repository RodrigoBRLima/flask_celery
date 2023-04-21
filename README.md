# Flash Celery

exemplo de uso do Flask com o Celery

inicializar o worker 
celery -A tasks worker -l info -P eventlet

pip install flower para acompanhar o que foi processado na porta localhost:5555
