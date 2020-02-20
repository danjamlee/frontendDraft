from flask import Flask, render_template

# fakedata = {"hi":"hey",
#             "what":"hh"}
# fakedata2 = {"ny income":"$44000"}

# entireDataset = {
#    's': {sneakerinfo},
#     'income': IncomeInfo
# }

# , data = sneakerjson
#            , data3=fakedata2 
app = Flask(__name__)

@app.route('/')
def project():
   return render_template("index.html")

@app.route('/map')
def map():
    return render_template("Project3.html")

if __name__ == "__main__": 
    app.run(debug = True)