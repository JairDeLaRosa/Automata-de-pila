/* eslint-disable no-unused-vars */
export class Stack {
    constructor() {
        this.items = [];
        this.states = [];
    }

    push(item) {
        this.items.push(item);
    }

    pop() {
        if (!this.isEmpty()) {
            return this.items.pop();
        }
        return null;
    }

    isEmpty() {
        return this.items.length === 0;
    }

    pushState(state) {
        this.states.push(state);
    }

    listStates() {
        return this.states;
    }

    clear() {
        this.states = [];
    }
}