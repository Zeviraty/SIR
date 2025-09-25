import click
from utils import *

@click.group()
def cli():
    """SIR server management"""
    pass

@cli.group()
def domain():
    """Manage domains"""
    pass

@domain.command()
@click.argument('name', type=str, required=True)
@click.argument('ip', type=str, required=True)
@click.argument('owner', type=str, required=True)
def add(name:str, ip:str, owner: str):
    add_domain(name,ip,owner)

@domain.command()
@click.argument('name', type=str, required=True)
def remove(name:str):
    remove_domain(name)

@cli.group()
def server():
    """Manage other SIR servers"""
    pass

@server.command()
@click.argument('name', type=str, required=True)
@click.argument('ip', type=str, required=True)
def add(name:str, ip:str):
    add_server(name,ip,owner)

@server.command()
@click.argument('name', type=str, required=True)
def remove(name:str):
    remove_server(name)

if __name__ == '__main__':
    cli()
