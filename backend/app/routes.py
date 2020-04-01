from flask import render_template, abort
from flask import jsonify, make_response
from app import api as app

@app.errorhandler(404)
def  not_found(error):
    return make_response(
        jsonify({'error':'not found'}), 
        404)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))        

        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')














'''
@app.errorhandler(404)
def  not_found(error):
    return make_response(
        jsonify({'error':'not found'}), 
        404)

@app.route('/api/books', methods=['GET'])    
def get_books():
    return jsonify({'books': books})



@app.route('/api/books/<int:book_id>') 
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify({'book': book})
    abort(404)


@app.route('/api/books', methods=['POST'])
def create_book():
    pass # dica: body em request.form

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    pass # dica: body em request.form

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    pass


@app.route('/')
@app.route('/home')
def home():
    message = 'Hello World'
    return render_template('Index.html', 
        msg = message)

@app.route('/contact')
def contact():
    return 'contact'

@app.route('/api/instituicao', methods=['GET']) 
def institui():
    return jsonify(instituicao)
    '''