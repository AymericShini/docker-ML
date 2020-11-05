FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8080
CMD python3 anime.py && streamlit run mainAnime.py
