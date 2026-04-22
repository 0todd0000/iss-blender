# Create spike particle system

This mini-tutorial demonstrates how to use Particle Systems to replicate virus spikes.





Select the membrane object (i.e., the sphere).

Select the Particle System panel.

Press the "+" button to create a new particle system.


<center>
    <img src="ss/vr27.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>



Change the particle system type to "Hair"


<center>
    <img src="ss/vr28.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

Adjust the particle system options:

- `Advanced` = True
- `Emission.Number` = 50
- `Rotation` = True
- `Render.RenderAs` = Object
- `Render.Object.InstanceObject` = Cylinder

<center>
    <img src="ss/vr29.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>



These settings will add 50 spikes at random locations around the membrane.

However, notice that the spikes are offset from the membrane surface.

<center>
    <img src="ss/vr30.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>



Select the spike and enter Edit mode.

Select <kbd>A</kbd> to select all vertices.

Press <kbd>G</kbd> then <kbd>Y</kbd> and drag the spike until that it is close to the global origin (0,0,0).

<center>
    <img src="ss/vr31.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>



Verify that the spikes now start on the membrane surface.

<center>
    <img src="ss/vr32.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>



Return to Object Mode.

Select the sphere.

In the Particle Sytem panel adjust the scale until the spikes are an appropriate size.

<center>
    <img src="ss/vr33.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>



From the main menu select `Render.. Render Image` 

<center>
    <img src="ss/vr34.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>



