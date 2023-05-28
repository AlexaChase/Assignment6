<!DOCTYPE html>
<html>
    <head>
        <title>Calculate the value of PI</title>
    </head>
    
    <body>
        <?php
        function formula() {
            $value= 0;
            for ($i= range($n)):
                $calculation= (-1) ** $i /(2*$i+1);
                $value= $value + $calculation;
            return $value*4;
        }
        echo "Please enter 'select' to let the program choose a number or enter 'number' to choose your own: ";
        $iterations="";
        if ($iterations= "number"){
           $number= int(input("Please enter a number: "));
            $pi=formula($number);
            echo ("The value of pi is:", $pi);
        }
        if ($iterations= "select"){
            $number= random_int(1, 100);
            echo ("The value selected by the program is:", $number);
            $pi=formula($number);
            print("The value of pi is:", $pi);
        }
        else{
            echo "Error, please try again";
        }
        ?>
    </body>
</html>
