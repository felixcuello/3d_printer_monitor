all: database_directory build

build: database_directory
	docker compose build

up:
	docker compose up

database_directory:
	mkdir -p 3d_fdm_prediction_db

clean:
	echo "To drop the database use 'make drop'"

drop: clean
	rm -rf 3d_fdm_prediction_db
