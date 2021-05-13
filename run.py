from flask import Flask, request, json, abort

app = Flask(__name__)
@app.route('https://webhook.site/5ae61ad3-cf23-4fb5-bfb2-7b2161bfd9b3/webhook',methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success',200
    else:
        abort(200)

if __name__ == '__main__':
    app.run()
