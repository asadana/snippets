// See http://en.wikibooks.org/wiki/OpenSCAD_User_Manual/The_OpenSCAD_Language#Modifier_Characters
// Use this subtree as usual in the rendering process but also draw it unmodified in transparent pink.
// Usage:
//   # { ... }


difference() {
	// start objects
	cylinder (h = 12, r=5, center = true, $fn=100);
        // first object that will subtracted
	#rotate ([90,0,0]) cylinder (h = 15, r=1, center = true, $fn=100);
        // second object that will be subtracted
	#rotate ([0,90,0]) cylinder (h = 15, r=3, center = true, $fn=100);
}