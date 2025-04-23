use std::mem::size_of_val;

struct Thing {
    i: usize,
    j: [usize; 100],
    k: usize,
}

impl Thing {
    fn new(i: usize, k: usize) -> Self {
        Thing {
            i,
            j: [i;100],
            k: k
        }
    }
    
    fn do_x(&self) -> usize {
        self.i + self.k + self.j[1]
    }
}

fn get_boxed_thing(thing: Thing) -> Box<Thing> {
    // TODO replace this to create a Box<Thing> from thing
    panic!("TODO");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_box_thing() {
        let thing = Thing::new(2, 5);
        assert_eq!(thing.do_x(), 9);
        assert_eq!(size_of_val(&thing), 816);
        let box_thing = get_boxed_thing(thing);
        assert_eq!(size_of_val(&box_thing), 8);
        assert_eq!(box_thing.do_x(), 9);
    }
}