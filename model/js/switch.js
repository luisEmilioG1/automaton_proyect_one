
function switch_to_notation(json) {
    const initial_state = json['initial_state']
    let digraph = `digraph {
            initial[label = "", shape = "plaintext", style = "dotted"]
            initial -> ${initial_state}[color ="green"]
            `
    json['transitions'].forEach(element => {
        const  init_state = element['source']
        const final_state = element['destiny']
        const event_names = element['event']

        if (json['acceptance_states'].indexOf(init_state) > -1) {
            digraph += `${init_state}[color ="red"]
            `
        }
        if (json['acceptance_states'].indexOf(final_state) > -1) {
            digraph += `${final_state}[color ="red"]
            `
        }
            digraph += `${init_state} -> ${final_state}[label="${event_names}"]
            `
    });
    digraph += "}"
    return digraph
}

const json =
{
    "states": ["A", "B", "C", "D"],
    "alphabet": ["0", "1"],
    "initial_state": "A",
    "acceptance_states": ["D"],
    "transitions": [
        {"source": "A", "event": ["0"], "destiny": "B"},
        {"source": "A", "event": ["1"], "destiny": "C"},
        {"source": "B", "event": ["1"], "destiny": "C"},
        {"source": "C", "event": ["0","1"], "destiny": "C"},
        {"source": "B", "event": ["0"], "destiny": "D"},
        {"source": "D", "event": ["0","1"], "destiny": "D"}
    ]
}
console.log(switch_to_notation(json));
