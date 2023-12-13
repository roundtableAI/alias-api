const textbox_id = 'exampleTextarea'

// Max number of characters to store in history 
const max_characters_for_history = 25000;

document.addEventListener('DOMContentLoaded', function () {

    // Text changes are stored here
    let question_history = [];
    let old_text = document.getElementById(textbox_id).value;
    let text_over_length = false;
    let start_time;

    // Handle input changes
    document.getElementById(textbox_id).addEventListener('input', function (e) {
        if (text_over_length) return;
        if (!start_time) {
            start_time = Date.now();
            t = 0;
        } else {
            t = Date.now() - start_time;
        }
        const state = e.target.value;
        const new_history = {
            s: state,
            t,
        };
        const length_of_history = JSON.stringify([...question_history, new_history]).length;
        if (length_of_history > max_characters_for_history) {
            text_over_length = true;
            return;
        }
        question_history.push(new_history);
        old_text = state;
    });

    // Handle copy changes
    document.getElementById(textbox_id).addEventListener('copy', function (e) {
        if (text_over_length) return;
        if (!start_time) {
            start_time = Date.now();
            t = 0;
        } else {
            t = Date.now() - start_time;
        }
        const new_history = {
            s: e.target.value,
            t,
            o: 'c',
            ct: window.getSelection().toString(),
        };
        const length_of_history = JSON.stringify([...question_history, new_history]).length;
        if (length_of_history > max_characters_for_history) {
            text_over_length = true;
            return;
        }
        question_history.push(new_history);
    });
});