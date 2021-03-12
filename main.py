from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Пейзажи Марса</title>
                      </head>
                      <body>
                      <header>
                        <h1>Пейзажи Марса</h1>
                      </header>
                        <script src="static\js\script.js"></script>
                        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                          <ol class="carousel-indicators">
                            <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"></li>
                            <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"></li>
                            <li data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"></li>
                          </ol>
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="static\img\\2.jpeg" class="d-block w-100" id="ph" alt="...">
                                </div>
                                <div class="carousel-item">
                                  <img src="static\img\\1.jpg" class="d-block w-100" id="ph" alt="...">
                                </div>
                                <div class="carousel-item">
                                  <img src="static\img\\3.jpg" class="d-block w-100" id="ph" alt="...">
                                </div>
                          </div>
                          <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                          </a>
                        </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" 
                    integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" 
                    crossorigin="anonymous"></script>
                    </body>
                    </html>
                    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)