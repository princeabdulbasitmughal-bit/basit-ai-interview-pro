# Multi-stage production container for Basit AI Interview Pro
FROM node:20-alpine AS base

# Install Python & curl for healthcheck and swarm runner
RUN apk add --no-cache python3 curl bash

WORKDIR /app

# Copy package descriptors first for optimal layer caching
COPY package.json ./

# Copy application source files
COPY server.js ./
COPY Modelfile ./
COPY Modelfile.32b ./
COPY basit_loop_orchestrator.py ./
COPY ecosystem.config.js ./
COPY public ./public
COPY modules ./modules
COPY tests ./tests
COPY data ./data
COPY reports ./reports

# Ensure directories exist and set appropriate permissions
RUN mkdir -p /app/data /app/reports /app/logs && \
    chown -R node:node /app

# Switch to non-root production user for OWASP container hardening
USER node

# Production environment variables
ENV NODE_ENV=production \
    PORT=8090 \
    PYTHONUNBUFFERED=1

EXPOSE 8090

# Native health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8090/api/health || exit 1

CMD ["node", "server.js"]
