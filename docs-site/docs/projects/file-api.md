---
# Presentation layer
title: "File API Overview"
description: "Description of ideas, frameworks, and prompts used to create the File API portfolio project."
date: "2026-03-20"
author: "Jeremiah Michaels"

# Semantic layer
description: "Project notes for the creation for the File API resume project."
ai-summary: "Covers idea to output for the project."
topics: ["api development", "security", "documentation", "modern python frameworks"]
keywords: ["api", "documentation"]
entities: ["claude", "fastapi", "python", "yml"]
audiences: "recruiters"
complexity: "intermediate"
language: "python"

# Graph layer
parent_topic:
related_ids:
content_stage:
---

# Idea

The idea for the `file-api` is to showcase my API documentation abilities. I used `claude desktop` to code a locally hosted API that I could generate an OpenAPI spec from and deploy with the Swagger UI.

I wanted a secure location since the API is exposed to the internet.

## Frameworks

I used `python` and `fastapi` for the framework. I wanted something that was easy to create and deploy. `fastapi` create a `yml` file by default.

## Prompt

I first prompted `claude desktop` about what my goal was. I asked what would be the easiest to do, and why. I was presented with three options, but the end of the output suggested that I use the `python` \ `fastapi` combo since it accomplished my goals and was the most straightforward.

Then I prompted my ideas for two functions, one to download a `txt` file from a folder, with the folder name as a required input parameter. The second function provides a list of files in a folder, with the folder name as a required parameter. 

I made sure to add that I wanted the highest level of security since I would be testing the endpoints on my local when it's connected to the internet.

## The Result

[File API](https://jeremiah-michaels.github.io/resume/)