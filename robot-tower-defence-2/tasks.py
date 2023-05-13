from invoke import task


@task
def start(ctx):
    ctx.run("python src/main.py")


@task
def debug(ctx):
    ctx.run("python src/main.py debug")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")


@task
def lint(ctx):
    ctx.run("pylint src")


@task
def build(ctx):
    ctx.run("rm -rf dist/robot_invasion_defence_2")
    ctx.run("pyinstaller src/main.py -n robot_invasion_defence_2 -w --icon=src/resources/images/ui/icon.ico")
    ctx.run("cp -r src/resources dist/robot_invasion_defence_2/")
    ctx.run("cd dist/robot_invasion_defence_2 & mkdir data")
