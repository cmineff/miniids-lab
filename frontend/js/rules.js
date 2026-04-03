async function loadRules() {
    checkAuth();

    const rules = await apiFetch('/rules/');
    const tbody = document.getElementById('rules-table');
    tbody.innerHTML = '';

    if (rules.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="loading">Nenhuma regra encontrada.</td></tr>';
        return;
    }

    rules.forEach(rule => {
        tbody.innerHTML += `
            <tr>
                <td>${rule.id}</td>
                <td>${rule.name}</td>
                <td>${rule.event_type}</td>
                <td><span class="badge badge-${rule.severity}">${rule.severity}</span></td>
                <td>${rule.threshold} em ${rule.window_seconds}s</td>
                <td>
                    <button
                        class="btn-toggle ${rule.is_active ? 'active' : 'inactive'}"
                        onclick="toggleRule(${rule.id})">
                        ${rule.is_active ? 'Ativa' : 'Inativa'}
                    </button>
                </td>
            </tr>
        `;
    });
}

async function toggleRule(id) {
    await apiFetch(`/rules/${id}/toggle`, { method: 'PATCH' });
    loadRules();
}

document.addEventListener('DOMContentLoaded', loadRules);
