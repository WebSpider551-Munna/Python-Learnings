// Get references to the elements
const board = document.getElementById('board');
const cells = document.querySelectorAll('.cell');
const message = document.getElementById('message');
const resetBtn = document.getElementById('reset');

// Game variables
let currentPlayer = 'X';
let gameBoard = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

// Function to handle a cell click
function cellClick(index) {
    if (gameBoard[index] === '' && gameActive) {
        gameBoard[index] = currentPlayer;
        cells[index].textContent = currentPlayer;
        cells[index].classList.add(currentPlayer === 'X' ? 'x-color' : 'o-color'); // Add color class
        checkWinner();
        switchPlayer();
    }
}

// Function to switch players
function switchPlayer() {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    message.textContent = `Player ${currentPlayer}'s turn`;
}

// Function to check for a winner
function checkWinner() {
    const winningCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]             // Diagonals
    ];

    for (let combo of winningCombos) {
        const [a, b, c] = combo;
        if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
            const winner = gameBoard[a];
            message.textContent = `Player ${winner} wins!`;
            gameActive = false;
            celebrate();
            return true;
        }
    }

    // Check for a tie
    if (!gameBoard.includes('')) {
        message.textContent = "It's a tie!";
        gameActive = false;
        return true;
    }
    return false;
}

function celebrate() {
    const particles = 200;
    for (let i = 0; i < particles; i++) {
        createParticle();
    }
}

function createParticle() {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    document.body.appendChild(particle);

    const size = Math.random() * 10 + 5;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;
    particle.style.background = `hsl(${Math.random() * 360}, 70%, 50%)`;
    particle.style.setProperty('--random-x', Math.random() * 2 - 1);
    particle.style.setProperty('--random-y', Math.random() * 2 - 1);
    particle.style.left = `${Math.random() * 100}vw`;
    particle.style.top = `${Math.random() * 100}vh`;

    const animationDuration = Math.random() * 2 + 1;
    particle.style.animation = `particle ${animationDuration}s linear`;

    particle.addEventListener('animationend', () => {
        particle.remove();
    });
}

// Function to reset the game
function resetGame() {
    currentPlayer = 'X';
    gameBoard = ['', '', '', '', '', '', '', '', ''];
    gameActive = true;
    message.textContent = `Player ${currentPlayer}'s turn`;
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x-color', 'o-color'); // Remove color classes
    });
}

// Add event listeners to the cells
cells.forEach((cell, index) => {
    cell.addEventListener('click', () => cellClick(index));
});

// Add event listener to the reset button
resetBtn.addEventListener('click', resetGame);

// Initial message
message.textContent = `Player ${currentPlayer}'s turn`;
