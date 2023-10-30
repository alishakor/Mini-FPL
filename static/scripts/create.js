// JavaScript for player selection, budget tracking, and constraints

// Initialize budget and position counters
let budget = 100;
let selectedGoalkeepers = 0;
let selectedDefenders = 0;
let selectedMidfielders = 0;
let selectedStrikers = 0;

// Function to initialize a player card
function initializePlayerCard(playerCard) {
    const selectPlayerBtn = playerCard.querySelector('#select-player');
    const playerPosition = 'Goalkeeper'; // Replace with the actual position for this player
    const playerPrice = 10; // Replace with the actual price for this player

    selectPlayerBtn.addEventListener('click', () => {
        if (canSelectPlayer(playerPosition) && canAffordPlayer(playerPrice)) {
            displayPlayerPool(playerCard);
        }
    });

    // Add additional initialization code for the player card, if needed
}

// Function to check if a player can be selected
function canSelectPlayer(position) {
    switch (position) {
        case 'Goalkeeper':
            return selectedGoalkeepers < 2;
        case 'Defender':
            return selectedDefenders < 5;
        case 'Midfielder':
            return selectedMidfielders < 5;
        case 'Striker':
            return selectedStrikers < 3;
        default:
            return false;
    }
}

// Function to check if a player can be afforded within the budget
function canAffordPlayer(price) {
    return budget - price >= 0;
}

// Function to display the player pool
function displayPlayerPool(playerCard) {
    // Fetch player data from the server using the /get_player_data route
    fetch('/get_player_data')
        .then(response => response.json())
        .then(playerData => {
            // Create a modal or dropdown to display the player pool
            const modal = document.createElement('div');
            modal.classList.add('player-pool-modal'); // Add CSS styles as needed
            modal.innerHTML = `
                <h3>Select a Player</h3>
                <ul id="player-list"></ul>
            `;

            const playerList = modal.querySelector('#player-list');

            // Add event listeners to the player pool items to handle player selection
            playerData.forEach(player => {
                const playerItem = document.createElement('li');
                playerItem.textContent = `${player.name} (${player.position}, $${player.price})`;

                playerItem.addEventListener('click', () => {
                    // Update the player card with the selected player's information
                    updatePlayerInfo(playerCard, player);

                    // Close the player pool modal or hide the dropdown
                    modal.style.display = 'none';
                });

                playerList.appendChild(playerItem);
            });

            // Add the modal to the document body or display the dropdown
            document.body.appendChild(modal);

            // You may need to add additional code to style and display the modal or dropdown
        });
}


// Function to update player info when a player is selected
function updatePlayerInfo(playerCard, selectedPlayer) {
    const playerPosition = selectedPlayer.position;
    const playerPrice = selectedPlayer.price;

    if (canSelectPlayer(playerPosition) && canAffordPlayer(playerPrice)) {
        // Update player info on the specific player card
        const playerName = playerCard.querySelector('#player-name');
        const playerPositionElement = playerCard.querySelector('#player-position');
        const playerPriceElement = playerCard.querySelector('#player-price');

        playerName.textContent = selectedPlayer.name;
        playerPositionElement.textContent = playerPosition;
        playerPriceElement.textContent = playerPrice;

        // Update position counter, budget, and enable "Create Team" button
        updatePositionCounter(playerPosition);
        updateBudget(playerPrice);
    }
}

// Function to update position counter
function updatePositionCounter(position) {
    switch (position) {
        case 'Goalkeeper':
            selectedGoalkeepers++;
            break;
        case 'Defender':
            selectedDefenders++;
            break;
        case 'Midfielder':
            selectedMidfielders++;
            break;
        case 'Striker':
            selectedStrikers++;
            break;
    }

    if (selectedGoalkeepers === 2 && selectedDefenders === 5 && selectedMidfielders === 5 && selectedStrikers === 3) {
        enableCreateTeamButton();
    }
}

// Function to update budget
function updateBudget(price) {
    budget -= price;

    if (budget < 0) {
        // Handle budget constraints as needed
    }
}

// Enable "Create Team" button
function enableCreateTeamButton() {
    const submitButton = document.getElementById('submitBtn');
    submitButton.disabled = false;
}

// Example: Initialize all player cards with the same code
const playerCards = document.querySelectorAll('.player-card');
playerCards.forEach(playerCard => {
    initializePlayerCard(playerCard);
});
