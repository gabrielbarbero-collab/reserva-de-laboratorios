document.addEventListener('DOMContentLoaded', () => {
    const inputData = document.getElementById('data');
    if (inputData) {
        const hoje = new Date().toISOString().split('T')[0];
        inputData.min = hoje;
    }

    carregarSalas();
    carregarUtilizadores();
    carregarReservas();

    const form = document.getElementById('form-reserva');
    form.addEventListener('submit', efetuarReserva);
});

async function carregarReservas() {
    const listaReservas = document.getElementById('lista-reservas');

    try {
        const resposta = await fetch('/api/reservas');
        if (!resposta.ok) throw new Error('Falha ao obter reservas');

        const reservas = await resposta.json();

        if (reservas.length === 0) {
            listaReservas.innerHTML = '<p class="loading-text">Nenhuma reserva registada até ao momento.</p>';
            return;
        }

        listaReservas.innerHTML = reservas.map(r => `
            <div class="sala-item">
                <div>
                    <strong><i class="fa-solid fa-bookmark" style="color: #2563eb;"></i> ${r.nome_sala}</strong> 
                    <small style="color: #64748b;">(${r.nome_utilizador})</small><br>
                    <small style="color: #475569;"><i class="fa-regular fa-calendar"></i> ${r.data} | <i class="fa-regular fa-clock"></i> ${r.hora_inicio} - ${r.hora_fim}</small>
                </div>
                <span class="sala-tag" style="background: #dcfce7; color: #15803d;"><i class="fa-solid fa-circle-check"></i> ${r.estado}</span>
            </div>
        `).join('');

    } catch (erro) {
        console.error('Erro:', erro);
        listaReservas.innerHTML = '<p class="loading-text" style="color: #ef4444;">Erro ao carregar reservas em tempo real.</p>';
    }
}

async function carregarSalas() {
    const listaDiv = document.getElementById('lista-salas');
    const selectSala = document.getElementById('sala');

    try {
        const resposta = await fetch('/api/salas');
        if (!resposta.ok) throw new Error('Falha ao obter salas');
        
        const salas = await resposta.json();
        document.getElementById('total-salas').innerText = salas.length;

        if (salas.length === 0) {
            listaDiv.innerHTML = '<p class="loading-text">Nenhuma sala registada no sistema.</p>';
            selectSala.innerHTML = '<option value="">Sem salas disponíveis</option>';
            return;
        }

        listaDiv.innerHTML = salas.map(sala => `
            <div class="sala-item">
                <div>
                    <strong><i class="fa-solid fa-door-closed"></i> ${sala.nome}</strong><br>
                    <small style="color: #64748b;">Recursos: ${sala.recursos}</small>
                </div>
                <span class="sala-tag"><i class="fa-solid fa-user-group"></i> Cap: ${sala.capacidade}</span>
            </div>
        `).join('');

        selectSala.innerHTML = '<option value="">Selecione uma sala...</option>' + 
            salas.map(s => `<option value="${s.id_sala}">${s.nome}</option>`).join('');

    } catch (erro) {
        console.error('Erro:', erro);
        listaDiv.innerHTML = '<p class="loading-text" style="color: #ef4444;">Erro ao carregar lista de salas.</p>';
    }
}

async function carregarUtilizadores() {
    const selectUtilizador = document.getElementById('utilizador');

    try {
        const resposta = await fetch('/api/utilizadores');
        if (!resposta.ok) throw new Error('Falha ao obter utilizadores');

        const utilizadores = await resposta.json();
        document.getElementById('total-utilizadores').innerText = utilizadores.length;

        selectUtilizador.innerHTML = '<option value="">Selecione o utilizador...</option>' + 
            utilizadores.map(u => `<option value="${u.id_utilizador}">${u.nome}</option>`).join('');
    } catch (erro) {
        console.error('Erro:', erro);
        selectUtilizador.innerHTML = '<option value="">Erro ao carregar utilizadores</option>';
    }
}

async function efetuarReserva(e) {
    e.preventDefault();
    const btnSubmit = document.getElementById('btn-submit');
    const textoOriginal = btnSubmit.innerHTML;

    const dadosReserva = {
        id_utilizador: document.getElementById('utilizador').value,
        id_sala: document.getElementById('sala').value,
        data: document.getElementById('data').value,
        hora_inicio: document.getElementById('hora_inicio').value,
        hora_fim: document.getElementById('hora_fim').value
    };

    btnSubmit.disabled = true;
    btnSubmit.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> A processar...';

    try {
        const resposta = await fetch('/api/reservas', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dadosReserva)
        });

        const resultado = await resposta.json();

        alert(resultado.mensagem);

        if (resposta.ok) {
            document.getElementById('form-reserva').reset();
            carregarReservas();
        }
    } catch (erro) {
        console.error('Erro de rede:', erro);
        alert('Ocorreu um erro de comunicação com o servidor.');
    } finally {
        btnSubmit.disabled = false;
        btnSubmit.innerHTML = textoOriginal;
    }
}