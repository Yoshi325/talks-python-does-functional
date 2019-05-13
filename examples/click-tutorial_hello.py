import click

from functools import partial


@click.command()
@click.argument('name')
@click.option('--red',   '-r', is_flag=True)
@click.option('--count', '-c', type=int, default=1)
def cli(name, red, count):
    ''' Help for cli command. (a command that says hello) '''
    # click.echo(f'red: {red}', err=True)
    echo_ = click.secho
    echo_ = partial(echo_, f'Hello, {name}!')
    echo_ = partial(echo_, fg=('red' if red else 'black'))
    for i in range(count):
        echo_()


if ('__main__' == __name__):
    cli()