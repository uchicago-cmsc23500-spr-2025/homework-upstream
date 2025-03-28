fn main() {
    /*
    Clippy is a tool that allows you to catch mistakes and improve your code. For this
    exercise, run ``` cargo clippy ``` to see the suggestions and correct the errors.
    */

    let mut res = 42;
    let option = Some(12);
    for x in option {
        // clippy will suggest changing this to 'if let Some(x) = option'
        res += x;
    }
    println!("{}", res);

    /*
    Go back to the exercises in Module 1 and Module 2 and run cargo fmt
    Note if this changes your formatting.
    */
}
