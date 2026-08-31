pub fn pr_2559() {
    let mut sys_input = String::new();
    io::stdin().read_line(&mut sys_input).unwrap();
    let sys_input: Vec<usize> = sys_input
        .split_ascii_whitespace()
        .map(|x| x.trim().parse::<usize>().unwrap())
        .collect();

    let (n, k): (usize, usize) = (*sys_input.get(0).unwrap(), *sys_input.get(1).unwrap());

    let mut num_list = String::new();
    io::stdin().read_line(&mut num_list).unwrap();
    let num_list: Vec<isize> = num_list
        .split_ascii_whitespace()
        .map(|x| x.trim().parse::<isize>().unwrap())
        .collect();

    let mut psum: Vec<isize> = vec![num_list[0]];
    for i in 1..n {
        psum.push(psum[i - 1] + num_list[i]);
    }

    let mut ret = -10000004;

    for i in k..n {
        // println!("{}", i);
        if psum[i] - psum[i - k] > ret {
            ret = psum[i] - psum[i - k];
        }
    }

    println!("{}", ret);
}
