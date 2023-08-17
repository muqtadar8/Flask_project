from flask import Flask,jsonify,request
app = Flask(__name__)



books = [{"id":1,"title":"Book1"},
         {"id":2,"title":"Book2"},
         {"id":3,"title":"Book3"},
         {"id":4,"title":"Book4"},
         {"id":5,"title":"Book5"}
         ]

@app.route("/books",methods = ['GET'])
def get_books():
    return books

@app.route("/books/<int:bookid>",methods = ['GET'])
def get_book(bookid):
    for i in books:
        if i['id'] == bookid:
            # return i['title']
            return jsonify(i)
    else: return jsonify({'message':"Book Not Found"}), 404

@app.route("/books",methods = ['POST'])
def create_book():
    data = request.get_json()
    inp = {'id' :len(books)+1,'title':data['title']}
    books.append(inp) 
    return jsonify({'message':"book added successfully"}),201

@app.route("/books",methods = ['DELETE'])
def delete_book():
    data = request.get_json()
    for i in books :
        if i['title'] == data['title']:
            # inp = {"id":i['id'],"title":i['title']}
            inp = i
            break
    books.remove(inp) 
    return jsonify({'message':"book removed successfully"}), 201

if __name__ == '__main__':
    app.run(debug = True,port = '8000',host = '172.18.181.148')



