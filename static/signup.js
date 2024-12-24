
document.addEventListener('DOMContentLoaded', function() {
    
    const csrfToken = "{{ csrf_token }}";
    
    document.getElementById('id_username').placeholder = "Username";
    document.getElementById('id_password1').placeholder = "Password";
    document.getElementById('id_password2').placeholder = "Confirm password";
    document.getElementById('id_first_name').placeholder = "First name";
    document.getElementById('id_mobile').placeholder = "Mobile number";

})