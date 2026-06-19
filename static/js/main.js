/* ─── main.js — TechSpace Programming Classes ─────────────────────── */
"use strict";

document.addEventListener("DOMContentLoaded", () => {

  /* ── 1. NAVBAR: Scroll effect + Hamburger + Drawer ─────────────── */
  const navbar   = document.getElementById("navbar");
  const hamburger= document.getElementById("hamburger");
  const drawer   = document.getElementById("mobileDrawer");
  const overlay  = document.getElementById("drawerOverlay");

  window.addEventListener("scroll", () => {
    navbar?.classList.toggle("scrolled", window.scrollY > 60);
    document.getElementById("scrollTop")?.classList.toggle("show", window.scrollY > 400);
  });

  function toggleDrawer(open) {
    hamburger?.classList.toggle("open", open);
    drawer?.classList.toggle("open", open);
    overlay?.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
  }
  hamburger?.addEventListener("click", () => toggleDrawer(!drawer.classList.contains("open")));
  overlay?.addEventListener("click", () => toggleDrawer(false));
  drawer?.querySelectorAll("a").forEach(a => a.addEventListener("click", () => toggleDrawer(false)));

  /* ── 2. SCROLL-TO-TOP ───────────────────────────────────────────── */
  document.getElementById("scrollTop")?.addEventListener("click", () => window.scrollTo({top:0,behavior:"smooth"}));

  /* ── 3. SMOOTH SCROLL for anchor links ─────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener("click", e => {
      const target = document.querySelector(a.getAttribute("href"));
      if (target) { e.preventDefault(); target.scrollIntoView({behavior:"smooth", block:"start"}); }
    });
  });

  /* ── 4. FADE-IN on scroll (IntersectionObserver) ───────────────── */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll(".fade-in").forEach(el => observer.observe(el));

  /* ── 5. COUNTER ANIMATION ───────────────────────────────────────── */
  function animateCounter(el, target, suffix = "") {
    let start = 0;
    const duration = 2000;
    const step = duration / 60;
    const increment = target / (duration / step);
    const timer = setInterval(() => {
      start += increment;
      if (start >= target) { start = target; clearInterval(timer); }
      el.textContent = Math.floor(start) + suffix;
    }, step);
  }

  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll("[data-count]").forEach(el => {
          const val    = parseInt(el.dataset.count);
          const suffix = el.dataset.suffix || "";
          animateCounter(el, val, suffix);
        });
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  const statsBar = document.querySelector(".stats-bar");
  if (statsBar) statsObserver.observe(statsBar);

  /* ── 6. STUDENTS CAROUSEL ───────────────────────────────────────── */
  function buildCarousel(trackId, prevId, nextId, cardWidth = 240, gap = 20) {
    const track = document.getElementById(trackId);
    if (!track) return;
    const prev = document.getElementById(prevId);
    const next = document.getElementById(nextId);
    let index = 0;
    const cards = track.children;
    const visibleCount = () => Math.floor(track.parentElement.offsetWidth / (cardWidth + gap));
    const maxIndex = () => Math.max(0, cards.length - visibleCount());

    function goTo(i) {
      index = Math.max(0, Math.min(i, maxIndex()));
      track.style.transform = `translateX(-${index * (cardWidth + gap)}px)`;
    }
    prev?.addEventListener("click", () => goTo(index - 1));
    next?.addEventListener("click", () => goTo(index + 1));

    // Auto-scroll
    let auto = setInterval(() => goTo(index >= maxIndex() ? 0 : index + 1), 3000);
    track.parentElement.addEventListener("mouseenter", () => clearInterval(auto));
    track.parentElement.addEventListener("mouseleave", () => {
      auto = setInterval(() => goTo(index >= maxIndex() ? 0 : index + 1), 3000);
    });
  }
  buildCarousel("studentsTrack", "studentsPrev", "studentsNext", 220, 20);

  /* ── 7. TESTIMONIALS CAROUSEL ───────────────────────────────────── */
  buildCarousel("testimonialsTrack", "testiPrev", "testiNext", 340, 24);

  /* ── 8. FAQ ACCORDION ───────────────────────────────────────────── */
  document.querySelectorAll(".faq-question").forEach(btn => {
    btn.addEventListener("click", () => {
      const item = btn.closest(".faq-item");
      const isOpen = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach(i => i.classList.remove("open"));
      if (!isOpen) item.classList.add("open");
    });
  });

  /* ── 9. BRANCH TABS ─────────────────────────────────────────────── */
  document.querySelectorAll(".branch-tab").forEach(tab => {
    tab.addEventListener("click", () => {
      const target = tab.dataset.branch;
      document.querySelectorAll(".branch-tab").forEach(t => t.classList.remove("active"));
      document.querySelectorAll(".branch-panel").forEach(p => p.classList.remove("active"));
      tab.classList.add("active");
      document.getElementById("branch-" + target)?.classList.add("active");
    });
  });

  /* ── 10. ENQUIRE NOW MODAL ──────────────────────────────────────── */
  function openModal(id) { document.getElementById(id)?.classList.add("open"); document.body.style.overflow = "hidden"; }
  function closeModal(id) { document.getElementById(id)?.classList.remove("open"); document.body.style.overflow = ""; }

  document.querySelectorAll("[data-modal-open]").forEach(btn =>
    btn.addEventListener("click", () => openModal(btn.dataset.modalOpen))
  );
  document.querySelectorAll("[data-modal-close]").forEach(btn =>
    btn.addEventListener("click", () => closeModal(btn.dataset.modalClose))
  );
  document.querySelectorAll(".modal-overlay").forEach(overlay =>
    overlay.addEventListener("click", e => { if (e.target === overlay) overlay.classList.remove("open"); document.body.style.overflow = ""; })
  );

  /* ── 11. ACTIVE NAV HIGHLIGHT on scroll ─────────────────────────── */
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-links a[href^='#']");
  const highlightNav = () => {
    let current = "";
    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - 100) current = sec.id;
    });
    navLinks.forEach(link => {
      link.classList.toggle("active", link.getAttribute("href") === "#" + current);
    });
  };
  window.addEventListener("scroll", highlightNav, { passive: true });

  /* ── 12. AUTO-DISMISS ALERTS ─────────────────────────────────────── */
  document.querySelectorAll(".alert").forEach(alert => {
    setTimeout(() => alert.style.opacity = "0", 4000);
    setTimeout(() => alert.remove(), 4500);
  });

  /* ── 13. FORM VALIDATION FEEDBACK ───────────────────────────────── */
  document.querySelectorAll("form").forEach(form => {
    form.addEventListener("submit", e => {
      const phone = form.querySelector("[name='phone']");
      if (phone && !/^[6-9]\d{9}$/.test(phone.value.replace(/\s/g, ""))) {
        e.preventDefault();
        phone.style.borderColor = "#dc2626";
        phone.focus();
        phone.setCustomValidity("Enter a valid 10-digit Indian mobile number");
        phone.reportValidity();
      }
    });
  });

});
