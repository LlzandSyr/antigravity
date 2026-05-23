# Scratchpad for Antigravity Quota Math Verification

## Checklist
- [x] Search Google and Reddit for discussions about Varun Mohan's tweets and the "9x" quota claim.
- [/] Find specific developer discussions, threads, or posts calculating the 3x rate limit * 3x weekly quota math.
- [ ] Extract user names, thread titles, quotes, and URLs showing technical consensus/frustration over the "9x" marketing claim vs actual capacity.
- [x] Document findings in this scratchpad.
- [ ] Provide final summary to the user.

## Findings

### Official Twitter/X Announcements by Varun Mohan (DeepMind):
1. **First Tweet (May 21, 2026):**
   - **Content:** *"An update: we're 3xing the rate limits for Gemini models across all paid tiers in Antigravity and resetting everyone's Gemini quota for the week. We understand some people hit their rate limits quickly and wanted to respond fast."*
   - **Key Detail:** The first update was specifically tripling **rate limits** (burst limits/speed).

2. **Second Tweet (8:25 AM · May 22, 2026):**
   - **Content:** *"Yesterday, we 3x’d limits on Antigravity and are seeing you build so much more. One thing we heard was people are worried about hitting their weekly limits after a couple work sessions. To give you more runway, we’re 3x’ing the weekly Gemini quotas AGAIN on all paid plans. We’ve also gone ahead and reset Gemini quotas on all paid plans."*
   - **Key Detail:** The second update was tripling **weekly Gemini quotas** (total capacity).

### Media Hype:
- **Android Authority Article:** *"Google gives Antigravity users another major Gemini quota boost as backlash refuses to die down"* by Shimul Sood (May 22, 2026)
- **URL:** https://www.androidauthority.com/gemini-antigravity-limits-increased-3670209/
- **Quote:** *"If you’re keeping count, that effectively works out to a massive 9x increase compared to where limits landed after the original nerf."*
- **Mathematical Fallacy:** The "9x increase" is indeed the product of multiplying the 3x rate limit increase by the 3x weekly quota increase (3 * 3 = 9x). However, this is a throughput capacity calculation, not 9x more actual weekly token usage capacity (which is only 3x).

### Developer Discussions & Consensus (Reddit):

Developers in the `r/google_antigravity` community immediately recognized the marketing spin and calculated the actual math, showing that the weekly quota is only 3x of the nerf limit, while the "9x" is a throughput capability calculation.

1. **Thread:** *"Additional 3x increase of Gemini in Antigravity!"* (May 22, 2026 - 190+ comments)
   - **User `gotoariel`:**
     - **Quote:** *"Thanks! So not it's 9x of original? Or 1x+3x+3x= 7x original quota? The problem though is the 7 day refresh.. It's way too long."*
   - **Developer Quote:**
     - **Quote:** *"this is a marketing stunt at best, just like codex team does. resetting limits and increasing caps does not matter because we dont know the actual usage. you can say 100x and we cant even know that for ..."*
   - **URL:** https://www.reddit.com/r/google_antigravity/comments/1tk6vu7/additional_3x_increase_of_gemini_in_antigravity/

2. **Thread:** *"3x More Gemini for Antigravity Users"* (May 21, 2026 - 230+ comments)
   - **User `Z33PLA`:**
     - **Quote:** *"... or some marketing spin from the previous comms email. Honestly, this makes me happy. Thank you Google for being logical here."*
   - **URL:** https://www.reddit.com/r/google_antigravity/comments/1tjawn4/3x_more_gemini_for_antigravity_users/

3. **Thread:** *"3X usage for Gemini models for all AI Plus, Pro, and Ultra..."* (May 21, 2026 - 160+ comments)
   - **Developer Quote:**
     - **Quote:** *"Saw the 3x limit and thought 'that's good'. Then proceeded to max out my limit within 2 hours on a few simple prompts, having never hit my limit..."*
   - **URL:** https://www.reddit.com/r/google_antigravity/comments/1tjbd1e/3x_usage_for_gemini_models_for_all_ai_plus_pro/

### Conclusion & Technical Consensus:
The developer community's reactions confirm the explanation:
- **Weekly Capacity:** Tripled once (3x).
- **Burst Limits / Speed:** Tripled once (3x).
- **The "9x" Hype:** A multiplication of speed (3x) by weekly capacity (3x) to claim a "9x total system capacity increase", which is highly misleading because developers cannot write 9x more code in a week; they can only write 3x more code but at 3x the speed (which causes them to max out the limit 3x faster, as experienced by users).
