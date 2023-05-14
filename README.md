# skillfactory_tasks - 18.6 Currency_converter
"Write and test a Telegram bot that implements the following functionality:

The bot returns the price for a certain amount of currency (euro, dollar, or ruble).
The pytelegrambotapi library should be used when writing the bot.
The user should send a message to the bot in the format <the name of the currency whose price he wants to know> <the name of the currency in which the price of the first currency should be known> <the amount of the first currency>.
When the /start or /help command is entered, the user should be provided with instructions on how to use the bot.
When the /values command is entered, information about all available currencies should be displayed in a readable format.
To get the currency exchange rates, you should use an API and send requests to it using the Requests library.
To parse the received responses, use the JSON library.
In case of a user error (for example, an incorrect or non-existent currency is entered, or the number is entered incorrectly), the custom APIException exception should be called with an explanation text of the error.
The text of any error with the indication of the error type should be sent to the user in messages.
To send requests to the API, describe a class with a static method get_price(), which takes three arguments: the name of the currency whose price you want to know - base, the name of the currency in which you want to know the price - quote, the amount of the converted currency - amount, and returns the required amount in the currency.
The Telegram bot token should be stored in a special config (you can use a .py file).
All classes should be hidden in the extensions.py file."
