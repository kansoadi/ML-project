@echo off
cd backend
uvicorn backend:app --reload
pause