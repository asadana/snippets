/* 
 * OSG Simple box
 *
 * Copyright (c) 2009 Jérémie Decock
 */

#include <osg/Group>
#include <osg/Geode>
#include <osg/ShapeDrawable>
#include <osgViewer/Viewer>

int main(int, char **) {

    // Set scenegraph
    osg::ref_ptr<osg::Box> box = new osg::Box( osg::Vec3(0,0,0), 1.0f );

    osg::ref_ptr<osg::ShapeDrawable> boxDrawable = new osg::ShapeDrawable(box);

    osg::ref_ptr<osg::Geode> geode = new osg::Geode;
    geode->addDrawable(boxDrawable);

    osg::ref_ptr<osg::Group> root = new osg::Group;
    root->addChild(geode);

    // Viewer
    osgViewer::Viewer viewer;
    viewer.setSceneData(root);
    viewer.run();

    return 0;
}
