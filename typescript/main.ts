// 3 basic types 
let isDone: boolean = false;
let lines: number = 42;
let name: string = "anders";

// can omit type annotation if variables are derived from explicit literals
let isDone = false;
let lines = 43;
let name = "adners";

// when in doubt use "Any" type
let notSure: any = 4;
notSure = "maybe string";
notSure = false;

// const for constants
const xyz = 9;
xyz = 1; // error

// for collections, typed and generic arrays are avl
// typed
let list: number[] = [1,2,3];
// generic
let list: Array<number> = [1,2,3];

// enums
enum Color {red, green, blue};
let c: Color = Color.green;
console.log(Color[c]); // green

// void is used in special case of returning nothing
function returnNothing(): void {
    alert("i'm just an alert");
}

// functions are 1st class citizens, support the lambda "fat arrow" syntax and
// use type inference
//
// following are equivalent, same signature will be inferred by compiler and same js will be emitted
let f1 = function (i:number): number { return i*i; }
// return type inferred
let f2 = function (i:number) {return i*i;}
// 'fat arrow' syntax
let f3 = (i:number): number => {return i*i;}
// 'fat arrow' syntax with return type inferred
let f4 = (i:number) => i*i;

// interfaces = structural , anything that has props
interface Person {
    name: string;
    age?: number; // ? = optional prop
    move(): void;
}

// object that implements Person interface can be treated as a person since it has name and move properties
let p: Person = { name: "ahmed", move: () => { } };
// object having optional prop
let validPerson: Person = { name: "ahmed", age: 32, move() => {}};
// object having different prop is not a person.
let invalidPerson: Person = {name: "ahmed", age: true}; // not a Person

// interfaces can also describe a function type
interface SearchFunc {
    (source: string, subString: string): boolean;
}

// only param types important, names not
let mySearch: SearchFunc;
mySearch = function (src: string, sub: string) {
    return src.search(sub) != -1;
}

// classes - members are public by default
class Point {
    // prop
    x: number;
    // constructor
    constructor(x: number, public y:number = 0) {
        this.x = x;
    }
    // public and private in constructor will generate biolerplate for property and init in constructor.
    // y will be defined just like x is, but with less code
    // default values are also supported
    //
    // functions
    dist(): number {
        return Math.sqrt(this.x * this.x + this.y * this.y);
    }

    // static members
    static origin = new Point(0,0);
}
// classes can be explicitly marked as implementing an interface.
// any missing prop will then cause an error at compilation
class PointPerson implements Person {
    name: string
    move() {}
}
let p1 = new Point(10,20);
let p2 = new Point(24); // y will be 0

// inheritance
class Point3D extends Point {
    constructor(x : number, y : number, public z : number = 0) {
        super(x,y); // explicit call to super class constructor in mandatory
    }
    // function overwrite
    dist(): number {
        let d = super.dist();
        return Math.sqrt(d*d + this.z * this.z);
    }
}

// Modules, "." can be used as seperator for sub modules
module Geometry {
    export class Square {
        constructor(public sideLength: number = 0) {}
        area() {
            return Math.pow(this.sideLength, 2);
        }
    }
}

let s1 = new Geometry.Square(5);
// local alias for referencing a module
import G = Geometry;
let s2 = new G.Square(10);

// Generics
// classes
class Tuple<T1, T2> {
    constructor(public item1: T1, public item2: T2) {}
}
// interfaces
interface Pair<T> {
    item1: T;
    item2: T;
}
// functions
let pairToTuple = function <T>(p: Pair<T>) {
    return new Tuple(p.item1, p.item2);
};

let tuple = pairToTuple({item1: "hello", item2: "world"});

