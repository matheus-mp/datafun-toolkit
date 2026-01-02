# Troubleshooting

Common questions and issues when using `datafun_toolkit`.

## Why does the log file appear in the project root?

This is intentional.

WHY:
- Makes logs easy to find
- Keeps paths consistent across machines
- Avoids writing to user-specific locations

## Why do logs not show usernames or full paths?

This toolkit intentionally sanitizes output.

WHY:
- Protect student privacy
- Make logs safe to share publicly
- Reduce noise in grading and debugging

## Why does detect_shell() return "unknown"?

Shell detection is heuristic.

OBS:
- Some terminals do not expose identifying environment variables.
- In these cases, returning "unknown" is expected and acceptable.

## Does this toolkit collect or transmit data?

No.

OBS:
- All functions run locally and return strings only.
- No network calls, telemetry, or persistent identifiers are used.

## Should students modify this package?

No.

WHY:
- This toolkit is intended to be imported as-is.
- Students should focus on their project code, not infrastructure utilities.
