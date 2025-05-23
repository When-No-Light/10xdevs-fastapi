import { OpenAPI } from "src/client";

if (process.env.PROXY_URL === undefined) {
    throw new Error("PROXY_URL is undefined");
}

OpenAPI.BASE = process.env.PROXY_URL;
