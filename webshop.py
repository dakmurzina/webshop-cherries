from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Products in the store
products = [
    {
        "type": "clothing",
        "id": "0",
        "name": "Black Elegance Dress",
        "price": 300,
        "img": "dress.png",
        "description": "Choose elegance, sophistication, and style with our Black Elegance Dress. Elevate your evening attire and captivate the room with your impeccable fashion sense. Order yours today and let the Black Elegance Dress become your go-to piece for unforgettable moments."
    },
    {
        "type": "clothing",
        "id": "1",
        "name": "Shimmering Nights Skirt",
        "price": 85,
        "img": "skirt2.png",
        "description": "Indulge in the allure of our Shimmering Nights Skirt and make a lasting impression wherever you go. Elevate your style with its undeniable beauty and create memories in an outfit that exudes sophistication and charm. Order yours today and let the Shimmering Nights Skirt be the centerpiece of your wardrobe."
    },
    {
        "type": "clothing",
        "id": "2",
        "name": "Blushing Petals Cardigan",
        "price": 45,
        "img": "cardigan.png",
        "description": "Embrace the softness and elegance of our Blushing Petals Cardigan and add a touch of pink perfection to your wardrobe. Elevate your everyday outfits and express your individuality with this versatile and charming piece. Order yours today and experience the joy of cozy and fashionable dressing."
    },
    {
        "type": "clothing",
        "id": "3",
        "name": "Sky High Jeans",
        "price": 40,
        "img": "jeans.png",
        "description": "Embrace the serene and enchanting charm of our Sky High Jeans and infuse your wardrobe with a touch of lightness and grace. Elevate your denim game with this whimsical and stylish pair that brings a breath of fresh air to your everyday outfits. Order yours today and experience the joy of fashionable and comfortable dressing."
    },
    {
        "type": "clothing",
        "id": "4",
        "name": "Classic Black T-Shirt",
        "price": 25,
        "img": "t-shirt.png",
        "description": "Invest in the timeless appeal and comfort of our Classic Black T-Shirt and elevate your everyday wardrobe. Experience the effortless style and versatility that this essential piece brings to your fashion repertoire. Order yours today and enjoy the perfect combination of style, comfort, and enduring appeal."
    },
    {
        "type": "clothing",
        "id": "5",
        "name": "Summer Breeze Top",
        "price": 15,
        "img": "top.png",
        "description": "Make a statement with our Summer Breeze Top and let it become your go-to piece for all your summer escapades. Experience the perfect combination of style, comfort, and breathability, allowing you to enjoy the sunny season to the fullest. Order yours today and welcome the refreshing breeze of summer into your wardrobe."
    },
    {
        "type": "shoes",
        "id": "6",
        "name": "Sunlit Radiance High Heels",
        "price": 90,
        "img": "heels.png",
        "description": "Elevate your summer style with the Sunlit Radiance High Heels and add a touch of vibrant elegance to your wardrobe. These heels will undoubtedly become your go-to pair for making a stylish statement and capturing the spirit of the sunny season. Order yours today and step into the summer with confidence and grace."
    },
    {
        "type": "shoes",
        "id": "7",
        "name": "Sunset Breeze Summer Sandals",
        "price": 38,
        "img": "sandals.png",
        "description": "Experience the ultimate combination of style, comfort, and versatility with our Sunset Breeze Summer Sandals. Perfect for beach vacations, garden parties, or simply enjoying a leisurely day in the sun, these sandals will become your go-to footwear choice for the season. Embrace the essence of summer and elevate your warm-weather style by adding a pair of Sunset Breeze sandals to your collection today."
    },
    {
        "type": "shoes",
        "id": "8",
        "name": "Elegance in Bloom Shoes",
        "price": 65,
        "img": "summer-shoes.png",
        "description": "Indulge in the beauty and elegance of our Elegance in Bloom Shoes and experience the epitome of sophistication. Whether you're attending a wedding, a gala, or simply want to add a touch of glamour to your everyday attire, these shoes are the perfect choice to make you feel confident and fabulous. Upgrade your shoe collection and embrace timeless elegance today."
    },
    {
        "type": "shoes",
        "id": "9",
        "name": "Active Stride Trainers",
        "price": 110,
        "img": "trainers.png",
        "description": "Step into a world of style and performance with our Active Stride Trainers. Experience the perfect blend of comfort, support, and fashion-forward design, empowering you to reach your fitness goals while feeling confident and stylish. Upgrade your active footwear today and embrace the journey of an active, fashionable lifestyle."
    },
    {
        "type": "accessories",
        "id": "10",
        "name": "Celestial Elegance Necklace",
        "price": 130,
        "img": "necklace.png",
        "description": "Indulge in the celestial allure and timeless elegance of our Celestial Elegance Necklace. Perfect as a gift for yourself or a loved one, this piece of jewelry is sure to become a cherished heirloom, symbolizing beauty, grace, and celestial wonder. Embrace the celestial realm and adorn yourself with a touch of heavenly elegance."
    },
    {
        "type": "accessories",
        "id": "11",
        "name": "Radiant Harmony Bracelet",
        "price": 90,
        "img": "bracelet.png",
        "description": "Indulge in the beauty and grace of our Radiant Harmony Bracelet. Perfect as a gift for yourself or a loved one, this piece of jewelry is an exquisite symbol of elegance and harmony. Elevate your style and celebrate the radiance within with this stunning bracelet."
    },
    {
        "type": "accessories",
        "id": "12",
        "name": "Eternal Sparkle Earrings",
        "price": 80,
        "img": "earings.png",
        "description": "Indulge in the radiance and sophistication of our Eternal Sparkle Earrings. Whether you're treating yourself or surprising a loved one, these earrings are a symbol of eternal beauty and timeless elegance. Embrace your inner sparkle and let these earrings be the perfect finishing touch to your glamorous ensemble."
    },
    {
        "type": "accessories",
        "id": "13",
        "name": "Timeless Brilliance Ring",
        "price": 65,
        "img": "ring.png",
        "description": "Indulge in the beauty and significance of our Timeless Brilliance Ring. Whether you're looking for a symbol of eternal love or a stunning statement piece, this ring is a celebration of timeless beauty and enduring style. Embrace the brilliance and create unforgettable moments with this exceptional ring."
    }
]

# Filter products in the store for three different pages
clothing_products = [
    product for product in products if product['type'] == "clothing"]
shoes_products = [
    product for product in products if product['type'] == "shoes"]
accessories_products = [
    product for product in products if product['type'] == "accessories"]

# Calculate the number of items in the cart


def calculate_no_items_in_cart():
    cart = session['cart'] if 'cart' in session else {}
    return sum(list(cart.values()))


@app.route('/')
def home():
    return render_template('index.html', total_no_items=calculate_no_items_in_cart())


@app.route('/about')
def about():
    return render_template('about.html', total_no_items=calculate_no_items_in_cart())


@app.route('/clothing')
def show_clothes():
    return render_template('products.html', products=clothing_products, total_no_items=calculate_no_items_in_cart())


@app.route('/shoes')
def show_shoes():
    return render_template('products.html', products=shoes_products, total_no_items=calculate_no_items_in_cart())


@app.route('/accessories')
def show_accessories():
    return render_template('products.html', products=accessories_products, total_no_items=calculate_no_items_in_cart())


@app.route('/clothing/<id>', methods=['GET', 'POST'])
def show_clothes_detail(id):
    quantity = None
    if request.method == 'POST':
        quantity = int(request.form.get('input'))
        add_to_cart(id, quantity)
    return render_template('product.html', products=clothing_products, id=id, total_no_items=calculate_no_items_in_cart(), input=quantity)


@app.route('/shoes/<id>', methods=['GET', 'POST'])
def show_shoes_detail(id):
    quantity = None
    if request.method == 'POST':
        quantity = int(request.form.get('input'))
        add_to_cart(id, quantity)
    return render_template('product.html', products=shoes_products, id=id, total_no_items=calculate_no_items_in_cart(), input=quantity)


@app.route('/accessories/<id>', methods=['GET', 'POST'])
def show_accessories_detail(id):
    quantity = None
    if request.method == 'POST':
        quantity = int(request.form.get('input'))
        add_to_cart(id, quantity)
    return render_template('product.html', products=accessories_products, id=id, total_no_items=calculate_no_items_in_cart(), input=quantity)


@app.route('/cart')
def show_cart():
    if 'cart' in session:
        cart = session['cart']
    products_in_cart = []
    for k in cart.keys():
        for product in products:
            if product['id'] == k:
                products_in_cart.append(product)
    total_price = calculate_total_price()
    total_no_items = sum(list(cart.values()))
    return render_template('cart.html', items=products_in_cart, total_price=total_price, cart=cart, total_no_items=calculate_no_items_in_cart())


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# Add items and their quantity to the cart


def add_to_cart(id, quantity):
    cart = session['cart'] if 'cart' in session else {}
    if id not in cart:
        cart[id] = quantity
    else:
        cart[id] += quantity
    session['cart'] = cart

# Calculate the total price


def calculate_total_price():
    total_price = 0
    if 'cart' in session:
        cart = session['cart']
    for id, quantity in cart.items():
        product_price = [product['price']
                         for product in products if product['id'] == id][0]
        total_price += product_price * quantity
    return total_price
