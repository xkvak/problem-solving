pub fn pr_1620() {
    let mut sys_input = String::new();
    io::stdin().read_line(&mut sys_input).unwrap();
    let mut sys_input: Vec<usize> = sys_input
        .split_ascii_whitespace()
        .map(|x| x.trim().parse::<usize>().unwrap())
        .collect();
    let (n, m): (usize, usize) = (sys_input[0], sys_input[1]);

    let mut pokemon_map1: HashMap<String, usize> = HashMap::new();
    let mut pokemon_map2: HashMap<usize, String> = HashMap::new();

    for i in 1..n + 1 {
        let mut sys_input = String::new();
        io::stdin().read_line(&mut sys_input).unwrap();
        sys_input = sys_input.trim().parse::<String>().unwrap();
        let sys_input_clone = sys_input.clone();
        pokemon_map1.insert(sys_input, i);
        pokemon_map2.insert(i, sys_input_clone);
    }

    for _ in 0..m {
        let mut buf: String = String::new();
        io::stdin().read_line(&mut buf).unwrap();
        buf = buf.trim().parse::<String>().unwrap();

        if is_string_numeric(&buf) {
            let buf: usize = buf.parse::<usize>().unwrap();
            println!("{}", pokemon_map2.get(&buf).unwrap());
        } else {
            let buf: String = buf.parse::<String>().unwrap();
            println!("{}", pokemon_map1.get(&*buf).unwrap());
        }
    }
}

fn is_string_numeric(str: &String) -> bool {
    str.parse::<usize>().is_ok()
}
