# miklos-steel-backend
# Backend for miklos-steel-frontend webshop
# contains the following url enpoints:
# getProducts/ to retrieve all product objects
# addToBasket/ to create a new basket item object which places the quantity sent on hold from the corresponding product object inventory
# removeBasketItem/<str:pk> to remove basket item object with id of pk and increment the corresponding product object inventory with its quantity
# getBasketItems/ to return an array of basket item objects based on the list sent from the frontend
# buyBasket/ this endpoint has the task of deleting the basket objects based on the list sent from the frontend and composing and sending an email to the shop owner based on the information contained in the body of the request.
