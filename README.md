# ISEEndpointUpdate

Python Repository to Interact with Cisco ISE

This is a simple python script to demonstrate Automation capabilities in Cisco Identity Services Engine.

This is a class based implementation which can be further extended as per the need of the user.

#Usecase

Currently the code in this repo will perform following operation
1. Fetch list of all Endpoints.
2. Add Endpoint to Cisco ISE
3. Add Bulk Endpoints to Cisco ISE
4. Delete Endpoints to Cisco ISE

Please Note: To create single Endpoint in Cisco ISE use file "endpoint.json", should you need to add endpoint in bulk you can use bulkendpoint.xml. {Currently JSON support for Bulk Endpoint upload does not work properly}

#Usage

To use the code.
1. Clone the repo in local system.
2. Modify the file config.py as per local details given in config.py
3. Update the required payload file (endpoint.json/bulkendpoint.xml)
4. Use the class as per need of operation.
5. Run the script python3 ISE.py

#Developer 

Madhuri Dewangan
