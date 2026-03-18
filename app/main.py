from fastapi import FastAPI

from app.db.connection import get_db_connection


app = FastAPI(title="Foundry API")


@app.get("/")
def root():
    return {"message": "Foundry API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-check")
def db_check():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT 1;")
    result = cur.fetchone()

    cur.close()
    conn.close()

    return {"database_ok": result[0]}
