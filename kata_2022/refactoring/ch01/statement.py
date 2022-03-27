from typing import Any

from kata_2022.refactoring.ch01.statement_data import create_statement_data, get_amount_for, get_usd


def statement(invoice: dict[str, Any], plays: dict[str, Any]) -> str:
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data: dict) -> str:
    result = f'Invoice (Customer: {data["customer"]})\n'
    for performance in data["performances"]:
        result += (
            f'\t{performance["play"]["name"]}: '
            f"{get_usd(get_amount_for(performance))} "
            f'({performance["audience"]} Seats)\n'
        )
    result += f"Total Amount: {get_usd(data['total_amount'])}\n"
    result += f"Volume Credits: {data['total_volume_credits']}\n"
    return result


def html_statement(invoice: dict, plays: dict) -> str:
    return render_html(create_statement_data(invoice, plays))


def render_html(data: dict) -> str:
    result = f"<h1>Invoice (Customer: {data['customer']})</h1>\n"
    result += "<table>\n"
    result += "<tr><th>Play</th><th>Seats</th><th>Price</th></tr>\n"

    for perf in data["performances"]:
        result += (
            f"\t<tr><td>{perf['play']['name']}</td>"
            f"<td>({perf['audience']} Seats)</td>"
            f"<td>{get_usd(perf['amount'])}</td></tr>\n"
        )

    result += "</table>\n"
    result += f"<p>Total Amount: <em>{get_usd(data['total_amount'])}</em></p>\n"
    result += (
        f"<p>Volume Credits: <em>{data['total_volume_credits']}</em></p>\n"
    )
    return result