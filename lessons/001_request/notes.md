# 001 – Making a Request

## Key ideas
- `load_dotenv()` loads `ANTHROPIC_API_KEY` from `.env`; `Anthropic()` reads it automatically.
- `client.messages.create(model, max_tokens, messages)` sends a request.
  - `max_tokens` is a cap on reply length, not a target.
  - `messages` is a list of `{"role": "user" | "assistant", "content": ...}`.
- The reply text is in `message.content[0].text` (`content` is a list of blocks).
- `stop_reason`: `end_turn` = finished, `max_tokens` = cut off.
- `usage` shows input/output tokens (what you pay for).

## My notes
-

## Questions
-
