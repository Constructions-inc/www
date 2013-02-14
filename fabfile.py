from fabric.api import *

env.user = 'dolphin-emu'
env.hosts = ['ssh.alwaysdata.com']

def deploy(root, branch):
    activate = "source /home/dolphin-emu/venv/www/bin/activate"
    with cd(root):
        run("git pull")
        run("git checkout %s" % branch)
        run(activate + " && python manage.py collectstatic --noinput")
        with cd("dolweb"):
            run("msgfmt localefixes/locale/ko/LC_MESSAGES/django.po -o "
                       "localefixes/locale/ko/LC_MESSAGES/django.mo")
            run(activate + "&& django-admin.py compilemessages")

def deploy_stable():
    deploy("/home/dolphin-emu/apps/www", "stable")

def deploy_dev():
    deploy("/home/dolphin-emu/apps/devwww", "master")
