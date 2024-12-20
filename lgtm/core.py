# an entry point script
import click
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image


@click.command()
@click.option('--message', '-m', default='LGMT', show_default=True, help='Str to be included in the image.')
@click.argument('keyword')
def cli(keyword: str, message: str):
    """LGTM image generating tool."""
    lgtm(keyword, message)

def lgtm(keyword: str, message: str):
    with get_image(keyword) as fp:
        save_with_message(fp, message)
