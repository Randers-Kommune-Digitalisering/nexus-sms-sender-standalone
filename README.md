# nexus-sms-sender-standalone
Script for sending SMS for orders in Nexus "Depot" -> "Selvafhentning", using Computopic SMS gateway.

## Run
* Install python
* Install requirements:  ```pip install -r requirements.txt```
* Set enviroment variables or create a [.env file](.env.example)
* Run script ```python main.py```

## Dependencies
Credentials for a Computopic SMS gateway. <br>
Access to Nexus api using client credentials flow (OAuth2). Nexus user needs read/write access to "Selvafhentning" list and orders.
