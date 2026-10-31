(function () {
  var SB = 'https://whbirxvvwmzyhjjiihhp.supabase.co/rest/v1/';
  var KEY = 'sb_publishable_2J47TXTa9-8BFWIWE029fw_7ONKbxy3';

  var menu = document.querySelector('.menu');
  var nav = document.querySelector('.nav');
  if (menu && nav) menu.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    menu.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  function send(table, row) {
    return fetch(SB + table, {
      method: 'POST',
      headers: { apikey: KEY, 'Content-Type': 'application/json', Prefer: 'return=minimal' },
      body: JSON.stringify(row)
    }).then(function (r) { if (!r.ok) throw new Error(r.status); });
  }

  function wire(form, table, build, okText, after) {
    if (!form) return;
    var msg = form.querySelector('.msg');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input').value) return; // bot trap
      var btn = form.querySelector('button');
      btn.disabled = true; msg.className = 'msg'; msg.textContent = 'Sending…';
      send(table, build(new FormData(form))).then(function () {
        msg.className = 'msg ok'; msg.textContent = okText; form.reset();
        if (after) after();
      }).catch(function () {
        msg.className = 'msg err';
        msg.innerHTML = 'Something went wrong. Please try again, or email <a href="mailto:psiproslab@gmail.com">psiproslab@gmail.com</a>.';
      }).then(function () { btn.disabled = false; });
    });
  }

  wire(document.getElementById('lead-form'), 'site_leads', function (d) {
    return { email: String(d.get('email')).trim(), consent_marketing: true, source: 'humming-reset' };
  }, 'Thank you. Opening your humming reset…', function () {
    setTimeout(function () { location.href = '/reset/'; }, 900);
  });

  wire(document.getElementById('booking-form'), 'booking_requests', function (d) {
    var reason = String(d.get('reason') || '').trim();
    return {
      name: String(d.get('name')).trim(),
      email: String(d.get('email')).trim(),
      country: String(d.get('country')).trim(),
      reason: reason || null,
      consent_privacy: true,
      consent_health: !!d.get('consent_health')
    };
  }, 'Thank you. Pros will email you within two working days to schedule your free 20-minute call.');

  // health-info consent is only required when a reason is filled in
  var bf = document.getElementById('booking-form');
  if (bf) {
    var r = bf.querySelector('[name=reason]'), c = bf.querySelector('[name=consent_health]');
    var sync = function () { c.required = r.value.trim().length > 0; };
    r.addEventListener('input', sync); sync();
  }
})();
