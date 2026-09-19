@echo off
chcp 65001 >nul
title 👑 BASIT AI INTERVIEW PRO — Sovereign Interview OS
color 0b
cls

echo ===============================================================================
echo 👑 BASIT AI INTERVIEW PRO — SOVEREIGN AI INTERVIEW SYSTEM
echo ===============================================================================
echo [INFO] Initializing High-Performance Node.js Engine...
echo [INFO] Port: 8090
echo [INFO] AI Models: Groq Llama 3.3 / Gemini 2.5 / OpenAI / Dynamic Fallback
echo ===============================================================================

cd /d "e:\basit-ai-interview"

:: Open browser after 1 second
start "" http://localhost:8090

:: Start server
node server.js

pause
