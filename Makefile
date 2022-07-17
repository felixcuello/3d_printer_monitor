all: database_directory build up

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

macos_prerequisites:
	brew install opencv@2

capture_osx:
	cd ./capture && pip3 install -r requirements.txt
	cd ./capture && python3 capture.py ${TIME} ${FRAME_NAME}
