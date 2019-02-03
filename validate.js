function validate(){
                let email_address = document.getElementById('email_address').value;
                let course_name = document.getElementById('course_id').value;
                if(email_address.length > 100){
                    alert('email address is too long!');
                    return false;
                }
                if(course_name.length > 10){
                    alert('invalid course ID');
                    return false;
                }
                return true;
}