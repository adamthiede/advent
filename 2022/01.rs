fn main() {
    day1();
}

// this is NOT MY CODE
fn day1() {
    let input = include_str!("01.txt");

    let mut current_sum = 0;
    let mut sums = Vec::new();

    for line in input.lines() {
        if line == "" {
            sums.push(current_sum);
            current_sum = 0;
        } else {
            current_sum = current_sum + line.parse::<i64>().expect("Invalid number");
        }
    }

    sums.push(current_sum);
    sums.sort();
    sums.reverse();

    println!("Top cal: {}", sums.get(0).unwrap());

    println!("Top 3 cal: {}", sums.get(0).unwrap() + sums.get(1).unwrap() + sums.get(2).unwrap());
}
