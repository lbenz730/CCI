# GPA calculator for Middlebury College Center for Careers and Internships
This is a web application for determining how many courses in which one needs to get a certain grade in order to raise their current grade point average to some desired grade point average. Since this application was designed for Middlebury College Center for Careers and Internships, GPA contributions from the Assumed Grade is based on the [grading system used at Middlebury College](http://www.middlebury.edu/about/handbook/academics/Grades_and_Records). Even if your school uses a slighlty different grading scale, this application will provide a very close approximation (if not exact).

To use the app, visit http://cci.herokuapp.com/.

## Usage:
__Curent GPA:__ Enter your current GPA, to any number of desired decimal places.

__Desired GPA:__ Enter your desired GPA, to any number of desired decimal places.

__# of Course Taken:__ Enter number of courses taken, to any number of desired decimal places.

__Assumed Grade:__ Enter letter grade (A, B+, C- etc.), with letter capitalized. 

### Possible Errors:
You will get errors for entering non-numeric text in any field that requires numeric text, or for entering numeric text in the __Assumed Grade__ field. Additionally, you will get an error if it is impossible for you to reach your target GPA with the Assumed Grade. For example, a student with current GPA of 3.2 and target GPA of 3.5 will not be able to reach their target GPA with Assumed Grade of B+ (weight = 3.3).


### Developer Comments/Questions
If you notice something that I didnt't catch, break the app, or have futher questions, please send me an email at luke.benz@yale.edu.
