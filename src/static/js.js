document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('.form-required');

    function validateInput(input, minLength, noNumbers) {
        const value = input.value;
        if (value.length < minLength || (noNumbers && /\d/.test(value))) {
            input.classList.add('error');
            input.classList.remove('valid');
        } else {
            input.classList.remove('error');
            input.classList.add('valid');
        }
    }

    inputs.forEach(function(input) {
        input.addEventListener('input', function() {
            validateInput(input, 3, true);
        });
    });

    form.addEventListener('submit', function(event) {
        inputs.forEach(function(input) {
            validateInput(input, 3, true);
        });

        if (form.querySelector('.error')) {
            event.preventDefault();
            alert('Por favor, corrija os erros no formulário antes de enviar.');
        }
    });
});
