# resin-scroll-bot

Displays a Cryptocurrency ticker on a [Pimoroni Scroll Bot - Pi Zero W Project Kit](https://shop.pimoroni.com/products/scroll-bot-pi-zero-w-project-kit), using a [rust command line tool](https://github.com/josephroberts/cryptocurrency-tracker) to get the Cryptocurrency data.

![demo](https://github.com/josephroberts/resin-scroll-bot/blob/master/demo.gif "demo")

## Getting started

 - Sign up on [resin.io](https://dashboard.resin.io/signup)
 - Work through the [getting started guide](https://docs.resin.io/raspberrypi/python/getting-started/)
 - Clone this repository to your local workspace
 - Create a new application
 - Add the application `resin remote` to your local workspace
 - Provision a Pi Zero W
 - Git push to resin

## Configuration variables

The behaviour must be configured with the following [environment
variables](https://docs.resin.io/management/env-vars/):

Environment Variable | Description
------------ | -------------
brightness | Set the display brightness (float between `0` and `1`, `0.5` works well)
rotation | Set the display rotation (integer between `0` and `360`, set to `180` for this project)
cryptos | Set the Cryptocurrencies to display (space separated list of symbols, for example `BTC ETH`)
format | Set the Cryptocurrency format (string consisting of values specified in the [coinmarketcap API](https://coinmarketcap.com/api/), for example `{symbol} {percent_change_24h}%`
