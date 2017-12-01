[![POGODEV](https://github.com/pogodevorg/assets/blob/master/public/img/logo-github.png?raw=true)](https://pogodev.org)

# pgoapi - a pokemon go api lib in python [![Build Status](https://travis-ci.org/pogodevorg/pgoapi.svg?branch=develop)](https://travis-ci.org/pogodevorg/pgoapi)

pgoapi is a client/api/demo for Pokemon Go by https://github.com/tejado & https://github.com/pogodevorg.
It allows automatic parsing of requests/responses by finding the correct protobuf objects over a naming convention and will return the response in a parsed python dictionary format.   

## Disclaimers

 * This is unofficial - **USE AT YOUR OWN RISK**!
 * Botting or farming is **not supported**.

## Features

 * Python 2 and 3
 * Google/PTC auth
 * Address parsing for GPS coordinates
 * Allows chaining of RPC calls
 * Re-auth if ticket expired
 * Check for server side-throttling
 * Thread-safety
 * Advanced logging/debugging
 * Uses [POGOProtos](https://github.com/AeonLucid/POGOProtos)
 * Most RPC calls are available (see [API reference](https://docs.pogodev.org) on the wiki)

## Documentation
Documentation is available at the github [pgoapi wiki](https://wiki.pogodev.org).

## Requirements
 * Python 2 or 3
 * requests
 * protobuf (>=3)
 * gpsoauth
 * s2sphere
 * geopy (only for pokecli demo)

## Use
To use this api as part of a python project using setuptools/pip, modify your requirements.txt file to include:
```
git+https://github.com/pogodevorg/pgoapi.git@develop#egg=pgoapi
```

If you are not using setuptools/pip, follow the instructions in the Contributing section below to clone this repository and then install pgoapi using the appropriate method for your project.

### Hashing

The API utilises the [API Hashing service](https://hashing.pogodev.org) provided by Bossland. Calls require a valid hash key to work on newer API Versions.

## Contributing
Contributions are highly welcome. Please use github or [Discord](https://discord.pogodev.org) for it!

You can get started by cloning this repository. Note that as pgoapi uses [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) you must perform a recursive clone:

| Protocol | Command |
| -------- | ------- |
| HTTPS | `git clone --recursive https://github.com/pogodevorg/pgoapi.git` |
| SSH   | `git clone --recursive git@github.com:pogodevorg/pgoapi.git` |

If you already have a copy of the repository you can use `git submodule update --init` to fetch and update the submodules.

Once you have cloned the repository, switch to the `develop` branch. To merge your changes back into the main repository, make a pull request to `develop`.

## Core Maintainers

[![Noctem](https://github.com/Noctem.png?size=36) - Noctem](https://github.com/Noctem)

[![ZeChrales](https://github.com/ZeChrales.png?size=36) - ZeChrales](https://github.com/ZeChrales)

[![Ephemerality](https://github.com/Ephemerality.png?size=36) - Ephemerality](https://github.com/Ephemerality)


## Credits

* [Mila432](https://github.com/Mila432/Pokemon_Go_API) for the login secrets  
* [elliottcarlson](https://github.com/elliottcarlson) for the Google Auth PR  
* [AeonLucid](https://github.com/AeonLucid/POGOProtos) for improved protos  
* [AHAAAAAAA](https://github.com/AHAAAAAAA/PokemonGo-Map) for parts of the s2sphere stuff  
* [mikeres0](https://github.com/mikeres0) for the slack channel including auto signup  
* [DeirhX](https://github.com/DeirhX) for thread-safety

## Ports

See [Awesome Pokemon Go](https://github.com/pogodevorg/awesome-pokemongo#api-libraries)
