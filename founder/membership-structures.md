# Membership card: joining fee and minimum spend structures

The card is a stored-value (prepaid) card that only works at this café. Every
structure below has three parts you set:

- **Joining fee (J):** paid once to become a member. Not spendable on food.
- **Load (L):** money put onto the card. Spendable on food and drinks.
- **Minimum spend (M):** what a member must spend in a period to stay active.

All rupee figures below are **placeholders to show how the maths works**, not
recommendations. Real figures come from `/founder-cfo` (your costs) and
`/founder-consumer` + `/founder-pricing` (what buyers will pay).

---

## The six structures

### A. Joining fee + first load
Pay J (non-refundable) and load at least L to start. Renew yearly.
- e.g. J = ₹5,000, first load ≥ ₹10,000, renewal ₹2,500/yr
- Good for: real exclusivity and upfront cash to help pay for building the café.
- Risk: the fee is the biggest barrier for the 19–25 group.

### B. Fully redeemable ("your fee is your credit")
There is no separate fee: you load L and all of it is credit to spend, plus member
perks. Exclusivity comes from limited seats or an invite, not price.
- e.g. load ₹10,000 = ₹10,000 credit + member-only events
- Good for: easiest yes, and the cash still arrives upfront.
- Risk: weaker filter, and a lower sense of being exclusive.

### C. Bonus tiers (load more, get more)
A small joining fee. Bigger loads earn bonus credit.

| Tier | Load | Bonus | Credit |
|---|---|---|---|
| Seed | ₹5,000 | 0% | ₹5,000 |
| Sapling | ₹15,000 | 7% | ₹16,050 |
| Tree | ₹30,000 | 12% | ₹33,600 |
| Forest | ₹60,000 | 18% | ₹70,800 |

- Good for: pulls cash forward, and gives a natural ladder that fits the green theme.
- Risk: bonuses cut margin. Keep the bonus below your gross margin (see the formula).

### D. Monthly minimum spend
Members must spend M per month (or per quarter). Any shortfall is deducted from the
balance or charged.
- e.g. M = ₹1,500/month; spend ₹900 and ₹600 is deducted
- Good for: predictable revenue, and members actually turn up.
- Risk: feels like a penalty. A quarterly minimum is gentler than a monthly one.

### E. Founding members (capped)
The first N members (e.g. 200) pay a higher J and get lifetime perks: a locked
price, a name on the founders' wall, priority events, a guest pass.
- Good for: raising build money before you open, and creating real scarcity.
- Risk: you must actually deliver the lifetime perks. Cost them with `/founder-cfo`.

### F. Segment tiers for a 19–46 age range
One card does not fit both a 20-year-old student and a 42-year-old professional.
- **Student / Creator (19–25):** low J, low M, off-peak hours only
- **Individual:** standard J and M
- **Duo / Family:** one card with 2–4 users, higher M, lower J per person
- **Corporate / Studio:** a company pays for 5+ cards (and can book the space for meetings)

**Practical combinations:** E to launch and raise money, then C + F for normal
membership, with D as a gentle **quarterly** minimum.

---

## How to work out your own numbers

### 1. Capacity: how many members can the land hold?
```
Area for seats            = total area × share used for seating   (500 sq yd ≈ 4,500 sq ft)
Seats                     = seating area ÷ sq ft per seat            (garden café: ~15–20 sq ft)
Visits per day            = seats × table turns per day
Max active members        = visits per day × 30 ÷ visits per member per month
```
Example: 60% seating → 2,700 sq ft ÷ 18 = 150 seats × 3 turns = 450 visits/day
→ 13,500/month ÷ 6 visits per member = **about 2,250 member capacity**. Cap
membership well below this (for example 800–1,200) to keep it exclusive and
uncrowded.

### 2. Minimum spend: what must each member spend?
```
Break-even sales / month  = fixed costs per month ÷ gross margin %
Minimum spend M (monthly) = break-even sales ÷ expected active members
```
Example: fixed costs ₹6,00,000/month (rent or land cost, staff, power, upkeep) and
a 65% gross margin (after food cost) → ₹9,23,000 sales/month. With 500 active
members, **M ≈ ₹1,850/month** just to break even. Set M at or a bit below this, and
count on walk-in guests and events for profit.

### 3. Joining fee: what should it recover?
```
J = (startup cost you want members to fund) ÷ number of members in year 1
```
Example: you want members to fund ₹40 lakh of a ₹1 crore build, and expect 400
founding members → **J ≈ ₹10,000**. If that is too high for your buyers, lower the
share funded by members or raise the member count.

### 4. Bonus ceiling (for structure C)
```
Max bonus % < gross margin % − target profit margin %
```
With a 65% gross margin and a target of 20% profit after fixed costs, bonuses
above about 15–20% start eating profit.

### 5. Breakage (unspent balance)
Some loaded money is never spent. **Do not plan profit on it.** Treat it as a
bonus, and set clear expiry and refund rules in the member terms.

---

## Before you finalise: check with a CA / lawyer (India)
- Prepaid cards used **only at your own business** are generally a "closed system"
  instrument and fall outside RBI prepaid-wallet licensing. Confirm this for your
  exact card design, especially if you ever allow cash-out or use at partner shops.
- GST on the joining fee and on loaded balances (vouchers) is treated differently
  from GST on café sales. Get the treatment confirmed before printing prices.
- Write member terms covering expiry, refunds, transfer, minimum-spend deductions
  and what happens to the balance if the café closes.
