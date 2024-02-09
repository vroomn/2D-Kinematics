# 2D Kinematics Simulator
A simple simulation of an object flying out of a cannon at a specified velocity and angle

## Running the software (or appending more)
I reccomend using python virtual enviroments  
```python -m venv 'YOUR NAME CHOICE'```  
Then navigate to the "Scripts" directory and run either "Activate.ps1" or "activate.bat". Now that it's a virtual enviroment the project requries Pygame, so:  

## Documentation
The entire simulation operates within the Pygame render loop, using ```PhysicsObject.physicsStep()``` within am if loop to control when the object is stimulated, and provide a floor for the object to hit. The simulation relies on the formula $\Delta y = (Velocity_{Inital\ y})(Time)+\frac{1}{2}(Gravity_{Acceleration})(Time)^2$ for the y component and $\Delta x = (Velocity_{Inital\ x})(Time)$ for the x component.

These computations rely on the object being a point in space, and so the actual sphere is merely visual representation that has no bearing on the output of the simulation itself. Time is measured the moment before the rendering/simulation loop as to provide a refrence for the physics algorithm to have a frame of refrence, this is then detracted from current time at ```physicsStep()``` for an accurate reading of $\Delta Time$. Rendering is handled by Pygame, with the FPS being locked to 60 for consistent results accross devices.

Inputs such as inital velocity are gathered through the standard library method of reading ```STDIN```. Each input is cast to an integer and absolute valued, then a check is performed to verify the input is valid. For the launch angle, the ```PhysicsObject``` class is equipped with a clamp method to ensure that there are no conflicts. 