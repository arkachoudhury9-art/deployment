import os

import uvicorn

if __name__ == "__main__":
    config = uvicorn.Config(
        "backend.main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", "8000")),
        reload=False,
        log_level="info",
    )
    server = uvicorn.Server(config)
    server.run()
