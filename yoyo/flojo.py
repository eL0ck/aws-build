from __future__ import print_function
import click


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option('--name', '-n', help="Add a name for personalised service.")
def dickhead(name):
    """ Get some recognition from your computer, conviently from the CLI!!  """

    print("Hallo {name}".format(name=name if name else "dickhead"))
