// single line
/*
multiline
*/

//	build tag is a line comment starting with // +build
/* +build prod, dev, test */

// main is a special name declaring an executable rather than a library
// package starts every source file
package main

// import
import (
	"fmt"
	"os"
)

// func definition
// main is special, entrypoint for exec program
func main() {
	fmt.Println("hi how ar eyou")
	// variables
	var x int // declaration

	y := 4 // tpye, declare, and assign
	sum, prod := learnMultiple(x, y)
	fmt.Println("sum:", sum, "prod", prod)

	return
}

// funtions
func learnMultiple(x, y int) (sum, prod int) {
	return x + y, x * y
}

// builtin types and literals
func learnType() {
	str := "learngo" // string
	s2 := `a "raw" string literal can include 
	line breaks`

	g := '<' // rune type, holds unicode code point

	f := 3.14159               // float64 64 bit f p number
	_, _, _, _ = str, s2, g, f // dummy values
	c := 3 + 4i                // complex128

	var u uint = 7 // unsigned int
	var pi float32 = 22. / 7

	n := byte('\n') // conversion syntax with a short declaration. byte is an alias for unit8

	var a4 [4]int                   // array of 4 ints, init to all 0
	a5 := [...]int{3, 1, 4, 4, 100} // array init witha fixed size of five elements, with values 3,1,4..

	// arrays have value semantics
	a4_cpy := a4
	a4_cpy[0] = 25

	fmt.Println(a4_cpy[0] == a4[0])

	// slices are dynamic size arrays.
	s3 := []int{4, 5, 5}    // no elipsis
	s4 := make([]int, 4)    // slice of 4 ints, init to 0
	var b2 [][]float64      // declaration only, nothing allocated here
	bs := []byte("a slice") // type conversion syntax

	// slices (as well as maps and channels) have reference semantics, arrays have value
	s3_cpy := s3 // both variables point to sam einstance
	s := []int{1, 2, 4}
	s = append(s, 4, 5, 6) // appended to same slice

	// unused variabels
	fmt.Println(s, s4, b2, bs, s3_cpy, n, a5, pi, u, c)

	p, q := learnMem() // p,q both pointers to int
	fmt.Println(*p, *q)

	m := map[string]int{"three": 3, "four": 4}
	m["one"] = 1

	file, _ := os.Create("output.txt")
	fmt.Fprint(file, "this is how you write to a flie btw")
	file.Close()

	learnControlFlow()
}

// go is fully garbage collected.
// has pointers but no pointer arithimetic
// make a mistake with a nil pointer, but not by incrementing a pointer
// unlike c/cpp taking and returining an address of a local variable is also safe
func learnMem() (p, q *int) {
	p = new(int) // builtin function new allocates memory
	// allocated int slice is inited to 0,p is no longer nil.
	s := make([]int, 20) // allocates 20 ints as single block of memory
	s[3] = 7             // assign one of them
	r := -2              // declare another lcal
	return &s[3], &r     // & for taking the address of an object
}

func learnControlFlow() {
	if true {
		fmt.Println("told ya")
	} else {
		// something
	}
	x := 1
	switch x {
	case 1:
		break
	case 2:
		// do something else
	default:
		// is optional but
	}
	// type switch allows switching on the tpye of something instead of value
	var data interface{}
	data = ""
	switch c := data.(type) {
	case string:
		fmt.Println(c, "is a string")
	case int64:
		fmt.Println("%d is an int", c)
	default:
		// all other cases
	}
	for x := 0; x < 3; x++ {
		fmt.Println("iteration", x)
	}

	for { // infinte loop
		break
		continue
	}

	for key, val := range map[string]int{"one": 1, "two": 2} {
		fmt.Println("key=%s %d", key, val)
	}

	// function literals are closures
	xBig := func() bool {
		return x > 1000
	}
	fmt.Println(xBig)

	x = 1.3e3 // make x = 1300

	fmt.Println("Add + double two numbers: ",
		func(a, b int) int {
			return (a + b) * 2
		}(10, 2))

	return
}

func learnNamedReturns(x, y int) (z int) {
	z = x * y
	return // z is implicit here because we named it earlier
}

func learnFunctionFactory() {
	fmt.Println(sentenceFactory("summer")("A beautiful", "day!"))
	// equivalent
	d := sentenceFactory("summer")
	fmt.Println(d("A beautifl", "day!"))
}

// decorators are common in other languages. Same can be done in Go
// with function literals that accept arguments
func sentenceFactory(myString string) func(before, after string) string {
	return func(before, after string) string {
		return fmt.Sprintf("%s %s %s", before, after, myString) // new string
	}
}

// defer
func learnDefer() (ok bool) {
	defer fmt.Println("deffered statements are executed in LIFO order")
	defer fmt.Println("this one will be printed before the above string")
	return true
}

// Stringer
type Stringer interface {
	String() string
}

type pair struct {
	x, y int
}

// define a method on type pair. implements Stringer because Pair has defined all the methods in interface
func (p pair) String() string {
	// p is called the receiver
	// dot syntax for accessing struct members
	return fmt.Sprintf("(%d, %d)", p.x, p.y)
}

func learnInterfaces() {
	p := pair{3, 4}
	fmt.Println(p.String())

	var i Stringer
	i = p
	i.String()

	learnVariadicParams("hi", "bi", "ni")
}

// ... variadic params
func learnVariadicParams(myStrings ...interface{}) {
	for _, param := range myStrings {
		fmt.Println("param: ", param)
	}
	fmt.Println(myStrings...)
	learnErrorHandling()
}

func learnErrorHandling() {
	learnConcurrency()
}

// c channel, concurrency safe communication object
func inc(i int, c chan int) {
	c <- i + 1 // <- is the send operator when a channel appears on left
}

func learnConcurrency() {
	// slice
	c := make(chan int)
	go inc(0, c)
	go inc(10, c)
	go inc(-805, c)

	fmt.Println(<-c, <-c, <-c) // channel on right is receive operator

	cs := make(chan string)       // a challen of strings
	ccs := make(chan chan string) // a channel of string channels

	go func() {
		c <- 84
	}() // start a new go routing just to send a value

	go func() { cs <- "wordy" }() // start a new go routing to send value

	select {
	case i := <-c:
		fmt.Println("it's a %T", i)
	case <-cs:
		fmt.Println("it's a string")
	case <-ccs: // empty channel not ready for communication
		fmt.Println("didn't haappen")
	}
	// one of the two go routines started above has completed, the other will remain blocked
}
