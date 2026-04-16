# Import molecule

This mini tutorial describes how to import molecule geometry for general visualization in Blender.

# Import geometry


Launch Blender and select:

```
File.. Import.. Protein Data Bank (.pdb)
```

In the file dialog find the `.pdb` file that you created in the Avogadro2 mini-tutorial


In the right-hand panel of the file dialog change the following options:

- `Type of ball` = "Mesh"
- `Azimuth` = 4
- `Zenith` = 4
- `Scaling factors.. Distance` = 2
- `Sticks/bonds.. Color` = True
- `Sticks/bonds.. Smooth` = True
- `Sticks/bonds.. Bonds` = True
- `Sticks/bonds.. Distance` = 2



Press "Import"



<center>
    <img src="ss/im03.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>



You should now see the molecule!



<center>
    <img src="ss/im04.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>

# Simplify to one object

WITHOUT deselecting the molecule, press:

```
Object.. Apply.. Make Instances Real
```



<center>
    <img src="ss/im05.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>

Hold the <kbd>SHIFT</kbd> key and left-click on any atom

Before selecting an atom there will be a dark orange outline around the whole molecule.

<center>
    <img src="ss/im06.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>


After SHIFT-selecting an atom there will be a light orange outline around the atom.

<center>
    <img src="ss/im07.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>


Press <kbd>CTRL</kbd> + <kbd>J</kbd>  to join all of the imported objects into a single object

<center>
    <img src="ss/im08.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>

To confirm that there is now a single object:

Left click somewhere outside the molecule object.

Verify that there is no longer an orange outline (i.e., the object is now deselected.)

<center>
    <img src="ss/im09.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>

Left-click anywhere on the molecule object to select it.

Press <kbd>G</kbd> then move the mouse to verify that all of the molecule's sub-objects are moving together

<center>
    <img src="ss/im10.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>

Rename the object

- Right-click on the molecule object and select "Rename Active Object" from the pop-up menu

  


<center>
    <img src="ss/im11.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Change the name to "Caffeine" and press <kbd>ENTER</kbd> 

<center>
    <img src="ss/im12.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>



# Tidy the scene collection

In the Scene collection find the imported .pdb file.

<center>
    <img src="ss/im13.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Press the arrow key to expand the .pdb collection

Find the Caffeine object.



> [!NOTE]
> If you selected a different atom above (i.e., before joining the geometry objects together) the "Caffeine" object may appear in a different place in the .pdb collection.



<center>
    <img src="ss/im14.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>

Move the Caffeine object from the .pdb collection to the main collection 

- Left-click on the Caffeine object then drag it and drop it on "Collection"



<center>
    <img src="ss/im15.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>

Delete the .pdb collection:

- Right-click on caffeine.pdb and select "Delete hierarchy"

<center>
    <img src="ss/im16.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>


Verify that the .pdb collection is cone and that only the Caffeine object remains in the Scene Collection

<center>
    <img src="ss/im17.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

# Enhance visualization

Go to the Geometry Nodes workspace.


<center>
    <img src="ss/im18.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Press "New" to create a new Geometry Nodes instance.


<center>
    <img src="ss/im19.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

Verify that there are now input and output nodes


<center>
    <img src="ss/im20.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
 Add an Atomic Instance visualizer

  ```
  Add.. CGFigures Assets.. Atomic Nodes Instances..
  Atomic Instance Core Setup
  ```


<center>
    <img src="ss/im21.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

Drop the new node between the "Group Input" and "Group Output" nodes
- This should automically connect all three nodes together




Verify:

- The new node is connected to both the input and output nodes
- The molecule is now smoother 


<center>
    <img src="ss/im22.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Return to the default Layout workspace

Select the Material Preview shader to view atom colors


<center>
    <img src="ss/im23.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

Select the Rendered shader for a more attractive view


<center>
    <img src="ss/im24.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
# Set view

For very large or very small molecules the camera may not be in an ideal place for visualization.

The camera view can be most easily set using the 3D Navigation extension.

To enable the 3D Navigation extension:

- Open Preferences  (`Edit.. Preferences`)
- Select "Get Extensions" from the left-hand menu
- In the search bar begin to type "navigation"
- Find the "3D Navigation" extension
- Press "Install"



<center>
    <img src="ss/im25.jpg" alt="image" width="700"/>
    <br>
    <br>
    <br>
</center>




Verify that "3D Navigation" now appears in the Installed list.


<center>
    <img src="ss/im26.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Select the molecule, then verify that an orange outline appears around it.

Press <kbd>N</kbd> to show the side panel.

<center>
    <img src="ss/im27.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>


Select the "View" tab

<center>
    <img src="ss/im28.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>

Press "View to Selected"

This will automatically set the 3D Viewport view to show the whole molecule.

<center>
    <img src="ss/im29.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>



To align the camera to the same view as the 3D Viewport, select:

```
View.. Align View.. Align Active Camera to View
```






<center>
    <img src="ss/im30.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

The camera should now surround the molecule.


<center>
    <img src="ss/im31.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>



From the main menu select:

```
Render.. Render Image
```

This should produce an attractive rendered image.

<center>
    <img src="ss/im32.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>