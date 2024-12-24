document.getElementById('id_username').placeholder = "Username";
document.getElementById('id_password').placeholder = "Password";

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const password = document.getElementById('id_password').value;
        console.log('Entered Password:', password);
        // You can perform any actions with the password value here
        // event.preventDefault(); // Prevent form submission for testing
    });
});
