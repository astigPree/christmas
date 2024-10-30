let near_trees = [];

document.addEventListener('DOMContentLoaded', () => {
    
    const near_trees_nav_button = document.getElementById('near-trees');
    const found_trees_nav_button = document.getElementById('found-trees');
    const not_found_trees_nav_button = document.getElementById('not-found-trees');
    
    const list_of_near_trees = document.getElementById('list-of-near-trees');
    const list_of_found_trees = document.getElementById('list-of-found-trees');
    const list_of_not_found_trees = document.getElementById('list-of-not-found-trees');

    const empty_trees_display = document.getElementById('empty-near-trees');
    setTimeout(() => {
        if (near_trees.length > 0) {
            empty_trees_display.classList.remove('hide');
        }
    },1000);

    near_trees_nav_button.addEventListener('click', () => {
        near_trees_nav_button.classList.add('app-nav-click');
        found_trees_nav_button.classList.remove('app-nav-click');
        not_found_trees_nav_button.classList.remove('app-nav-click');

        
        list_of_near_trees.classList.remove('hide');
        list_of_found_trees.classList.add('hide');
        list_of_not_found_trees.classList.add('hide');

    });


    found_trees_nav_button.addEventListener('click', () => {

        near_trees_nav_button.classList.remove('app-nav-click');
        found_trees_nav_button.classList.add('app-nav-click');
        not_found_trees_nav_button.classList.remove('app-nav-click');

        list_of_found_trees.classList.remove('hide');
        list_of_not_found_trees.classList.add('hide');
        list_of_near_trees.classList.add('hide');

    });


    not_found_trees_nav_button.addEventListener('click', () => {

        near_trees_nav_button.classList.remove('app-nav-click');
        found_trees_nav_button.classList.remove('app-nav-click');
        not_found_trees_nav_button.classList.add('app-nav-click');

        list_of_found_trees.classList.add('hide');
        list_of_not_found_trees.classList.remove('hide');
        list_of_near_trees.classList.add('hide');

    });

})