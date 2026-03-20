// Calculator UI JavaScript

const expressionInput = document.getElementById('expression');
const calculateBtn = document.getElementById('calculateBtn');
const clearBtn = document.getElementById('clearBtn');
const resultContainer = document.getElementById('resultContainer');
const resultValue = document.getElementById('resultValue');
const errorMessage = document.getElementById('errorMessage');

// Handle calculate button click
calculateBtn.addEventListener('click', calculateExpression);

// Handle clear button click
clearBtn.addEventListener('click', clearForm);

// Allow Enter key to calculate
expressionInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        calculateExpression();
    }
});

async function calculateExpression() {
    const expression = expressionInput.value.trim();

    if (!expression) {
        showError('Please enter an expression');
        return;
    }

    try {
        // Show loading state
        calculateBtn.disabled = true;
        calculateBtn.textContent = 'Calculating...';

        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ expression: expression }),
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || 'Failed to calculate expression');
            return;
        }

        showResult(data.result);
    } catch (error) {
        showError(`Error: ${error.message}`);
    } finally {
        calculateBtn.disabled = false;
        calculateBtn.textContent = 'Calculate';
    }
}

function showResult(result) {
    // Format the result to avoid floating-point precision issues
    const formattedResult =
        Math.abs(result) < 1e-10
            ? '0'
            : parseFloat(result.toFixed(10)).toString();

    resultValue.textContent = formattedResult;
    resultContainer.style.display = 'block';
    errorMessage.classList.remove('show');
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.add('show');
    resultContainer.style.display = 'block';
}

function clearForm() {
    expressionInput.value = '';
    resultContainer.style.display = 'none';
    errorMessage.classList.remove('show');
    expressionInput.focus();
}
