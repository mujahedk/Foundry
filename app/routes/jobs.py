from typing import List
from fastapi import APIRouter, HTTPException

from app.db.connection import get_db_connection
from app.schema import JobCreate, JobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

# router changes root to this


@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate):
    # POST jobs: accept payload, insert row into jobs, set to pending
    conn = get_db_connection()
    cur = conn.cursor()
    # executes SQL command
    cur.execute(
        """
        INSERT INTO jobs (status, payload)
        VALUES (%s, %s)
        RETURNING id, status, payload, result, created_at;
        """,
        ("pending", job.payload)
    )
    # creates row, fetches all values
    row = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    return {
        "id": row[0],
        "status": row[1],
        "payload": row[2],
        "result": row[3],
        "created_at": row[4],
    }


@router.get("/", response_model=List[JobResponse])
def get_jobs():
    # GET jobs: query table, return all jobs
    conn = get_db_connection()
    cur = conn.cursor()
    # executes SQL command
    cur.execute(
        """
        SELECT id, status, payload, result, created_at
        FROM jobs
        ORDER BY id;
        """
    )
    # creates row, fetches all values
    rows = cur.fetchall()

    cur.close()
    conn.close()
    jobs = []
    for row in rows:
        jobs.append(
            {
                "id": row[0],
                "status": row[1],
                "payload": row[2],
                "result": row[3],
                "created_at": row[4],
            }
        )
    return jobs


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int):
    # GET jobs/{id}: query table, return specific ID job
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, status, payload, result, created_at
        FROM jobs
        WHERE id = %s;
        """,
        (job_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    # if none, return error message
    if row is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {
        "id": row[0],
        "status": row[1],
        "payload": row[2],
        "result": row[3],
        "created_at": row[4],
    }
