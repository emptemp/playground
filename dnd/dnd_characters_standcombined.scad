cvxty=10;

translate([5,5,42.5]) { 
    scale([12,12,12])
    import("fara.stl", convexity = cvxty);
}
rotate(a=50) {
    translate([-60,0,32.5]) {
        scale([7,7,7])
        import("eomund.stl", convexity = cvxty); 
    }
    translate([0,60,24]) { 
        scale([6,6,6])
        import("hel.stl", convexity = cvxty);
    }
    translate([0,-58,36]) { 
        scale([9,9,9])
        import("parkatian.stl", convexity = cvxty);
    }
    translate([60,-5,39]) { 
        scale([8,8,8])
        rotate(a=180)
        import("rumiko.stl", convexity = cvxty);
    }
}
translate([0,0,-0.5])
cube(size=[140,140,1], center=true);
