from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

from models.database import db
from models.flats import Flats

flat_app = Blueprint("flat_app", __name__)

from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound


# @product_app.route("/", endpoint="list")
# def products_list():
#     products = Product.query.all()
#     return render_template("products/index.html", products=products)
#
#
# @product_app.route("/<int:product_id>/", endpoint="details")
# def product_details(product_id):
#     product = Product.query.filter_by(id=product_id).one_or_none()
#     if product is None:
#         raise NotFound(f"Product with id {product_id} doesn't exist!")
#
#     return render_template(
#         "products/details.html",
#         product=product,
#     )
#
#
# @product_app.route("/add/", methods=["GET", "POST"], endpoint="add")
# def product_add():
#     if request.method == "GET":
#         return render_template("products/add-new.html")
#
#     product = Product(name=request.form.get("product-name"))
#     db.session.add(product)
#     db.session.commit()
#     return redirect(url_for("product_app.list"))


@flat_app.route("/", endpoint="list")
def flats_list():
    flats = Flats.query.all()
    return render_template("flats/index.html", flats=flats)


@flat_app.route("/<int:flat_id>/", methods=["GET", "POST"], endpoint="details")
def flat_details(flat_id):
    flat = Flats.query.filter_by(id=flat_id).one_or_none()
    if flat is None:
        raise NotFound(f"Product with id {product_id} doesn't exist!")
    if request.method == "GET":
        return render_template(
            "flats/details.html",
            flat=flat,
        )
    flat.name = request.form.get("name")
    flat.address = request.form.get("address")
    flat.electricity_t1 = request.form.get("electricity_t1")
    flat.hot_water = request.form.get("hot_water")
    flat.cold_water = request.form.get("cold_water")
    db.session.commit()
    return redirect(url_for("flat_app.list"))


@flat_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def flat_add():
    if request.method == "GET":
        return render_template("flats/add.html")
    flat = Flats(name=request.form.get("name"),
                 address=request.form.get("address"),
                 electricity_t1=request.form.get("electricity_t1"),
                 hot_water=request.form.get("hot_water"),
                 cold_water=request.form.get("cold_water"))
    db.session.add(flat)
    db.session.commit()
    return redirect(url_for("flat_app.list"))
