async function loadEvents() {
    checkAuth();

    const events = await apiFetch('/events/');
    const tbody = document.getElementById('events-table');
    tbody.innerHTML = '';

    if (events.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="loading">Nenhum evento encontrado.</td></tr>';
        return;
    }

    events.slice().reverse().forEach(event => {
        tbody.innerHTML += `
            <tr>
                <td>${event.id}</td>
                <td>${event.source_ip}</td>
                <td>${event.destination_ip || '-'}</td>
                <td>${event.event_type}</td>
                <td>${event.message}</td>
                <td>${new Date(event.created_at).toLocaleString('pt-BR')}</td>
            </tr>
        `;
    });
}

document.addEventListener('DOMContentLoaded', loadEvents);
