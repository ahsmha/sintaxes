package main

type Set interface {
	Add(value int)
	Contains(value int) bool
	Length() int
	RemoveDuplicates()
}

func NewSet() Set {
	return &HashSet{make(map[int]bool)}
}

type HashSet struct {
	data map[int]bool
}

func (this *HashSet) Add(value int) {
	this.data[value] = true
}

func (this *HashSet) Contains(value int) (exists bool) {
	_, exists = this.data[value]
	return // implicit return
}

func (this *HashSet) Length() int {
	return len(this.data)
}

func (this *HashSet) RemoveDuplicates() {
	// already map takes care of that, no need to implement
}
