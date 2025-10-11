/**
 * Articles/Blog Module
 * Matches the functionality from the blog folder
 */

document.addEventListener('DOMContentLoaded', function () {
    const blogItems = document.querySelectorAll('.blog-item');
    const categoryFilters = document.querySelectorAll('.category-filter');
    const featuredPost = document.querySelector('.featured-post');

    // Mobile filters
    const mobileCategoryChips = document.querySelectorAll('.mobile-category-chip');

    // Pagination variables
    let currentPage = 1;
    const postsPerPage = 5;
    let filteredPosts = Array.from(blogItems);

    // Make featured post clickable
    if (featuredPost) {
        featuredPost.addEventListener('click', function () {
            // Navigate to featured post
            console.log('Featured post clicked');
        });
    }

    // Make blog items clickable
    blogItems.forEach(item => {
        item.addEventListener('click', function (e) {
            if (e.target.tagName !== 'BUTTON') {
                console.log('Blog post clicked:', this.querySelector('h2').textContent);
            }
        });

        item.style.cursor = 'pointer';
    });

    // Category filtering
    categoryFilters.forEach(filter => {
        filter.addEventListener('click', function () {
            const category = this.dataset.category;

            // Update active state
            categoryFilters.forEach(f => f.classList.remove('active'));
            this.classList.add('active');

            // Filter blog posts
            filterPosts(category);
        });
    });

    // Mobile Category filtering
    mobileCategoryChips.forEach(chip => {
        chip.addEventListener('click', function () {
            const category = this.dataset.category;

            // Update active state for mobile
            mobileCategoryChips.forEach(c => c.classList.remove('active'));
            this.classList.add('active');

            // Update desktop category active state (if exists)
            categoryFilters.forEach(f => {
                f.classList.remove('active');
                if (f.dataset.category === category) {
                    f.classList.add('active');
                }
            });

            // Filter blog posts
            filterPosts(category);
        });
    });

    // Filter function
    function filterPosts(category) {
        // Show/hide featured post based on category
        if (featuredPost) {
            if (category === 'all') {
                featuredPost.style.display = 'block';
            } else {
                featuredPost.style.display = 'none';
            }
        }

        filteredPosts = Array.from(blogItems).filter(item => {
            let show = true;

            // Category filter
            if (category !== 'all') {
                show = item.dataset.category === category;
            }

            return show;
        });

        currentPage = 1;
        displayPosts();
        updateCategoryCounts();
        updatePagination();

        // Scroll to the top of blog container AFTER display animation completes
        // Display takes 200ms + (5 posts * 50ms) = 450ms total
        setTimeout(() => {
            scrollToBlogTop(category);
        }, 500);
    }

    // Scroll to blog container top
    function scrollToBlogTop(category) {
        const blogContainer = document.getElementById('blog-container');
        const mainContainer = document.querySelector('.main-container');

        if (!blogContainer || !mainContainer) return;

        // Get viewport and scroll position
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // If filtering by specific category (not "all"), scroll to align blog container with sidebar
        if (category !== 'all') {
            const blogRect = blogContainer.getBoundingClientRect();
            const blogTop = blogRect.top + scrollTop;

            // Scroll to position blog container at 120px from top (aligned with sidebar)
            window.scrollTo({
                top: blogTop - 120, // 120px = navbar height + spacing to match sidebar sticky position
                behavior: 'smooth'
            });
        } else {
            // For "All Posts", use the original minimal scroll behavior
            const mainRect = mainContainer.getBoundingClientRect();

            // Only scroll if the main container is above viewport
            if (mainRect.top < 0) {
                const targetPosition = scrollTop + mainRect.top - 120;

                window.scrollTo({
                    top: Math.max(0, targetPosition),
                    behavior: 'smooth'
                });
            }
        }
    }

    // Scroll to blog container for pagination
    function scrollToBlogContainer() {
        const blogContainer = document.getElementById('blog-container');
        if (!blogContainer) return;

        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const blogRect = blogContainer.getBoundingClientRect();
        const blogTop = blogRect.top + scrollTop;

        // Scroll to position blog container at 120px from top (aligned with sidebar)
        window.scrollTo({
            top: blogTop - 120, // 120px = navbar height + spacing to match sidebar sticky position
            behavior: 'smooth'
        });
    }

    // Display posts for current page
    function displayPosts() {
        const startIndex = (currentPage - 1) * postsPerPage;
        const endIndex = startIndex + postsPerPage;

        // Fade out all posts
        blogItems.forEach(item => {
            if (item.style.opacity === '1') {
                item.style.opacity = '0';
            }
        });

        // Wait briefly, then show relevant posts
        setTimeout(() => {
            blogItems.forEach(item => {
                item.style.display = 'none';
            });

            // Show posts for current page with subtle stagger
            filteredPosts.slice(startIndex, endIndex).forEach((item, index) => {
                item.style.display = 'block';
                setTimeout(() => {
                    item.style.opacity = '1';
                    item.style.transform = 'translateY(0)';
                }, index * 50);
            });

            // Update posts range display
            const totalPosts = filteredPosts.length;
            const displayStart = totalPosts > 0 ? startIndex + 1 : 0;
            const displayEnd = Math.min(endIndex, totalPosts);

            const postsRange = document.getElementById('posts-range');
            const totalPostsEl = document.getElementById('total-posts');

            if (postsRange) postsRange.textContent = `${displayStart}-${displayEnd}`;
            if (totalPostsEl) totalPostsEl.textContent = totalPosts;
        }, 200);
    }

    // Update pagination controls
    function updatePagination() {
        const totalPages = Math.ceil(filteredPosts.length / postsPerPage);
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        const pageNumbersContainer = document.getElementById('page-numbers');

        if (!pageNumbersContainer) return;

        // Update previous button
        if (prevBtn) prevBtn.disabled = currentPage === 1;

        // Update next button
        if (nextBtn) nextBtn.disabled = currentPage === totalPages || totalPages === 0;

        // Generate page numbers
        pageNumbersContainer.innerHTML = '';

        if (totalPages <= 5) {
            // Show all pages if 5 or fewer
            for (let i = 1; i <= totalPages; i++) {
                const pageBtn = createPageButton(i);
                pageNumbersContainer.appendChild(pageBtn);
            }
        } else {
            // Show first page
            pageNumbersContainer.appendChild(createPageButton(1));

            if (currentPage > 3) {
                const ellipsis = document.createElement('span');
                ellipsis.className = 'px-2';
                ellipsis.textContent = '...';
                ellipsis.style.color = 'var(--text-tertiary)';
                pageNumbersContainer.appendChild(ellipsis);
            }

            // Show pages around current page
            const start = Math.max(2, currentPage - 1);
            const end = Math.min(totalPages - 1, currentPage + 1);

            for (let i = start; i <= end; i++) {
                pageNumbersContainer.appendChild(createPageButton(i));
            }

            if (currentPage < totalPages - 2) {
                const ellipsis = document.createElement('span');
                ellipsis.className = 'px-2';
                ellipsis.textContent = '...';
                ellipsis.style.color = 'var(--text-tertiary)';
                pageNumbersContainer.appendChild(ellipsis);
            }

            // Show last page
            if (totalPages > 1) {
                pageNumbersContainer.appendChild(createPageButton(totalPages));
            }
        }
    }

    // Create page button
    function createPageButton(pageNum) {
        const button = document.createElement('button');
        button.className = `page-number px-3 py-2 text-sm font-medium rounded-lg transition-colors`;
        button.textContent = pageNum;
        button.dataset.page = pageNum;

        // Apply theme styles
        if (pageNum === currentPage) {
            button.style.background = 'var(--page-primary-gradient)';
            button.style.color = '#ffffff';
            button.style.border = '1px solid var(--page-text-accent)';
            button.style.fontWeight = '600';
            button.style.boxShadow = '0 2px 8px rgba(20, 184, 166, 0.3)';
            button.classList.add('active');
        } else {
            button.style.background = 'var(--page-bg-card)';
            button.style.color = 'var(--page-text-secondary)';
            button.style.border = '1px solid var(--page-border-color)';
        }

        button.addEventListener('click', function () {
            currentPage = parseInt(this.dataset.page);
            displayPosts();
            updatePagination();

            // Scroll to align blog container with sidebar AFTER display animation
            setTimeout(() => {
                scrollToBlogContainer();
            }, 500);
        });

        return button;
    }

    // Pagination button event listeners
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    if (prevBtn) {
        prevBtn.addEventListener('click', function () {
            if (currentPage > 1) {
                currentPage--;
                displayPosts();
                updatePagination();
                // Delay scroll until display animation completes
                setTimeout(() => {
                    scrollToBlogContainer();
                }, 500);
            }
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function () {
            const totalPages = Math.ceil(filteredPosts.length / postsPerPage);
            if (currentPage < totalPages) {
                currentPage++;
                displayPosts();
                updatePagination();
                // Delay scroll until display animation completes
                setTimeout(() => {
                    scrollToBlogContainer();
                }, 500);
            }
        });
    }

    // Update category counts
    function updateCategoryCounts() {
        categoryFilters.forEach(filter => {
            const category = filter.dataset.category;
            let count = 0;

            if (category === 'all') {
                count = blogItems.length;
            } else {
                count = Array.from(blogItems).filter(item =>
                    item.dataset.category === category
                ).length;
            }

            const countSpan = filter.querySelector('span');
            if (countSpan) {
                countSpan.textContent = `(${count})`;
            }
        });
    }

    // Initialize
    displayPosts();
    updatePagination();

    // Add transition styles to blog items
    blogItems.forEach(item => {
        item.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
    });
});
