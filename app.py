from flask import Flask, render_template, request
from endpoints.get_countries import countries_response
from endpoints.get_operator_by_phone import get_operator
from endpoints.create_btcpay_invoice import create_invoice
from endpoints.country import get_country
from endpoints.send_topup import send_topup
from endpoints.convert_currency import convert_to_usd
from endpoints.get_operator_that_support_data import get_data_operator
from endpoints.get_operators import operators_response

app = Flask(__name__)

phone_number = ''
country_iso = ''
operator_id = ''
currency = ''
amount = ''
operator = {}

@app.route('/')
def index():
    return render_template('index.html', countries_response=countries_response)

@app.route('/countries')
def countries_page():
    return render_template('countries.html', countries_response=countries_response)

@app.route('/data')
def data_page():
    return render_template('data.html', countries_response=countries_response)

@app.route('/operators')
def operators():
    return render_template('operators.html', operators_response=operators_response)

@app.route('/operator/<id>')
def operator(id=None):
    return render_template('operator.html', operators_response=operators_response, id=id)

@app.route('/airtime')
def airtime_page():
    return render_template('airtime.html', countries_response=countries_response)

@app.route('/topup', methods=['POST'])
def search_operator():
    global phone_number, country_iso, operator_id, currency, operator
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        country_iso = request.form['country']
        operator = get_operator(number=phone_number,country_iso=country_iso)
        operator_id = operator['operatorId']
        currency = get_country(iso=country_iso)['currencyCode']
        return render_template('continue.html', operator=operator, country_iso=country_iso, currency=currency)

@app.route('/data/topup', methods=['POST'])
def search_data_operator():
    global phone_number, country_iso, operator_id, currency, operator
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        country_iso = request.form['country']
        operator = get_data_operator(number=phone_number,country_iso=country_iso)
        operator_id = operator['operatorId']
        currency = get_country(iso=country_iso)['currencyCode']
        return render_template('data_continue.html', operator=operator, country_iso=country_iso, currency=currency)

@app.route('/checkout', methods=['POST'])
def checkout():
    global amount, currency
    if request.method == 'POST':
        amount = request.form['amount']
        currency = request.form['currency']
        try:
            checkout_link = create_invoice(amount=amount, currency=currency)
        except KeyError:
            checkout_link = create_invoice(amount=convert_to_usd(amount=amount, currency=currency), currency='USD')
        finally:
            return render_template('checkout.html', link=checkout_link)

@app.route('/data/checkout', methods=['POST'])
def data_checkout():
    global amount, currency
    if request.method == 'POST':
        amount = request.form['amount']
        currency = request.form['currency']
        try:
            checkout_link = create_invoice(amount=amount, currency=currency)
        except KeyError:
            checkout_link = create_invoice(amount=convert_to_usd(amount=amount, currency=currency), currency='USD')
        finally:
            return render_template('checkout.html', link=checkout_link)

@app.route('/success')
def top_up():
    if operator['fixedAmounts'] == []:
        if operator['minAmount'] <= amount <= operator['maxAmount']:
            topup_result = send_topup(amount=amount, operator_id=operator_id, number=phone_number,country_code=country_iso)
            if topup_result == '200':
                return render_template('success.html')
            else:
                return  render_template('failed.html')
    elif amount in operator['fixedAmounts']:
        topup_result = send_topup(amount=amount, operator_id=operator_id, number=phone_number, country_code=country_iso)
        if topup_result == '200':
            return render_template('success.html')
        else:
            return render_template('failed.html')





if __name__ == '__main__':
    app.debug = True
    app.run()