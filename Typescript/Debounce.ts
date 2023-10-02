function debounce<T extends Function>(cb: T, wait = 20) {
    let h = 0;
    let callable = (...args: any) => {
        clearTimeout(h);
        h = setTimeout(() => cb(...args), wait);
    };
    return <T>(<any>callable);
}

// usage
let f = debounce((a: string, b: number, c?: number) => console.log(a.length + b + c || 0));
f("hi", 1, 1);
f("world", 1);
