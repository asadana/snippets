#include "classes.h"

Foo::Foo(Point * _pt) {
    this->pt = _pt;
}

void Foo::translate() {
    this->pt->x += 1;
    this->pt->y += 1;
}
