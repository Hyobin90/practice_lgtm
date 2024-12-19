# an entry point script
import click


@click.command()
@click.option('--message', '-m', default='LGMT', show_default=True, help='Str to be included in the image.')
@click.argument('keyword')
def cli(keyword: str, message: str):
    """LGTM image generating tool."""
    lgtm()
    click.echo('lgtm') # for testing

def lgtm():
    # logics to be added
    pass
