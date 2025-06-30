import typer
from .query import run_query
app = typer.Typer()

@app.command()
def query():
    """Ställ en fråga mot mishnah-indexet."""
    run_query()

def main():
    app()

if __name__ == "__main__":
    main()