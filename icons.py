"""House illustration set for psiproslab: one style (round line art, navy stroke, one green accent).
All drawn for this site, so no licence issues."""

_P = {
    # sections
    "blocks": '<rect x="9" y="9" width="13" height="13" rx="3"/><rect x="26" y="9" width="13" height="13" rx="3" class="a"/><rect x="9" y="26" width="13" height="13" rx="3"/><rect x="26" y="26" width="13" height="13" rx="3"/>',
    "exercises": '<rect x="11" y="8" width="26" height="32" rx="4"/><path d="M17 19l3 3 6-6" class="s"/><path d="M17 30h14"/>',
    "brain-sleep": '<path d="M30 9a13 13 0 1 0 9 22A11 11 0 0 1 30 9z"/><circle cx="35" cy="13" r="2.4" class="a"/>',
    # building blocks
    "abc-model": '<text x="24" y="30" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor" stroke="none" font-family="Inter,sans-serif">ABC</text><path d="M10 36h28"/><circle cx="38" cy="36" r="2.4" class="a"/>',
    "three-brains": '<path d="M12 34a12 12 0 0 1 24 0"/><path d="M16 34a8 8 0 0 1 16 0"/><path d="M20 34a4 4 0 0 1 8 0" class="s"/><circle cx="24" cy="34" r="2" class="a"/>',
    "instinct-is-faster": '<path d="M27 7L14 26h9l-3 15 14-21h-9z" class="af"/>',
    "emotion-takes-over": '<path d="M24 38s-13-7.5-13-17a7 7 0 0 1 13-3.6A7 7 0 0 1 37 21c0 9.5-13 17-13 17z"/><path d="M15 24h5l2-4 3 8 2-4h6" class="s"/>',
    "white-bear-effect": '<circle cx="15" cy="15" r="4"/><circle cx="33" cy="15" r="4"/><circle cx="24" cy="27" r="12"/><circle cx="20" cy="25" r="1.3" class="a"/><circle cx="28" cy="25" r="1.3" class="a"/><path d="M22 31h4"/>',
    "emotional-bucket": '<path d="M11 15h26l-3 24H14z"/><path d="M12.5 25c4 2.5 8 -2.5 11.5 0s8 2.5 11.5 0" class="s"/><path d="M16 15a8 8 0 0 1 16 0"/>',
    "clogged-engine": '<circle cx="24" cy="24" r="6"/><path d="M24 9v5M24 34v5M9 24h5M34 24h5M13.4 13.4l3.5 3.5M31.1 31.1l3.5 3.5M13.4 34.6l3.5-3.5M31.1 16.9l3.5-3.5"/><circle cx="24" cy="24" r="2" class="a"/>',
    "relief-reward": '<path d="M10 24h20"/><path d="M24 17l7 7-7 7"/><path d="M36 12l1.5 3 3 .5-2.2 2.1.5 3-2.8-1.5-2.8 1.5.5-3L31.5 15.5l3-.5z" class="af"/>',
    "tipp": '<path d="M24 8s-11 12-11 20a11 11 0 0 0 22 0c0-8-11-20-11-20z"/><path d="M19 29a5 5 0 0 0 5 5" class="s"/>',
    # exercises
    "quitting-smoking": '<rect x="8" y="22" width="28" height="7" rx="2"/><path d="M30 22v7"/><path d="M39 22c0-3-3-3-3-6" class="s"/><path d="M10 38L38 10" class="s"/>',
    "beating-procrastination": '<circle cx="24" cy="25" r="14"/><path d="M24 17v8l5 4"/><path d="M20 7h8"/><circle cx="24" cy="25" r="2" class="a"/>',
    "limitless-wish-list": '<path d="M24 8l4.7 9.6 10.6 1.5-7.7 7.5 1.8 10.5L24 32.1l-9.4 5 1.8-10.5-7.7-7.5 10.6-1.5z"/><circle cx="24" cy="24" r="2.4" class="a"/>',
    # brain & sleep: basics
    "sleep": '<path d="M30 9a13 13 0 1 0 9 22A11 11 0 0 1 30 9z"/><path d="M33 13h5l-5 5h5" class="s"/>',
    "move": '<circle cx="28" cy="10" r="3.2" class="a"/><path d="M19 22l6-6 5 5 6 1"/><path d="M25 16l-3 12-7 9"/><path d="M22 28l7 4 2 7"/>',
    "eat": '<path d="M12 36C12 20 24 10 38 10c0 16-10 26-26 26z"/><path d="M12 36l16-16" class="s"/>',
    "focus": '<circle cx="24" cy="24" r="14"/><circle cx="24" cy="24" r="8"/><circle cx="24" cy="24" r="2.6" class="a"/>',
    # brain & sleep: supplements
    "melatonin": '<path d="M28 9a12 12 0 1 0 8 20A10 10 0 0 1 28 9z"/><path d="M8 38h32" /><path d="M14 38v-4M24 38v-6M34 38v-4" class="s"/>',
    "creatine": '<rect x="9" y="16" width="27" height="16" rx="3"/><path d="M36 21h3v6h-3"/><rect x="13" y="20" width="12" height="8" rx="1" class="af"/>',
    "l-theanine": '<path d="M10 20h22v8a11 11 0 0 1-22 0z"/><path d="M32 22h3a4 4 0 0 1 0 8h-3"/><path d="M18 14c0-3 3-3 3-6M24 14c0-3 3-3 3-6" class="s"/>',
    "omega-3": '<path d="M8 24c6-8 16-10 24 0-8 10-18 8-24 0z"/><path d="M32 24l8-6v12z"/><circle cx="15" cy="22" r="1.6" class="a"/>',
    "lions-mane": '<path d="M9 24a15 12 0 0 1 30 0z"/><path d="M19 24v13h10V24"/><path d="M14 18v3M20 15v4M26 14v4M32 17v3" class="s"/>',
    "peptides": '<path d="M18 8h12"/><path d="M20 8v8l-8 18a3 3 0 0 0 3 4h18a3 3 0 0 0 3-4l-8-18V8"/><path d="M16 30h16" class="s"/>',
}


def icon(key, size=40):
    return (f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 48 48" aria-hidden="true" fill="none" '
            f'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{_P[key]}</svg>')
