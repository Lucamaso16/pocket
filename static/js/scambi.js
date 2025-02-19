document.addEventListener("DOMContentLoaded", function () {
    const espansioneField = document.getElementById("id_espansione");
    const pokemonField = document.getElementById("id_pokemon");

    espansioneField.addEventListener("change", function () {
        const espansioneId = espansioneField.value;
        if (!espansioneId) {
            pokemonField.innerHTML = '<option value="">Seleziona un Pokémon</option>';
            return;
        }

        fetch(pokemonUrl + "?espansione=" + espansioneId)
            .then(response => response.json())
            .then(data => {
                pokemonField.innerHTML = '<option value="">Seleziona un Pokémon</option>';
                data.pokemon.forEach(pokemon => {
                    let option = document.createElement("option");
                    option.value = pokemon.id;
                    option.textContent = pokemon.nome;
                    pokemonField.appendChild(option);
                });
            });
    });
});
