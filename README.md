# vehicle data kata

### running the app

You can run the app using docker compose, in the app dir just run the command:

```
docker-compose up
```

to change the port of the app, please edit it in docker-compose.yml then run again.

### using the app

you can send a post request (that includes the file) to the app endpoint:

`http://localhost/vehicle/csv`

to process the data, for an example using cURL:

```
curl -X POST --data-binary @vehicles.csv http://localhost/vehicle/csv
```

### running tests

You can run the tests using another docker compose config file, just run:

```
docker-compose -f ./docker-compose.test.yml up
```
