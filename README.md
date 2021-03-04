Current repo represents a simple application for warehouse. 
To start it you need: 

* Clone this repo;
* Go to the repo folder warehouse;
* Create a virtual environment python3 -m venv warehouse;
* Activate it source warehouse/bin/activate
* Install the requirements `pip install -r requirements.txt`;
* Set PYTHONPATH with current directory to export `PYTHONPATH=current_folder/app`
* Start an app with `python run.py`

Application will start on http://127.0.0.1:5000/ if default env settings are used.

Which actions are avalible: 
* Creation of articles:
  curl --location --request POST 'http://127.0.0.1:5000/inventory' --header 'Content-Type: application/json' --data-raw '{}'
(instead of data-raw json with inventory has to be placed)
* Receive articles:
curl --location --request GET 'http://127.0.0.1:5000/inventory'
* Creation of products:
  curl --location --request PUT 'http://127.0.0.1:5000/products' \
--header 'Content-Type: application/json' \
--data-raw '{}' 
(instead of data-raw json with inventory has to be placed)
Products will be created only if there is enough articles in the inventory.
* List of available products:
  curl --location --request GET 'http://127.0.0.1:5000/products'
* Cell of the product
  curl --location --request PATCH 'http://127.0.0.1:5000/products/product_name'
  (instead of the product name actual product name should be)

Test are available in the `test` folder and can be executed with `pytest` command