pub fn pr_9996() {
    let mut m = String::new();
    let mut pattern = String::new();

    io::stdin().read_line(&mut m).unwrap();
    let m: i32 = m.trim().parse::<i32>().unwrap();

    io::stdin().read_line(&mut pattern).unwrap();
    let pattern: Vec<String> = pattern
        .split("*")
        .map(|x| x.trim().parse::<String>().unwrap())
        .collect();
    let first_patter: String = pattern.first().unwrap().to_string();
    let last_patter: String = pattern.last().unwrap().to_string();

    let mut result: Vec<String> = vec![];
    for _ in 0..m {
        let mut sys_input = String::new();
        io::stdin().read_line(&mut sys_input).unwrap();
        sys_input = sys_input.trim().parse::<String>().unwrap();

        let fist_word = sys_input[0..first_patter.len()].to_string();
        let last_word = sys_input[sys_input.len() - last_patter.len()..].to_string();

        if first_patter == fist_word && last_patter == last_word {
            result.push("DA".to_string());
        } else {
            result.push("NE".to_string());
        }
    }

    for i in result {
        println!("{}", i);
    }
}
