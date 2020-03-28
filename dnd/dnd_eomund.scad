cvxty=10;
difference() {
    translate([0,0,23.001]) {
        scale([5,5,5])
        import("eomund.stl", convexity = cvxty); 
    }
    translate([0,0,-0.5])
    cube(size=[50,50,1], center=true);
}