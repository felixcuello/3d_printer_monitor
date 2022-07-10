# 3D Printer Monitor

## Introduction

The following software has been developed to monitor a 3D FDM system by using different tools.

The goal is to replace a human to monitor 3D FDM printers, so you can leave them unattended and receive notifications if something is wrong and has to be adjusted.

## Installation

All the services runs inside a docker container with the exception of the capturing software that runs natively, so you have to set up your environment properly in order to make it to work.

The biggest requirement is docker because everything runs dockerized. However the capture software will require to install some native libraries in order to work.

The `./media` directory is shared among all the services, so be careful with this directory.


## All the services (except the `capture` service)

You can just execute `make` (so the `make` command is a prerrequisite) if it's the first time.

If you have your images already built you can just run `make up`

## Capture

For the capture service you can run `make macos_prerequisites` and `make capture_up`


## Architecture

The following diagram is an example architecture described in this software. All the services (except the capturing software) are dockerized.

![Architecture](./docs/architecture.png)

