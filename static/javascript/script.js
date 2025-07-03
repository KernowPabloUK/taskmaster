/**
 * Task Management Scripts
 * Handles task actions like toggling completion status
 */

document.addEventListener('DOMContentLoaded', function() {
    // Task completion toggle
    initTaskToggle();
});

/**
 * Initialize task completion toggle functionality
 */
function initTaskToggle() {
    // Select all checkbox buttons
    const checkboxButtons = document.querySelectorAll('.checkbox-btn');
    
    checkboxButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Get the task ID from data attribute
            const taskId = this.dataset.taskId;
            
            // Create and send AJAX request
            fetch(`/toggle/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Reload the page to show updated lists
                    window.location.reload();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
}