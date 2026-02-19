import sentry_sdk

sentry_sdk.init(
    dsn="https://3e5f3ee43e9d3af60317460772347a37@o4510914236579840.ingest.us.sentry.io/4510914258665472",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

print("Hello, Sentry!")

numerator = 1
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError:
    result = None
    print("Warning: NN Division by zero avoided. Result set to None.")

print(f"Result: {result}")