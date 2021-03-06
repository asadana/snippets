# OSG TODO

http://jeux.developpez.com/tutoriels/?page=prog-3d#openscenegraph-3d

## STEP 1

- [x] import STL objects (cf livre OSG 3.0)
- [x] materials (different meterials for different objects), colors, ...
- [x] gestion des evenements clavier / sourie http://jeux.developpez.com/tutoriels/openscenegraph/evenements/ + livre p.232
- [ ] Fog (livre p. 134)
- [ ] display OSG as Qt4 (or Qt5) widget (cf. 2e livre)
- [ ] cameras http://jeux.developpez.com/tutoriels/openscenegraph/camera/
- [ ] shading (Flat / Gouraud / Phong shading)
- [ ] shadow see osgShadow nodekit http://trac.openscenegraph.org/documentation/OpenSceneGraphReferenceDocs/a01601.html
    - http://osgjs.org/examples/shadow/

## STEP 2

- [ ] GLSL (OpenGL Shading Language) !!!! see http://trac.openscenegraph.org/projects/osg//wiki/Support/Tutorials/ShadersIntroduction + livre p.152)
- [ ] draw 2d text on the screen
- [ ] draw points and lines (e.g. to draw edges of 3D graphs from .dot files)     http://osghelp.com/?p=48  http://forum.openscenegraph.org/viewtopic.php?t=9658&view=previous  http://svn.openscenegraph.org/osg/OpenSceneGraph/tags/osg_v0_9_7_rc1_sync_release/examples/osggeometry/osggeometry.cpp   http://www.delta3d.org/forum/viewtopic.php?showtopic=16609
- [ ] create objects form vertices, modify vertices of objects
    - infinite plane (ground) see the documentation of the Plane class ( http://trac.openscenegraph.org/documentation/OpenSceneGraphReferenceDocs/a00601.html ) -> "It can be used to represent an infinite plane. The infinite plane is described by an implicit plane equation a*x+b*y+c*z+d = 0." Use the following constructor : osg::Plane::Plane(const Vec3_type & v1, const Vec3_type & v2, const Vec3_type & v3).  This constructor calculates from the three points describing an infinite plane the internal values.  
- [ ] super-sample anti-aliasing (SSAA) see http://osghelp.com/?p=179  http://osghelp.com/?p=48   https://en.wikipedia.org/wiki/Spatial_anti-aliasing
    - OpenGL buffers and off-screen rendering (render in images, no X11) livre p.184
- [ ] particles see osgParticle http://trac.openscenegraph.org/documentation/OpenSceneGraphReferenceDocs/a01599.html
- [ ] animations http://jeux.developpez.com/tutoriels/openscenegraph/animations/
    - Animation path (to smoothly move an object from point A to point B) see http://osghelp.com/?p=19 (useful for physics, 3D graphs animations, MCTS, ...)
- [ ] transformations et états (cf. http://jeux.developpez.com/tutoriels/openscenegraph/)
- [ ] gestion des états (cf. http://jeux.developpez.com/tutoriels/openscenegraph/)
- [ ] post processing effects (depth of field, ...)
- [ ] motion blur (see http://forum.openscenegraph.org/viewtopic.php?t=12182) http://trac.openscenegraph.org/projects/osg//browser/OpenSceneGraph/trunk/examples/osgmotionblur/osgmotionblur.cpp
- [ ] textures (http://osghelp.com/?p=119)
- [ ] LOD (Level Of Details) : néessaire pour les "infinite planes"

## STEP 3

- [ ] callbacks, osg basics, ...
- [ ] OSG and SDL / Frame buffer (no X11) ???
- [ ] display scene without viewer object (manual render...) + mouse drag & drop of objects (e.g. for damper physics simulation)
- [ ] advanced materials: (google -> "opengl material")
   - transparent objects (livre p. 148)
   - mirror surfaces (eg black mirror ground, ...) -> search "openscenegraph reflect"
   - ...

## STEP 4

- [ ] soft shadows (radiosity), ...
- [ ] clouds (volumetric), volumetric textures, ... see osgVolume nodekit http://trac.openscenegraph.org/documentation/OpenSceneGraphReferenceDocs/a01607.html#details
- [ ] artistic stuff : e.g. see http://www.creativeapplications.net/c/openscenegraph-and-cefix-c-ipad/  https://www.flickr.com/photos/stephanmaximilianhuber/sets/72157623028241391/

See http://www.packtpub.com/openscenegrap-3-for-advanced-3d-programming-using-api-cookbook/book
