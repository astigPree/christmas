

document.addEventListener('DOMContentLoaded', () => {
    
    const all_trees_nav_button = document.getElementById('all-trees');
    const found_trees_nav_button = document.getElementById('found-trees');
    const not_found_trees_nav_button = document.getElementById('not-found-trees');
    const list_of_found_trees = document.getElementById('list-of-found-trees');
    const list_of_not_found_trees = document.getElementById('list-of-not-found-trees');


    all_trees_nav_button.addEventListener('click', () => {
        all_trees_nav_button.classList.add('app-nav-click');
        found_trees_nav_button.classList.remove('app-nav-click');
        not_found_trees_nav_button.classList.remove('app-nav-click');


        list_of_found_trees.classList.remove('hide');
        list_of_not_found_trees.classList.remove('hide');

    });


    found_trees_nav_button.addEventListener('click', () => {

        all_trees_nav_button.classList.remove('app-nav-click');
        found_trees_nav_button.classList.add('app-nav-click');
        not_found_trees_nav_button.classList.remove('app-nav-click');

        list_of_found_trees.classList.remove('hide');
        list_of_not_found_trees.classList.add('hide');

    });


    not_found_trees_nav_button.addEventListener('click', () => {

        all_trees_nav_button.classList.remove('app-nav-click');
        found_trees_nav_button.classList.remove('app-nav-click');
        not_found_trees_nav_button.classList.add('app-nav-click');

        list_of_found_trees.classList.add('hide');
        list_of_not_found_trees.classList.remove('hide');

    });

})