use std::thread;
use std::sync::{Arc, Mutex};

struct Counter {
    count: i32
}

fn incr(/* TODO: Insert Counter Struct Parameter here */) {
    // TODO: Complete this function, which should increment the counter
    // struct's count field in-place
}

pub fn mutex_counter() { 
    
    // TODO: Initialize a counter variable, wrapped in a mutex here:
    let counter = /* TODO: Complete this assignment */
    

    // Mutable clone of the counter variable for use in the thread below:
    let mut c = counter.clone();
    // spawn a thread to call incr() 50 times
    let handle = thread::spawn(move|| {
        for _i in 0..50 {
            // TODO: Correctly call the increment function here
            /* Your call to incr() goes here */
            println!("thread spawned count {}", _i);
        }
    });
   
    // in the main thread, call incr() 50 times
    let mut c_main = counter.clone();
    for _i in 0..50 {
        // TODO: Correctly call the increment function here
        /* Your call to incr() goes here */
        println!("thread main count {}", _i);
    }

    handle.join().unwrap();

    // If done correctly, the counter should have been incremented
    // correctly and print a value of 100 below:
    println!("Final Counter Value {}", counter.lock().unwrap().count);

}