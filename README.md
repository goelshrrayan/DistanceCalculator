# DistanceCalculator
DistanceCalculator 91Social

Running the project locally:

1. Create a virtual environment using
    python -m venv myvenv

2. Clone the project from github
    https://github.com/goelshrrayan/DistanceCalculator

3. Activate the virtual environment using
    source myvenv/bin/activate

4. Navigate inside the project folder and install requirements.txt using command line     
    pip install -r requirements.txt

5. Run makemigration:
    python manage.py maemigrations

6. Run migrate:
    python manage.py migrate

7. Run project using:
    python manage.py runserver

Flow of the app:

1. There are two pages: home page and a page where user can enter current location and query shops nearby

2. By default user will be routed to home page.

    a) You can create a new shop entry here by clicking add button
    b) You can edit a previous entry here by clicking edit button corresponding to a shop
    c) you can route to page where you can query nearby shops by clicking "shop list" button

3. After clicking "shop list" a new tab will be opened.

    a) You can add current location and distance and click submit.
    b) In the text area below a json will be returned with all the shops nearby within the distance given.

Input Format:
1. Shop Name: String
2. Shop Owner Name: String
3. Latitude: In decimals(-90 to 90)
4. Longitude: In decimals(-180 to 180)    
