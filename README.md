# Traffic Light
Employee and Department

## App is live on Heroku server

1. To test app go below site:

    https://traffic-light-a.herokuapp.com

2. To go to admin panel:

    https://traffic-light-a.herokuapp.com/admin

        login:admin
        password:123


## Build and run the app on local machine with Docker

1. Install Docker

2. Download this repository
    ```
    git clone https://github.com/abdullasalimov/traffic_light.git
    ```
3. Go to directory
    ```
    cd traffic_light
    ```

6. On the command line, within this directory, do this to build the image and start the container:

        docker-compose up -d --buil

7. Migrate database with below code:

        docker-compose exec web python manage.py migrate --noinp

7. If that's successful you can then go to the localhost on you browser to test it:

        http://localhost:8000

8. To add data on admin panel create superuser with below code:

        docker-compose exec web python manage.py createsuperuser

9. Link to admin page:

        http://localhost:8000/admin

