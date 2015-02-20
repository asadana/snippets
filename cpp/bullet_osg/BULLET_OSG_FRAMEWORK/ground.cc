/* 
 * Bullet OSG Framework.
 * The ground module.
 *
 * Copyright (c) 2015 Jérémie Decock <jd.jdhp@gmail.com>
 *
 * www.jdhp.org
 */

#include "ground.h"

#include <osg/Geode>
#include <osg/Group>
#include <osg/Material>
#include <osg/PositionAttitudeTransform>
#include <osg/ShapeDrawable>

#include <Eigen/Dense>

#include <btBulletDynamicsCommon.h>

simulator::Ground::Ground() {
    // BULLET
    this->groundShape = new btStaticPlaneShape(btVector3(0, 0, 1), 0);

    this->groundMotionState = new btDefaultMotionState(btTransform(btQuaternion(0,0,0,1), btVector3(0,0,0)));
    btRigidBody::btRigidBodyConstructionInfo groundRigidBodyCI(0, this->groundMotionState, this->groundShape, btVector3(0, 0, 0));
    this->rigidBody = new btRigidBody(groundRigidBodyCI);

    // OSG
    this->osgGroup = new osg::Group();

    int num_tiles = 25;
    double tiles_size = 10.;

    for(int tile_pos_x=0 ; tile_pos_x < num_tiles ; tile_pos_x++) {
        for(int tile_pos_y=0 ; tile_pos_y < num_tiles ; tile_pos_y++) {
            osg::Vec3 tile_pos(tile_pos_x*tiles_size - (num_tiles*tiles_size)/2., tile_pos_y*tiles_size - (num_tiles*tiles_size)/2., -1);
            osg::ref_ptr<osg::Box> p_osg_box = new osg::Box(tile_pos, 1.0f);
            p_osg_box->setHalfLengths(osg::Vec3(tiles_size/2., tiles_size/2., 1));

            osg::ref_ptr<osg::ShapeDrawable> p_osg_shape_drawable = new osg::ShapeDrawable(p_osg_box);
            if((tile_pos_x%2 == 0) != (tile_pos_y%2 == 0)) {    // != is the XOR logical operator...
                p_osg_shape_drawable->setColor(osg::Vec4(1.0f, 1.0f, 1.0f, 0.0f)); // TODO: annulé par le "material" défini plus bas...
            } else {
                p_osg_shape_drawable->setColor(osg::Vec4(0.0f, 0.0f, 0.0f, 0.0f)); // TODO: annulé par le "material" défini plus bas...
            }

            osg::ref_ptr<osg::Geode> p_osg_geode = new osg::Geode();
            p_osg_geode->addDrawable(p_osg_shape_drawable);

            this->osgGroup->addChild(p_osg_geode);
        }
    }
    
    this->osgPAT = new osg::PositionAttitudeTransform();
    this->osgPAT->addChild(this->osgGroup);
}

simulator::Ground::~Ground() {
    delete this->rigidBody->getMotionState(); // TODO ?
    delete this->rigidBody; // TODO ?

    delete this->groundShape;
    delete this->groundMotionState;

    //delete this->osgPAT;
}

