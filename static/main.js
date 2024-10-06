function check_me(input_id) {
    var checked_input = document.querySelector("input[id=" + input_id + "]");
    var checked_label = document.querySelector("label[name=" + input_id + "]");

    if (checked_input.checked) {
        checked_label.style.textDecoration = "line-through";
    } else {
        checked_label.style.textDecoration = "";
    }

    var btn = document.getElementById("remove_btn");

    // Check if any checkbox is checked
    var anyChecked = Array.from(document.querySelectorAll("input[name='check']")).some(input => input.checked);
    
    // Update button text based on whether any item is checked
    if (anyChecked) {
        btn.value = "REMOVE ITEMS";
        btn.style.color = "#FFFFFF";
        btn.style.backgroundColor = "#FE7575";
        btn.style.cursor = "pointer";
    } else {
        btn.value = "CHECK ITEMS"; // Change back to CHECK ITEMS when none are checked
        btn.style.color = "#000"; // Reset to default color
        btn.style.backgroundColor = "lightgray"; // Reset to default background
        btn.style.cursor = "default"; // Reset cursor
    }
}
