const API_URL = 'http://127.0.0.1:8000';

function getToken() {
    return localStorage.getItem('token');
}

function setToken(token) {
    localStorage.setItem('token', token);
}

function removeToken() {
    localStorage.removeItem('token');
}

async function apiFetch(endpoint, options = {}) {
    const token = getToken();
    const headers = {
        'Content-Type': 'application/json',
        ...(token && { 'Authorization': `Bearer ${token}` })
    };

    const response = await fetch(`${API_URL}${endpoint}`, {
        ...options,
        headers
    });

    if (response.status === 401) {
        removeToken();
        window.location.href = 'login.html';
        return;
    }

    return response.json();
}
