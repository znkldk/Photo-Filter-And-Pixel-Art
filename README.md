# Photo-Filter-And-Pixel-Art

This is a photo filter and Pixel Art algoritm that using Opencv.

It has 6 colors; 
Yellow White Black Red Green Blue
Every pixel in a photo turns the nearest color in 6 colors. And the result;


![output-onlinepngtools (1)](https://user-images.githubusercontent.com/49093505/81481625-284b3f80-923a-11ea-839e-6aef409dc970.png)
![output-onlinepngtools](https://user-images.githubusercontent.com/49093505/81481598-06ea5380-923a-11ea-88f1-5027cc128cf1.png)

In this example some places are painted wrong color and I love it :) I Thing it makes result better.

I must confess the hardest part in this project is choose the similar color. 
First I tried to RGB numbers. I had the pixel RGB numbers from photo and 6 main color numbers then I found the nearest main color number to my pixel RGB numbers and it was not the correct color. Color's word was more crazy then I though. In my first try RGB numbers were the similest but colors almost opposite. I though how can I fix this problem and I found a solution. 
It is not the best but It works.

*Choose the nearest color problem;

In this projeckt we have 6 colors. Lets talk abouth green and black.

Green's number is 0,255,0  
Black's number is 0,0,0  
and we have 0,100,0 to compare.
This color number is near to black but color is not. If you search this color (0,100,0) it is absolutly near green. The reason of this problem is rgb system colors doesnt settle equaly. For example in rgb system red has 10 number yellow has 5 numbers. Footprints are not equal.

*How to solve this problem;

I Just added more reference colors :) if we use more referans colors for black and green the distinction between the two becomes clearer. The result becomes more errorless 



![output-onlinepngtools (4)](https://user-images.githubusercontent.com/49093505/81481859-a9570680-923b-11ea-8fd6-e13c352c5953.png)


