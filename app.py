import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == "GET":
        # get url
        query = requests.get('https://restcountries.eu/rest/v2/all')
        for dic in query.json():
            for k, v in dic.items():
                if k == 'name':
                    results.append(v)
        return render_template('page.html', results=results)
    elif request.method == "POST":
        input = request.form['country']
        query = requests.get('https://restcountries.eu/rest/v2/name/' + input)
        for dic in query.json():
            print(dic)
            oneSet = {}
            oneSet['name'] = dic['name']
            oneSet['capital'] = dic['capital']
            oneSet['timezones'] = dic['timezones']
            oneSet['currencies'] = dic['currencies']
            oneSet['languages'] = dic['languages']
            results.append(oneSet)
        return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
