from flask import Blueprint, jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Gauge
import time
import psutil
import os
from datetime import datetime

health_bp = Blueprint('health', __name__)

start_time = time.time()

# Definindo métricas
cpu_usage = Gauge('system_cpu_percent', 'Uso de CPU (%)')
mem_usage = Gauge('system_memory_percent', 'Uso de memória (%)')
uptime = Gauge('system_uptime_seconds', 'Uptime da aplicação (segundos)')

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'uptime_seconds': int(time.time() - start_time),
        'version': '1.0.0'
    }), 200

@health_bp.route('/metrics', methods=['GET'])
def metrics():
    """Endpoint de métricas compatível com Prometheus"""
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        up = int(time.time() - start_time)

        # Atualiza métricas Prometheus
        cpu_usage.set(cpu)
        mem_usage.set(memory.percent)
        uptime.set(up)

        # Retorna no formato Prometheus
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
    except Exception as e:
        return Response(f"# erro: {str(e)}", status=500, mimetype="text/plain")

@health_bp.route('/ready', methods=['GET'])
def readiness_check():
    return jsonify({
        'status': 'ready',
        'timestamp': datetime.utcnow().isoformat()
    }), 200
