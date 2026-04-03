async function loadAlerts() {
    checkAuth();

    const alerts = await apiFetch('/alerts/');
    const tbody = document.getElementById('alerts-table');
    tbody.innerHTML = '';

    if (alerts.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="loading">Nenhum alerta encontrado.</td></tr>';
        return;
    }

    alerts.slice().reverse().forEach(alert => {
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

document.addEventListener('DOMContentLoaded', loadAlerts);
