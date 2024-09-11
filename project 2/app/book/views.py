from flask import render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
import os
from app.models import db, Books
from app.book import bookBlueprint
from app.book.forms import BooksForm

@bookBlueprint.route("/", endpoint="home")
def books_list():
    books = Books.query.all()
    return render_template("books/home.html", books=books)


@bookBlueprint.route("/create", endpoint="create", methods=["GET", "POST"])
def books_create():
    form = BooksForm()
    if form.validate_on_submit():
        image_filename = secure_filename(form.image.data.filename)
        print(image_filename)
        if form.image.data:
            form.image.data.save(os.path.join('static/images', image_filename))

        book = Books(
            title=form.Booktitle.data,
            description=form.description.data,
            pages=form.pages.data,
            image=image_filename
        )
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('books.home')) 

    return render_template('books/create.html', form=form)


@bookBlueprint.route('/<int:id>/edit', methods=['GET', 'POST'])
def books_edit(id):
    book = Books.query.get_or_404(id)
    form = BooksForm()

    if form.validate_on_submit():
        book.title = form.Booktitle.data
        book.description = form.description.data
        book.pages = form.pages.data

        if form.image.data:
            image_filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join('static/images', image_filename))
            book.image = image_filename

        db.session.commit() 
        return redirect(url_for('books.home', id=book.id))

    elif request.method == 'GET':
        form.Booktitle.data = book.title
        form.description.data = book.description
        form.pages.data = book.pages

    return render_template('books/edit.html', form=form, book=book)


@bookBlueprint.route("<int:id>/details", endpoint="details")
def book_show(id):
    book = db.get_or_404(Books, id)
    return render_template("books/details.html", book=book)


@bookBlueprint.route("<int:id>/delete", endpoint="delete", methods=["POST"])
def book_delete(id):
    book = db.get_or_404(Books, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books.home"))