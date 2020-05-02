#Base Image
FROM Python:3.7.2-slim

ADD csv_to_db.py /

# install
RUN pip install pymongo, pandas

# run server
CMD [ "python", "./csv_to_db.py" ]