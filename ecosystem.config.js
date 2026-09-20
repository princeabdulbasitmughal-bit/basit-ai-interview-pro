/**
 * ================================================================================
 * 👑 BASIT AI INTERVIEW PRO — PM2 PRODUCTION ECOSYSTEM CONFIG
 * ================================================================================
 * Enterprise-grade 24/7 process manager for AI Interview Pro & Autonomous Looper.
 *
 * Install PM2:  npm install -g pm2
 * Start all:    pm2 start ecosystem.config.js
 * Stop all:     pm2 stop all
 * Restart all:  pm2 restart all
 * Status:       pm2 status
 * Live logs:    pm2 logs
 * ================================================================================
 */

module.exports = {
  apps: [
    // ── 1. CORE INTERVIEW INTELLIGENCE SERVER ────────────────────────────────
    {
      name: "basit-interview-server",
      script: "server.js",
      cwd: __dirname,
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: "1G",
      restart_delay: 2000,
      max_restarts: 15,
      min_uptime: "10s",
      env: {
        NODE_ENV: "production",
        PORT: 8090,
      },
      error_file: "logs/pm2-interview-error.log",
      out_file: "logs/pm2-interview-out.log",
      log_date_format: "YYYY-MM-DD HH:mm:ss",
    },

    // ── 2. CONTINUOUS 10-MINUTE LOOPING ORCHESTRATOR ────────────────────────
    {
      name: "basit-loop-orchestrator",
      script: "python",
      args: ["-u", "basit_loop_orchestrator.py"],
      cwd: __dirname,
      interpreter: "none",
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: "500M",
      restart_delay: 5000,
      max_restarts: 10,
      min_uptime: "15s",
      env: {
        PYTHONIOENCODING: "utf-8",
        PYTHONUNBUFFERED: "1",
      },
      error_file: "logs/pm2-orchestrator-error.log",
      out_file: "logs/pm2-orchestrator-out.log",
      log_date_format: "YYYY-MM-DD HH:mm:ss",
    }
  ]
};
