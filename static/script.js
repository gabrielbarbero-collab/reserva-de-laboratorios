document.addEventListener('DOMContentLoaded', () => {
    carregarSalas();
    carregarUtilizadores();

    const form = document.getElementById('form-reserva');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const dadosReserva = {
            id_utilizador: document.getElementById('utilizador').value,
            id_sala: document.getElementById('sala').value,
            data: document.getElementById('data').value,
            hora_inicio: document.getElementById('hora_inicio').value,
            hora_fim: document.getElementById('hora_fim').value
        };

        try {
            const resposta = await fetch('/api/reservas', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dadosReserva)
            });

            const resultado = await resposta.json();
            alert(resultado.mensagem);
            if (resposta.ok) form.reset();
        } catch (erro) {
            console.error('Erro ao efetuar reserva:', erro);
            alert('Erro ao ligar ao servidor.');
        }
    });
});

async function carregarSalas() {
    try {
        const resposta = await fetch('/api/salas');
        const salas = await resposta.json();
        const listaDiv = document.getElementById('lista-salas');
        const selectSala = document.getElementById('sala');

        document.getElementById('total-salas').innerText = salas.length;

        if (salas.length === 0) {
            listaDiv.innerHTML = '<p>Nenhuma sala registada.</p>';
            selectSala.innerHTML = '<option value="">Sem salas disponíveis</option>';
            return;
        }

        // Renderizar lista na página
        listaDiv.innerHTML = salas.map(sala => `
            <div class="sala-item">
                <div>
                    <strong><i class="fa-solid fa-door-closed"></i> ${sala.nome}</strong><br>
                    <small style="color: #64748b;">Recursos: ${sala.recursos}</small>
                </div>
                <span class="sala-tag"><i class="fa-solid fa-user-group"></i> Lotação: ${sala.capacidade}</span>
            </div>
        `).join('');

        // Preencher Dropdown do formulário
        selectSala.innerHTML = '<option value="">Selecione uma sala...</option>' + 
            salas.map(s => `<option value="${s.id_sala}">${s.nome}</option>`).join('');

    } catch (erro) {
        console.error('Erro ao carregar salas:', erro);
        document.getElementById('lista-salas').innerHTML = '<p>Erro ao carregar lista de salas.</p>';
    }
}

async function carregarUtilizadores() {
    try {
        const resposta = await fetch('/api/utilizadores');
        const utilizadores = await resposta.json();
        const selectUtilizador = document.getElementById('utilizador');

        document.getElementById('total-utilizadores').innerText = utilizadores.length;

        selectUtilizador.innerHTML = '<option value="">Selecione o utilizador...</option>' + 
            utilizadores.map(u => `<option value="${u.id_utilizador}">${u.nome}</option>`).join('');
    } catch (erro) {
        console.error('Erro ao carregar utilizadores:', erro);
    }
}