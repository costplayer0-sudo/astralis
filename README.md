# ✦ Astralis — Constellation Sigils (Paper plugin)

Every player is awakened beneath a **constellation** and carries its **sigil**. Right-click for an ability, build **Stardust**
by fighting, then unleash your **Zenith**. Five constellations form a rock-paper-scissors **counter ring**; two rare
**Mythicals** sit outside it and are only won in server events.

Targets **Paper 1.21.x**, Java 21. Build: `mvn package` → `target/Astralis-1.0.0.jar` → drop into `plugins/`.
(If your server is newer, change `<paper.version>` in `pom.xml`.)

## Controls
| Input | Effect |
|---|---|
| Right-click (sigil in main hand) | Primary ability (cooldown) |
| Sneak + right-click, or **F** (swap hands) | **Zenith** (costs Stardust) |
| Stellar Core in main hand + Dim sigil in off-hand, right-click | Ascend to **Radiant** |

## The constellations
Ring: **Aries > Orion > Draco > Cassiopeia > Gemini > Aries** (+10% damage vs prey, −10% vs predator; configurable).

| | Passive | Right-click | Zenith |
|---|---|---|---|
| **Aries** (Ram) | Sprint hits hit harder + knock back | Rampart Charge: dash, shatters shields | Worldbreaker Horn: travelling fissure launches enemies |
| **Orion** (Hunter) | Bonus arrow damage | Starpiercer Beam: piercing, marks targets (+dmg from you, glowing) | Hunter's Volley: star-arrow rain where you aim |
| **Draco** (Dragon) | Fire resistance | Ember Breath: flame cone | Wyrmfall: soar, then shockwave dive |
| **Cassiopeia** (Queen) | Resistance when badly hurt | Starlit Aegis: absorption + reflects melee | Crown of Gravity: pulling slow-field, then collapse |
| **Gemini** (Twins) | Chance to dodge melee, then speed | Mirror Step: blink, afterimage detonates & pulls | Twin Echo: every melee hit repeats |
| **Phoenix** (Reborn) — *Mythical* | Cheats a killing blow (long cooldown) | Cinder Wings: fiery surge | Rebirth Nova: cleanse, heal, burst |
| **Andromeda** (Chained) — *Mythical* | Slow/weakness wear off fast | Astral Chains: yank + root first target | Constellation Prison: star cage, holds prisoners in |

**Stardust** fills from damage dealt/taken (mobs at 25%), kills, and Starfall shards. **Radiant** tier: stronger, shorter cooldowns, cheaper Zenith.

## Sigil rules (the "lose it and someone can take it" layer)
* PvP death → sigil drops as a glowing beacon, announced server-wide. Non-PvP death → you keep it.
* Max 2 carried; only the best one's passive is active. A sigil that isn't yours is **unattuned** (×0.75 power).
* Sigils can't go in chests/hoppers/frames, can't be renamed or crafted with.
* `/astralis trust <player>`: your abilities never hurt them.

## Events (`/astralis event ...`)
| Event | What happens |
|---|---|
| **starfall** | Stars crash near players; collect **Stardust Shards** (+20 Stardust) |
| **convergence** | King-of-the-hill. Hold the marked zone *alone* for 90s to win a **Mythical sigil** (contested = paused) |
| **eclipse** | Everyone's Stardust gain is multiplied (×2) |

Admins: `/astralis event start <starfall|convergence|eclipse> [minutes]`, `/astralis event stop`.
Anyone: `/astralis event status|locate|list`. Optional automatic events: `events.auto.enabled: true`.

## Commands
Player: `help`, `info [constellation]`, `stats [player]`, `trust|untrust <player>`, `trusted`, `event status|locate|list`

Admin (`astralis.admin`): `give <player> <constellation> [dim|radiant]`, `core <player> [n]`, `tier <player> <dim|radiant>`,
`remove <player> [constellation]`, `awaken <player> [constellation]`, `reroll <player>`,
`energy <player> set|add|take|max|reset [n]`, `cooldown <player>`, `cast <player> primary|ultimate`, `holders`,
`event start|stop`, `reload`, `selftest`.  Aliases: `/sigil`, `/as`.

## Configuration
Everything numeric lives in `config.yml` and reloads with `/astralis reload`. Key dials: `general.ability-damage-scale`,
`counter-ring.bonus/penalty`, `tiers.*`, `stardust.*`, per-ability numbers under `constellations.*`, and `events.*`.

## Balance & testing — what was and wasn't checked
* **Compiled** against stand-in API stubs: zero errors. **111 behaviour checks pass** (`bash tools/simulation/run.sh`): commands, ring math,
  dodge rate (measured 10.0% at 10% config), reflect/echo/mark, death/pickup rules, storage protection, Stellar Core ascension,
  all 7 kits animating frame-by-frame, all 3 events end-to-end. It found and fixed a real bug (orphan Starfall shard after an event ended).
* **Balance Monte Carlo** (coarse 1v1 model driven by `config.yml`): initial config had Phoenix ~92% and Cassiopeia ~82% average win
  rate; retuned to ring members **42–54%**, Phoenix ~59%, Andromeda ~48%. Counter matchups land ~75–80% (intended).
  This is a relative signal for outliers, **not** a prediction of real PvP — playtest and adjust.
* **Not verified:** the real Paper API itself (no network here). If the first `mvn package` fails, it will be a renamed API
  method/constant. Most likely suspects: `Player#clearActiveItem`, `Player#setCooldown(Material,int)`, `Bukkit#getOfflinePlayerIfCached`,
  `Item#setUnlimitedLifetime`, `PlayerDeathEvent#getItemsToKeep`, `ItemMeta#setMaxStackSize`, and a few `Particle`/`Sound` constants.
  Send the error and it's a one-line fix.

## Layout
`src/main/java/com/astralis/` — `core/` (managers, damage, sigils), `kit/` (one class per constellation), `event/`, `listener/`,
`command/`, `fx/`, `task/`.  `tools/simulation/` — the test harness.  `ALL_CODE.txt` — every source file in one paste-able file.
