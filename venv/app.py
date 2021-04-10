from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        rawdata = request.form.get("rawdata")
        new_dict = eval(str(rawdata))
        def output(node):
            for i in new_dict["relation"]:
                if i["child"] == node:
                    yield i["parent"]
        datadict={}
        for items in new_dict["node_ids"]:
            res = []
            nodes = output(items)
            val = [i for i in nodes]
            for node in val:
                res.extend([j for j in output(node)])
                datadict.update({items:res + val + [items]})
        data = datadict
        return render_template('home.html', data=data)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')