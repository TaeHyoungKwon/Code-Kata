import json
import math


def statement(invoice, plays):

    def amount_for(a_performance, play):
        result = 0
        if play["type"] == "tragedy":
            result = 40000
            if a_performance["audience"] > 30:
                result += 1000 * (a_performance["audience"] - 30)
        elif play["type"] == "comedy":
            result = 30000
            if a_performance["audience"] > 20:
                result += 10000 + 500 * (a_performance["audience"] - 20)
            result += 300 * a_performance["audience"]
        else:
            raise Exception("알 수 없는 장르")
        return result

    total_amount = 0
    volume_credits = 0
    result = f"청구 내역 (고객명: {invoice['customer']})\n"
    dollar_format = '${:,.2f}'

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = amount_for(perf, play)
        volume_credits += max(perf["audience"] - 30, 0)

        if play["type"] == "comedy":
            volume_credits += math.floor(perf["audience"] / 5)

        result += f' {play["name"]}: {dollar_format.format(this_amount / 100)} ({perf["audience"]}석)\n'
        total_amount += this_amount

    result += f"총액: {dollar_format.format(total_amount / 100)}\n"
    result += f"적립 포인트': {volume_credits}점\n"
    return result


if __name__ == '__main__':
    with open('invoices.json') as json_file:
        invoice = json.load(json_file)[0]

    with open('plays.json') as json_file:
        plays = json.load(json_file)

    print(statement(invoice, plays))


