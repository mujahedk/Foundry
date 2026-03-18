A backend app where users submit jobs, jobs get processed by a worker, the API is protected by API keys and rate limiting, and completed jobs/documents can be searched. (7 Day Project)

Workflow: Users submit jobs → jobs get processed → results stored → dashboard shows system state.

- Flow
  ```jsx
  User submits job
  ↓
  API receives request
  ↓
  Job stored in database
  ↓
  Worker finds job
  ↓
  Worker processes job
  ↓
  Worker saves result
  ↓
  Dashboard displays result
  ```

## 📝 Blueprint

### Day 1: Project Setup

Goal: the server runs and the database connects.

TODOs:

- [x] Setup project structure and environment
- [x] Start FastAPI server
- [x] Connect application to Postgres
- [x] Create **jobs table** (id, status, payload, result)

What you should understand by end of day:

> how a request reaches your server and how your server talks to a database.

### Day 2: Job API

Goal: the system can create and view jobs.

TODOs:

- [ ] Build **create job endpoint**
- [ ] Build **list jobs endpoint**
- [ ] Build **get single job endpoint**
- [ ] Test API with curl/Postman

What you should understand:

> how APIs store and retrieve database data.

### Day 3: Worker System (Afterburner skills)

Goal: jobs actually get processed.

TODOs:

- [ ] Build worker loop that polls database
- [ ] Implement **job claiming**
- [ ] Process job and update status
- [ ] Store job result

What you should understand:

> how background workers process queued tasks.

### Day 4: Job Lifecycle + Retries

Goal: system becomes reliable.

TODOs:

- [ ] Add job states (pending, running, done, failed)
- [ ] Implement retry counter
- [ ] Retry failed jobs automatically
- [ ] Log job execution events

What you should understand:

> how real systems recover from failure.

### Day 5: API Keys + Rate Limiting (Throttle skills)

Goal: protect the API.

TODOs:

- [ ] Create API key authentication
- [ ] Add request middleware
- [ ] Implement Redis rate limiting
- [ ] Return proper rate-limit headers

What you should understand:

> how production APIs prevent abuse.

### Day 6: Search + Dashboard

Goal: visual demo + searchable data.

TODOs:

- [ ] Implement search over job results
- [ ] Create simple dashboard page
- [ ] Show job statuses visually
- [ ] Display system metrics (jobs processed)

What you should understand:

> how data becomes visible to users.

### Day 7: Polish + Demo

Goal: make Foundry explainable.

TODOs:

- [ ] Add job submission form to dashboard
- [ ] Clean up UI and layout
- [ ] Write README explaining architecture
- [ ] Record demo or screenshots

What you should understand:

> how to explain a backend system clearly.
