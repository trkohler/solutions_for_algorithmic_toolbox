// fibbonaci solving in rust
use std::io;

fn main() {
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("failed to read input.");
    let n: u32 = n.trim().parse().expect("invalid input");
    let n = fibonacci(n);
    println!("Fibbonaci is {}", n);
}

fn fibonacci(number: u32) -> u32 { 
    let mut a = 0;
    let mut b = 1;
    for _ in 0..number {
        let tmp = a;
        a = b;
        b = a + tmp;
    }

    b
}
