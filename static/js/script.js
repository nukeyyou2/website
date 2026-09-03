document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.navbar');
    const navMenu = document.querySelector('.nav-menu');
    const menuToggle = document.getElementById('menuToggle');
    const navLinks = document.querySelectorAll('.nav-menu a');
    const sections = document.querySelectorAll('section[id]');
    const progressBar = document.getElementById('scrollProgress');
    const revealItems = document.querySelectorAll('[data-reveal]');

    const backToTopButton = document.createElement('button');
    backToTopButton.className = 'back-to-top';
    backToTopButton.innerText = '↑';
    backToTopButton.setAttribute('aria-label', '返回顶部');
    document.body.appendChild(backToTopButton);

    function setMenuState(open) {
        if (!navMenu || !menuToggle) {
            return;
        }

        if (open) {
            navMenu.classList.add('is-open');
            menuToggle.classList.add('is-open');
            menuToggle.setAttribute('aria-expanded', 'true');
        } else {
            navMenu.classList.remove('is-open');
            menuToggle.classList.remove('is-open');
            menuToggle.setAttribute('aria-expanded', 'false');
        }
    }

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            const shouldOpen = !navMenu.classList.contains('is-open');
            setMenuState(shouldOpen);
        });

        navLinks.forEach((link) => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 980) {
                    setMenuState(false);
                }
            });
        });

        document.addEventListener('click', (event) => {
            if (!navMenu || !menuToggle) {
                return;
            }

            const clickedInsideMenu = navMenu.contains(event.target);
            const clickedToggle = menuToggle.contains(event.target);
            if (!clickedInsideMenu && !clickedToggle && navMenu.classList.contains('is-open')) {
                setMenuState(false);
            }
        });
    }

    function updateActiveLink() {
        const scrollY = window.scrollY + 150;
        let activeId = '';

        sections.forEach((section) => {
            const sectionTop = section.offsetTop;
            const sectionBottom = sectionTop + section.offsetHeight;
            if (scrollY >= sectionTop && scrollY < sectionBottom) {
                activeId = section.getAttribute('id');
            }
        });

        if (!activeId && sections.length > 0) {
            activeId = sections[sections.length - 1].getAttribute('id');
        }

        navLinks.forEach((link) => {
            const href = link.getAttribute('href') || '';
            link.classList.toggle('is-active', href === `#${activeId}`);
        });
    }

    function updateProgressBar() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const percent = docHeight > 0 ? Math.min((scrollTop / docHeight) * 100, 100) : 0;
        if (progressBar) {
            progressBar.style.setProperty('--scroll-progress', `${percent.toFixed(2)}%`);
        }
    }

    function handleScroll() {
        if (window.scrollY > 16 && navbar) {
            navbar.classList.add('is-scrolled');
        } else if (navbar) {
            navbar.classList.remove('is-scrolled');
        }

        updateActiveLink();
        updateProgressBar();

        if (window.scrollY > 520) {
            backToTopButton.classList.add('is-visible');
        } else {
            backToTopButton.classList.remove('is-visible');
        }
    }

    function animateCounters() {
        const counters = document.querySelectorAll('.count-up[data-count]');
        counters.forEach((counter) => {
            const target = Number(counter.dataset.count || '0');
            if (Number.isNaN(target) || target <= 0) {
                counter.textContent = String(target || 0);
                return;
            }

            const duration = 1600;
            const startTime = performance.now();
            const startValue = 0;

            const step = (timestamp) => {
                const elapsed = timestamp - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const value = Math.round(startValue + (target - startValue) * progress);
                counter.textContent = String(value);
                if (progress < 1) {
                    requestAnimationFrame(step);
                }
            };

            requestAnimationFrame(step);
        });
    }

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const item = entry.target;
                item.classList.add('is-visible');
                obs.unobserve(item);
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '0px 0px -8% 0px'
    });

    revealItems.forEach((item, index) => {
        item.style.transitionDelay = `${Math.min(index, 16) * 40}ms`;
        observer.observe(item);
    });

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    window.addEventListener('scroll', () => {
        handleScroll();
    }, { passive: true });

    window.addEventListener('resize', () => {
        if (window.innerWidth > 980) {
            setMenuState(false);
        }
    });

    handleScroll();
    animateCounters();
    updateActiveLink();
});
