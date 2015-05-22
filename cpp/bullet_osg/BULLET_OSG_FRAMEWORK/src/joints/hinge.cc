/* 
 * Bullet OSG Framework.
 * The hinge module.
 *
 * Copyright (c) 2015 Jérémie Decock <jd.jdhp@gmail.com>
 *
 * www.jdhp.org
 */

#include "hinge.h"

#include "tools/tools.h"

simulator::Hinge::Hinge(simulator::Part * part1,
                        simulator::Part * part2,
                        simulator::HingeSlot * joint_slot_for_part1,
                        simulator::HingeSlot * joint_slot_for_part2,
                        std::string _name) {

    this->name = _name;

    btRigidBody * bt_rigid_body1 = part1->getRigidBody();
    btRigidBody * bt_rigid_body2 = part2->getRigidBody();

    Eigen::Vector3d pivot_in_part1 = joint_slot_for_part1->getPivot();
    Eigen::Vector3d pivot_in_part2 = joint_slot_for_part2->getPivot();
    btVector3 bt_pivot_in_part1 = simulator::vec3_eigen_to_bullet(pivot_in_part1);
    btVector3 bt_pivot_in_part2 = simulator::vec3_eigen_to_bullet(pivot_in_part2);

    Eigen::Vector3d axis_in_part1 = joint_slot_for_part1->getAxis();
    Eigen::Vector3d axis_in_part2 = joint_slot_for_part2->getAxis();
    btVector3 bt_axis_in_part1 = simulator::vec3_eigen_to_bullet(axis_in_part1);
    btVector3 bt_axis_in_part2 = simulator::vec3_eigen_to_bullet(axis_in_part2);

    this->bulletTypedConstraint = new btHingeConstraint(*bt_rigid_body1, *bt_rigid_body2, bt_pivot_in_part1, bt_pivot_in_part2, bt_axis_in_part1, bt_axis_in_part2);
}

simulator::Hinge::Hinge(simulator::Part * part,
                        simulator::HingeSlot * joint_slot,
                        std::string _name) {

    this->name = _name;

    btRigidBody * bt_rigid_body = part->getRigidBody();

    Eigen::Vector3d pivot = joint_slot->getPivot();
    btVector3 bt_pivot_in_part = simulator::vec3_eigen_to_bullet(pivot);

    Eigen::Vector3d axis = joint_slot->getAxis();
    btVector3 bt_axis_in_part = simulator::vec3_eigen_to_bullet(axis);

    this->bulletTypedConstraint = new btHingeConstraint(*bt_rigid_body, bt_pivot_in_part, bt_axis_in_part);
}

simulator::Hinge::~Hinge() {
    // TODO
}

std::string simulator::Hinge::getName() const {
    return this->name;
}
