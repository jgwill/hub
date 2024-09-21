import click
from langchain import hub

@click.command()
def jhub():
    prompts = hub.get_prompts('jgwill', 'langchainhub')
    for prompt in prompts:
        click.echo(prompt)

if __name__ == '__main__':
    jhub()