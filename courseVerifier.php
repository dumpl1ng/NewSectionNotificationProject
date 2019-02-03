<?php

            /*verify that user input course number exists*/
            function findCourse($link){
                $fp = fopen($link,'r');
                while(!feof($fp)){
                    $lines = fgets($fp);
                    $pattern = '/<div class="no-courses-message">No courses matched your search filters above.<\/div>/';
                    if(preg_match($pattern,$lines) === 1){
                        return 0;
                    }
                }
                return 1;
            }








?>