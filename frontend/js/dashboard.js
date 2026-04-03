async function loadDashboard() {
    checkAuth();

    const events = await apiFetch('/events/');
    const alerts = await apiFetch('/alerts/');
    const rules = await apiFetch('/rules/');

    document.getElementById('total-events').textContent = events.length;
    document.getElementById('total-alerts').textContent = alerts.length;
    document.getElementById('total-rules').textContent = rules.length;

    const openAlerts = alerts.filter(a => a.status === 'open').length;
    document.getElementById('open-alerts').textContent = openAlerts;

    const recentAlerts = alerts.slice(-5).reverse();
    const tbody = document.getElementById('recent-alerts');
    tbody.innerHTML = '';

    recentAlerts.forEach(alert => {
        tbody.innerHTML += `
            <tr>
                <td>${alert.title}</td>
                <td>${alert.source_ip || '-'}</td>
                <td><span class="badge badge-${alert.severity}">${alert.severity}</span></td>
                <td><span class="badge badge-${alert.status}">${alert.status}</span></td>
                <td>${new Date(alert.created_at).toLocaleString('pt-BR')}</td>
            </tr>
        `;
    });
}

document.addEventListener('DOMContentLoaded', loadDashboard);
