/**
 * Articles/Blog Module
 * Matches the functionality from the blog folder
 */

// Toggle mobile categories menu - Make it globally accessible
window.toggleMobileCategories = function () {
    const categoriesContainer = document.getElementById('mobile-categories-container');
    const hamburgerBtn = document.getElementById('hamburger-btn');

    if (categoriesContainer && hamburgerBtn) {
        categoriesContainer.classList.toggle('expanded');
        hamburgerBtn.classList.toggle('active');
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const blogItems = document.querySelectorAll('.blog-item');
    const categoryFilters = document.querySelectorAll('.category-link');
    const featuredPost = document.querySelector('.redesigned-featured');

    // Debug: Log if featured post is found
    console.log('Featured post element found:', !!featuredPost);

    // Mobile filters
    const mobileCategoryChips = document.querySelectorAll('.mobile-category-chip');
    const categoriesContainer = document.getElementById('mobile-categories-container');
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const mobileFilterHeader = document.querySelector('.mobile-filter-header');

    // Keep track of featured post original place so we can detach/restore without leaving gaps
    let featuredOriginalParent = null;
    let featuredOriginalNextSibling = null;
    let featuredDetached = false;

    if (featuredPost) {
        featuredOriginalParent = featuredPost.parentNode;
        featuredOriginalNextSibling = featuredPost.nextSibling;
    }

    // Close dropdown when clicking outside
    document.addEventListener('click', function (event) {
        if (categoriesContainer && hamburgerBtn && categoriesContainer.classList.contains('expanded')) {
            const isClickInsideHeader = mobileFilterHeader && mobileFilterHeader.contains(event.target);
            const isClickInsideDropdown = categoriesContainer.contains(event.target);

            // Close if click is outside both header and dropdown
            if (!isClickInsideHeader && !isClickInsideDropdown) {
                categoriesContainer.classList.remove('expanded');
                hamburgerBtn.classList.remove('active');
            }
        }
    });

    // Pagination variables
    let currentPage = 1;
    const postsPerPage = 10;
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

            // Auto-collapse the menu after selection on mobile
            const categoriesContainer = document.getElementById('mobile-categories-container');
            const hamburgerBtn = document.getElementById('hamburger-btn');
            if (categoriesContainer && hamburgerBtn) {
                setTimeout(() => {
                    categoriesContainer.classList.remove('expanded');
                    hamburgerBtn.classList.remove('active');
                }, 300); // Small delay for visual feedback
            }
        });
    });

    // Filter function
    function filterPosts(category) {
        const pageHeader = document.querySelector('.page-header');
        const blogContent = document.querySelector('.blog-content');
        const blogContainer = document.getElementById('blog-container');
        const isMobile = window.innerWidth <= 768;

        // On mobile, hide page header when filtering by specific category
        if (isMobile && pageHeader) {
            if (category === 'all') {
                pageHeader.classList.remove('filtered');
            } else {
                pageHeader.classList.add('filtered');
            }
        }

        // Show/hide featured post based on category - ONLY show on "All Posts"
        if (featuredPost) {
            // If the featured article itself belongs to the selected category, keep it shown
            // as a normal card (no detaching). Otherwise detach it to avoid layout gaps.
            const featuredCategory = featuredPost.dataset && featuredPost.dataset.category;

            if (category === 'all' || featuredCategory === category) {
                // restore if previously detached
                if (featuredDetached && featuredOriginalParent) {
                    featuredOriginalParent.insertBefore(featuredPost, featuredOriginalNextSibling);
                    featuredDetached = false;
                }

                featuredPost.style.display = 'block';
                featuredPost.classList.remove('hidden');
                if (blogContent) {
                    blogContent.classList.remove('no-featured');
                }
            } else {
                // detach from DOM to ensure no space is reserved by the hidden element
                if (!featuredDetached && featuredPost.parentNode) {
                    featuredOriginalParent = featuredPost.parentNode;
                    featuredOriginalNextSibling = featuredPost.nextSibling;
                    featuredPost.parentNode.removeChild(featuredPost);
                    featuredDetached = true;
                }

                if (blogContent) {
                    blogContent.classList.add('no-featured');
                }
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

        // Display posts first, then scroll
        displayPosts();
        updateCategoryCounts();
        updatePagination();

        // Scroll after a longer delay to ensure layout is completely stable
        setTimeout(() => {
            scrollToFirstVisiblePost();
        }, 300);
    }

    // Scroll to blog container top - simplified version
    function scrollToBlogTop(category) {
        // Just use the main scroll function for consistency
        setTimeout(() => {
            scrollToFirstVisiblePost();
        }, 300);
    }

    // Scroll to the first visible blog post so it aligns with the sticky sidebar/filter bar.
    // This is more reliable than scrolling to the container when items/images can change height.
    function scrollToFirstVisiblePost() {
        // Small delay to ensure DOM updates are complete
        setTimeout(() => {
            const posts = Array.from(document.querySelectorAll('.blog-item'));
            if (!posts.length) return;

            const firstVisible = posts.find(p => {
                return p.style.display !== 'none' && p.offsetParent !== null && getComputedStyle(p).visibility !== 'hidden';
            });

            if (!firstVisible) return;

            const isMobile = window.innerWidth <= 768;

            // Calculate navbar height (matches CSS clamp(60px, 8vh, 80px))
            const navbarHeight = Math.min(Math.max(60, window.innerHeight * 0.08), 80);

            // Scroll to position where posts appear right below navbar
            // This allows the sticky sidebar to overlay naturally
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            const firstPostRect = firstVisible.getBoundingClientRect();
            const currentPostTop = scrollTop + firstPostRect.top;

            // Target position: navbar height + small padding (30px)
            const targetPosition = navbarHeight + 30;

            // Only scroll if the post is not already properly positioned
            if (Math.abs(currentPostTop - targetPosition) > 50) { // Allow 50px tolerance
                window.scrollTo({
                    top: Math.max(0, scrollTop + firstPostRect.top - targetPosition),
                    behavior: 'smooth'
                });
            }
        }, 150); // Slightly longer delay to ensure layout is completely stable
    }

    // Backwards-compatible wrapper - now just calls the main function
    function scrollToBlogContainer() {
        setTimeout(() => {
            scrollToFirstVisiblePost();
        }, 300);
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

        if (totalPages <= 10) {
            // Show all pages if 10 or fewer
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

            // Scroll to align the first visible post with the sidebar AFTER display animation
            setTimeout(() => {
                scrollToFirstVisiblePost();
            }, 300);
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
                    scrollToFirstVisiblePost();
                }, 300);
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
                    scrollToFirstVisiblePost();
                }, 300);
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

            const countSpan = filter.querySelector('.count');
            if (countSpan) {
                countSpan.textContent = count;
            }
        });

        // Update mobile category chips counts too
        mobileCategoryChips.forEach(chip => {
            const category = chip.dataset.category;
            let count = 0;

            if (category === 'all') {
                count = blogItems.length;
            } else {
                count = Array.from(blogItems).filter(item =>
                    item.dataset.category === category
                ).length;
            }

            const countSpan = chip.querySelector('.chip-count');
            if (countSpan) {
                countSpan.textContent = count;
            }
        });
    }

    // Initialize
    updateCategoryCounts(); // Update counts first before displaying
    displayPosts();
    updatePagination();

    // Initial scroll to ensure proper alignment
    setTimeout(() => {
        scrollToFirstVisiblePost();
    }, 500);

    // Add transition styles to blog items
    blogItems.forEach(item => {
        item.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
    });
});
