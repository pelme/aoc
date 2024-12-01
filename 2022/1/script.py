
import typer

@typer.run
def main(input: typer.FileText, num: int = typer.Option(1)) -> None:
    groups = input.read().split('\n\n')
    sums = sorted((sum(int(num) for num in group.split()) for group in groups), reverse=True)
    print(sum(sums[:num]))

    return None
