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

8. Run test cases:
    python manage.py test    

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

Function used to calculate distance:

    a) In order to calculate distance between two latitude and longitude pairs we have used
        Haversine formula.
    b) Haversine formula states:
        a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
        c = 2 * atan2( √a, √(1−a) )
        d = R * c     

        Where:

            1. lat1 and lon1 are the latitude and longitude of the first point in radians
            2. lat2 and lon2 are the latitude and longitude of the second point in radians
            3. Δlat and Δlon are the differences between the latitudes and longitudes of the two points in radians
            4. R is the radius of the Earth in the desired units (e.g. miles or kilometers)
            5. sin is the sine function
            6. cos is the cosine function
            7. atan2 is the two-argument arctangent function (sometimes written as atan(y,x))
