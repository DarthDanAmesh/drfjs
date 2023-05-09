let userToken;
var csrftoken = $.cookie(‘csrftoken’);

document.getElementById('login_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let email = document.getElementById('id_email').value;
    let password = document.getElementById('id_password').value;

    fetch('http://127.0.0.1:8000/api/auth-token/', {
        method: 'POST',
        headers: {
            'X-CSRFTOKEN': csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "username": email,
            "password": password,
        })
    }).then( response => {
        return response.json();
    }).then(data => {
        console.log(data);
        userToken = data.token;
        console.log('Logged in. Got the token.');
    }).catch((error) => {
        console.error('Error:', error);
    });
});

function submitNewForm(){

document.getElementById('avatar_form').addEventListener('submit', function(event) {
    event.preventDefault();
    let number = document.getElementById('id_number').value;
    let middle = document.getElementById('id_middle_name').value;
    let two_names = document.getElementById('id_first_two_names').value;
    let contact = document.getElementById('id_contact').value;
    let location = document.getElementById('id_location').value;
    let input = document.getElementById('id_bio');
    let cover = document.getElementById('id_resume');

    let data = new FormData();
    // matching each field in model.py with the id in avatar_form
    data.append('cover', input.files[0]);
    data.append('resume', cover.files[0]);
    data.append('contact', contact);
    data.append('location', location);
    data.append('first_two_names', two_names);
    data.append('middle_name', middle);
    data.append('id_number', number);

    //data.append()

    fetch('http://127.0.0.1:8000/api/user-uploads/', {
        method: 'POST',
        headers: {
            'X-CSRFTOKEN': csrftoken),
            'Authorization': `Token ${userToken}`
        },
        body: data
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data);
    }).catch((error) => {
        console.error('Invalid submission details:', error);
    });

});
}
    /* code block */
    /*  */