import click
from proxy import iniciar_servidor_proxy

@click.group()

def cli():
    pass


@cli.command()
@click.option('--port',default = 8080, help='Perto en el que se ejecutará el servidor')
@click.option('--origin', required = True, help='URL servidor de origen que se enviaran las solicitudes')
def run(port,origin):
    host = '127.0.0.1'        
    iniciar_servidor_proxy(host, port, origin)

@cli.command()
def clear_cache():
    from proxy import cache
    cache.clear()
    click.echo('Caché borrada exitosamente!')

if __name__ == '__main__':
    cli()
