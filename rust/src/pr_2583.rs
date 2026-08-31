fn pr_2583() {
    let mut sys_input = String::new();
    io::stdin().read_line(&mut sys_input).unwrap();
    let sys_input: Vec<usize> = sys_input
        .trim()
        .split_ascii_whitespace()
        .map(|x| x.trim().parse::<usize>().unwrap())
        .collect();
    let (m, n, k) = (sys_input[0], sys_input[1], sys_input[2]);

    let mut map: Vec<Vec<usize>> = vec![vec![0; n + 1]; m + 1];

    for _ in 0..k {
        let mut sys_input = String::new();
        io::stdin().read_line(&mut sys_input).unwrap();
        let sys_input: Vec<usize> = sys_input
            .trim()
            .split_ascii_whitespace()
            .map(|x| x.trim().parse::<usize>().unwrap())
            .collect();
        let (s_x, s_y, e_x, e_y) = (sys_input[0], sys_input[1], sys_input[2], sys_input[3]);

        for i in s_y..e_y {
            for j in s_x..e_x {
                map[i][j] = 1;
            }
        }
    }
    let mut ret = 0;
    let mut sizes: Vec<usize> = vec![];

    let mut visited: Vec<Vec<bool>> = vec![vec![false; n]; m];

    for y in 0..m {
        for x in 0..n {
            if map[y][x] == 0 && !visited[y][x] {
                ret += 1;
                let mut size = 0;
                dfs(y, x, &map, &mut visited, &mut size, m, n);
                sizes.push(size);
            }
        }
    }

    println!("{ret}");
    sizes.sort();
    for i in sizes {
        print!("{i} ");
    }
}

fn dfs(
    y: usize,
    x: usize,
    map: &Vec<Vec<usize>>,
    visited: &mut Vec<Vec<bool>>,
    size: &mut usize,
    m: usize,
    n: usize,
) {
    let dy = [-1, 0, 1, 0];
    let dx = [0, 1, 0, -1];

    visited[y][x] = true;
    *size = *size + 1;

    for i in 0..4 {
        let my: isize = y as isize + dy[i];
        let mx: isize = x as isize + dx[i];

        if my < 0 || my >= m as isize || mx < 0 || mx >= n as isize {
            continue;
        }

        let my = my as usize;
        let mx = mx as usize;
        if map[my][mx] == 1 {
            continue;
        }
        if visited[my][mx] {
            continue;
        }

        dfs(my, mx, map, visited, size, m, n);
    }
}
