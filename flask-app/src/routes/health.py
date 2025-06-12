from flask import Blueprint, jsonify
import time
import psutil
import os
from datetime import datetime

health_bp = Blueprint('health', __name__)

start_time = time.time()

@health_bp.route('/health', methods=['GET'])
def health_check():
    """Endpoint de health check para verificação de saúde da aplicação"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'uptime_seconds': int(time.time() - start_time),
        'version': '1.0.0'
    }), 200

@health_bp.route('/metrics', methods=['GET'])
def metrics():
    """Endpoint de métricas básicas para monitoramento"""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return jsonify({
            'timestamp': datetime.utcnow().isoformat(),
            'uptime_seconds': int(time.time() - start_time),
            'system': {
                'cpu_percent': cpu_percent,
                'memory_percent': memory.percent,
                'memory_used_mb': memory.used // (1024 * 1024),
                'memory_total_mb': memory.total // (1024 * 1024),
                'disk_percent': (disk.used / disk.total) * 100,
                'disk_used_gb': disk.used // (1024 * 1024 * 1024),
                'disk_total_gb': disk.total // (1024 * 1024 * 1024)
            },
            'application': {
                'version': '1.0.0',
                'environment': os.getenv('ENVIRONMENT', 'development'),
                'process_id': os.getpid()
            }
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Failed to collect metrics',
            'message': str(e)
        }), 500

@health_bp.route('/ready', methods=['GET'])
def readiness_check():
    """Endpoint de readiness para Kubernetes/ECS"""
    return jsonify({
        'status': 'ready',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

