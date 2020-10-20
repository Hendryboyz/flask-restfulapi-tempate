FROM python:3.8-alpine as build

WORKDIR /src

COPY ./ /src

RUN pip install -e . \
  && python setup.py bdist_wheel \
  && ls -al /src

FROM python:3.8-alpine as deployment
ENV FLASK_APP=flaskr
WORKDIR /app

COPY --from=build /src/dist/* /app

RUN pip install flaskr-1.0.0-py3-none-any.whl \
  && pip install waitress

EXPOSE 8080

ENTRYPOINT waitress-serve --call 'flaskr:create_app'