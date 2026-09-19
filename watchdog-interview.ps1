# Basit AI Interview System - 24/7 Resilience Watchdog Guardian v3.0
# Port: 8090 | Zero-Hang Autorecovery with Active Health Heartbeat

$workDir = "E:\basit-ai-interview"
$port = 8090
$healthUrl = "http://127.0.0.1:$port/api/health"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  BASIT AI INTERVIEW SYSTEM - 24/7 WATCHDOG GUARDIAN v3.0" -ForegroundColor Green
Write-Host "  Port: $port | Target Dir: $workDir" -ForegroundColor Yellow
Write-Host "  Active Heartbeat: $healthUrl" -ForegroundColor Magenta
Write-Host "==========================================================" -ForegroundColor Cyan

$consecutiveFailures = 0

while ($true) {
    try {
        # Check if port 8090 is occupied by a healthy process
        $isHealthy = $false
        try {
            $resp = Invoke-RestMethod -Uri $healthUrl -Method Get -TimeoutSec 6 -ErrorAction SilentlyContinue
            if ($resp.status -eq "online") {
                $isHealthy = $true
            }
        } catch {}

        if ($isHealthy) {
            $consecutiveFailures = 0
            Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Heartbeat OK: Server online on port $port" -ForegroundColor DarkGreen
        } else {
            $consecutiveFailures++
            Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Server probe missed ($consecutiveFailures/3)..." -ForegroundColor Yellow

            if ($consecutiveFailures -ge 3) {
                Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] 3 consecutive failures. Cleaning port $port and restarting..." -ForegroundColor Red
                $conns = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
                if ($conns) {
                    foreach ($c in $conns) {
                        if ($c.OwningProcess -gt 0) {
                            Stop-Process -Id $c.OwningProcess -Force -ErrorAction SilentlyContinue
                        }
                    }
                }

                Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Starting Node.js Server on port $port..." -ForegroundColor Green
                $proc = Start-Process "node" -ArgumentList "server.js" -WorkingDirectory $workDir -PassThru -NoNewWindow
                Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Server started with PID $($proc.Id)" -ForegroundColor Cyan
                $consecutiveFailures = 0
                Start-Sleep -Seconds 6
            }
        }
    } catch {
        Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Watchdog exception: $_" -ForegroundColor Red
    }
    Start-Sleep -Seconds 10
}
