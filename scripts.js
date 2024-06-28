<script type="text/javascript">
    function showToast(message, type) {
        Toastify({
            text: message,
            duration: 3000, // duration in ms
            close: true, // show close button
            gravity: "top", // position: top or bottom
            position: "right", // position: left, center or right
            backgroundColor: type === 'success' ? "linear-gradient(to right, #00b09b, #96c93d)" : "linear-gradient(to right, #ff5f6d, #ffc371)",
            stopOnFocus: true, // prevent dismissing on hover
        }).showToast();
    }

    function showAlert() {
        var firstname = document.getElementById('firstname').value;
        var lastname = document.getElementById('lastname').value;
        var email = document.getElementById('email').value;

        if (!firstname || !lastname || !email) {
            showToast('Please fill out the required fields', 'error');
        } else {
            showToast('Registration Successful', 'success');
        }
    }

    // Optional: Add event listener to your form submit button
    document.getElementById('submit').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent form submission
        showAlert();
    });
</script>
