from flask import Flask, jsonify, make_response, request, abort
from api_helper import ApiHelper


app = Flask(__name__)
apiHelp = ApiHelper()


# Get category articles
@app.route('/api/articles/category=<category>', methods=['GET'])
# curl -i http://localhost:5000/api/articles/category=<category>
def getArticlesByCategory(category):
    articles = apiHelp.getArticlesByCategory(category)
    print(articles)
    if len(articles) == 0:
        abort(404)
    return jsonify({'articles': articles})


# Save Article to DB
@app.route('/api/articles/add/sources=<sources>', methods=['GET'])
# curl -i http://localhost:5000/api/add/articles/sources=<sources>
def saveArticlesBySources(sources):
    response = None
    response = apiHelp.insertArticles(sources.split(','))
    print(response)
    if response == None:
        abort(404)
    return jsonify({'Response': response})


# Error handling
@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def badRequest(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')

