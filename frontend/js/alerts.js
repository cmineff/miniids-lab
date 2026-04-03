async function loadAlerts(severity = '', status = '') {
    checkAuth();

    let url = '/alerts/?limit=100';
    if (severity) url += `&severity=${severity}`;
    if (status) url += `&status=${status}`;

    const alerts = await apiFetch(url);
    const tbody = document.getElementById('alerts-table');
    tbody.innerHTML = '';

    if (alerts.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="loading">Nenhum alerta encontrado.</td></tr>';
        return;
    }

    alerts.forEach(alert => {
        tbody.innerHTML += `
            <tr>
                <td>${alert.id}</td>
                <td>${alert.title}</td>
                <td>${alert.source_ip || '-'}</td>
                <td><span class="badge badge-${alert.severity}">${alert.severity}</span></td>
                <td><span class="badge badge-${alert.status}">${alert.status}</span></td>
                <td>${new Date(alert.created_at).toLocaleString('pt-BR')}</td>
            </tr>
        `;
    });
}

async function updateStatus(alertId, status) {
    await apiFetch(`/alerts/${alertId}/status?status=${status}`, { method: 'PATCH' });
    loadAlerts();
}

document.addEventListener('DOMContentLoaded', () => {
    loadAlerts();

    document.getElementById('filter-severity').addEventListener('change', () => {
        const severity = document.getElementById('filter-severity').value;
        const status = document.getElementById('filter-status').value;
        loadAlerts(severity, status);
    });

    document.getElementById('filter-status').addEventListener('change', () => {
        const severity = document.getElementById('filter-severity').value;
        const status = document.getElementById('filter-status').value;
        loadAlerts(severity, status);
    });
});
