from flask import Flask, render_template, request, redirect, url_for;

app = Flask(__name__)

@app.route('/')
def index():
    live=[{'India':[{'rohit':[140,113],'kohli':[77,65],
    'dhoni':[57,78],'jadeja':[0,1],'raina':[26,18],'pandya':[35,16]},{
    'amir':[3,47,10],
    'shadab':[1,71,10],'shoaib':[1,84,9],'hassan':[1,104,20]
    }],'score':[336,5],'overs':50}]
    key=list(live[0].keys())
    return render_template('Home_page.html',team=key,live_s=live)

@app.route('/home')
def Home_page():
    return render_template('Home_page.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/sample')
def sample():
    return render_template('sample.html')
    


if __name__ == '__main__':
    app.run(debug=True)
