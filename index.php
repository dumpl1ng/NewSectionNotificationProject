<!DOCTYPE html>
<html>
    <head>
        <title>Sections Finder</title>
        <link rel="stylesheet" href="index.css" >
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    </head>
    
    <body>
        <div id=background ></div>
        
        <div id=input_field >
            <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>" onsubmit="return validate();">
                <br>
                <strong class="text">Email Address</strong><br>
                <input type=email name='email_address' id='email' class="w3-input w3-border w3-round" required=true/><br>
                <strong class="text">Course ID(e.g. CMSC420)</strong><br>
                <input type=text name='course_id' id='course_id' class="w3-input w3-border w3-round" />
                <input type=submit name='go' id='button' value='register' /><br>
                <input type=submit name='unsub' id='unsub' value='unsub' />
            </form>
        </div>
        
        <script src='validate.js'>
            
        </script>
        
        <?php
            require "courseVerifier.php";
            require "connect.php";
            
            if(isset($_POST['go'])){
                $courseID = $_POST['course_id'];
                $email = $_POST['email_address'];
                $link ='https://app.testudo.umd.edu/soc/search?courseId='.trim($courseID).
                '&sectionId=&termId=201808&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on';
                if(findCourse($link) === 0 || (strlen($courseID) != 7 && strlen($courseID) != 8)){
                    echo "<script>alert('The Course you entered does not exist!')</script>";
                }else if(filter_var($email, FILTER_VALIDATE_EMAIL) === FALSE){
                    echo "<script>alert('Invalid email address')</script>";
                }else{
                    $table = "contacts";
                    $course_name = $_POST['course_id'];
                    
                    
                    $stmt = $db->prepare("SELECT email FROM contacts where course_name = ? and email = ?");
                    $stmt->bind_param("ss",$course_name,$email);
                    $stmt->execute();
                    
                    
                    $result = $stmt->get_result();
                    $row = $result->fetch_assoc();
                    
                    if($row){
                        echo "<script>alert('You have already registered this course using this email')</script>";
                    }else{
                        $stmt = $db->prepare("INSERT INTO contacts (course_name, email) VALUES (?, ?)");
                        $stmt->bind_param("ss",$course_name,$email);
                        $stmt->execute();
                        echo "<script>alert('Course and Email are registered!')</script>";
                    }
                    
                    
                    
                }
                
            }
            
            if(isset($_POST['unsub'])){
                $email = $_POST['email_address'];
                $table = "contacts";
                
                $stmt = $db->prepare("SELECT * FROM contacts where email = ?");
                $stmt->bind_param("s",$email);
                $stmt->execute();
                    
                $result = $stmt->get_result();
                $row = $result->fetch_assoc();
                
                if($row === NULL){
                    echo "<script>alert('There are no matching records for this email address')</script>";
                }else{
                    $stmt = $db->prepare("DELETE FROM contacts where email = ?");
                    $stmt->bind_param("s",$email);
                    $stmt->execute();
                    echo "<script>alert('You have been unsub from all regiestered courses!')</script>";
                }
                    
                
            }
        
        
        
        
        
        
        ?>
        
    </body>
</html>