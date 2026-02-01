
---

# Disclaimers

This process can be replicated in VS Code on Windows.

This configuration involves PNPM, Vite, React, Typescript, and Docker.

---

# Required Tools

- Docker Desktop
- PNPM

---

# Creating a New Project

Enter the folder where you want to create your new project folder.

Run the following command.

```
pnpm create vite@latest
```

Provide the following options:
- Project name:
	- your-project-name-kebab-case
- Select a framework:
	- React
- Select a variant:
	- TypeScript

---

Enter your newly created project folder

```
cd your-project-name-kebab-case
```

---

# Initialize Dependencies

---


```
pnpm install
```

You may need to approve some builds. If that's the case, you will be prompted to run the following command:

```
pnpm approve-builds
```

---

# Additional Dependencies

Once again, you may need to run `pnpm approve-builds` after adding any of the following dependencies to your project.

---

## React Router

```
pnpm add react-router react-router-dom
```

```
pnpm add @types/react-router @types/react-router-dom -D
```

---

## SCSS

```
pnpm add sass -D
```

---

# Alias Configuration

There are three TypeScript configuration files:
- `tsconfig.app.json`
- `tsconfig.json`
- `tsconfig.node.json`

---

In both `tsconfig.app.json` and `tsconfig.node.json`, add the following code in the object:

``` json
"extends": "./tsconfig.json"
```

---

In `tsconfig.json`, add the following code in the object:

``` json
"compilerOptions": {
	"baseUrl": ".",
	"paths": { "@/*": ["src/*"] }
}
```

---

In `vite.config.ts`, add the following code:

``` ts
resolve: { alias: { "@": "/src" } }
```

Now, `vite.config.ts` should look like this:

``` ts
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
	 plugins: [react()],
	 resolve: { alias: { "@": "/src" } }
})
```

---

# HTML File

Update the content of the `title` element to be the name of your app, which will appear in your browser as the name of any tabs running your application

Find the `link` element that with an attribute of `rel=icon` and update the value of the `type` attribute to be the logo of your app, which will appear in your browser as the favicon of any tabs running your application.

---

# Docker

Create the following files in the top level of your project folder:
- `Dockerfile`
- `docker-compose.yaml`
- `.dockerignore`

---

## Dockerfile

``` Dockerfile
# Dockerfile
FROM node:20-alpine

# Create app directory
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy files
COPY . .

# Install dependencies
RUN pnpm install

# Expose dev server port
EXPOSE 5173

# Start Vite dev server
CMD ["pnpm", "run", "dev"]
```

---

## docker-compose.yaml

``` yaml
services:
  web:
    build: .
    ports:
      - "5173:5173"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - CHOKIDAR_USEPOLLING=true
    command: pnpm run dev
```

---

## .dockerignore

```
node_modules
dist
.git
.vscode
.env
```

---

# Server

In `vite-config.ts`, add the following code:

``` ts
server: {
  host: true,
  port: 5173
}
```

That code is necessary when you want to start your application with docker.

---

# Router

Create a folder called `router` in the `src` folder.

Create the following files in the `router` folder:
- `client-paths.ts`
- `client-routes.tsx`
- `client-router.tsx`

---

## Client Paths

Create a file called `client-paths.tsx` in the `router` folder.

``` ts
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

export type ClientPaths = {
  ROOT: string
}

export const CLIENT_PATHS: ClientPaths = {
  ROOT: "/"
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

---

## Client Routes

Create a file called `client-routes.tsx` in the `router` folder.

``` tsx
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import type { RouteObject } from "react-router-dom"
import { CLIENT_PATHS } from "./client-paths"

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

export type ClientRoutes = {
  ROOT: RouteObject
}

export const CLIENT_ROUTES: ClientRoutes = {
  ROOT: {
    path: CLIENT_PATHS.ROOT,
    element: null
  }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

---

## Client Router

Create a file called `client-router.tsx` in the `router` folder.

``` tsx
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import { createBrowserRouter } from "react-router-dom"
import { CLIENT_ROUTES } from "./client-routes"

export const CLIENT_ROUTER = createBrowserRouter([...Object.values(CLIENT_ROUTES)])

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

---
# Default Source Files

There should be four files in the top level of the `src` folder:
- `App.css`
- `App.tsx`
- `index.css`
- `main.tsx`

---

Delete `index.css` and replace it with `index.scss`.
`index.scss` should contain all of the basic styles for your app, which may include:
- `:root {}`
- `* {}`
- any vanilla elements
	- `html`
	- `body`
	- `div`
	- `h1`, `h2`, `h3`, `h4`, `h5`, `h6`
	- `p`
	- `span`
	- `button`
	- `input`
	- `ol`, `ul`, `li`
	- `nav`
	- `a`
	- `...`
- any custom elements from `index.html`
	- `#root`

---

Update `main.tsx` so that it imports `index.scss` rather than `index.css`.

`main.tsx` should look something like this:

``` tsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import './index.scss'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

---

Delete `App.css`

---

Update `App.tsx` to be a simple application container, which could look something like this:

``` tsx
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import { RouterProvider } from "react-router-dom"
import { CLIENT_ROUTER } from "./router/client-router"

export default function App() {
  return (
    <RouterProvider router={CLIENT_ROUTER} />
  )
}
  
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

---

# Starting & Stopping Your Application

---

## PNPM

- `pnpm run dev`
	- starts your application in development mode
	- press `CTRL + C` to stop your application

---

## Docker

Docker Desktop must be open and running.

- `docker compose up`
	- runs your containers in the background
	- press `CTRL + C` twice to stop your application

- `docker compose up --build`
	- rebuilds your images
	- runs containers in the background
	- press `CTRL + C` twice to stop your application

- `docker compose up -d`
	- runs your containers in the foreground
	- run `docker compose down` to stop your application

- `docker compose up --build -d`
	- rebuilds your images
	- runs your containers in the foreground
	- run `docker compose down` to stop your application

---

# Git

Initialize your project as a git repository and make an initial commit with an arbitrary message.

```
git init
```

```
git add .
```

```
git commit -m "New Project Configured"
```

---
