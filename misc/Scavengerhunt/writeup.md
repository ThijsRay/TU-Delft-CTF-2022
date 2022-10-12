## Challenge

Are you looking for a friend too? Send me a request @1029491866770624562

## Solution

- 1029491866770624562 is a discord id
- the user has their github account linked
- heading to the github we can notice few things
  - location: Mumbai
  - starred repos: stegcloak, whitespace
  - commit history of README.md
  - https://pastebin.com/eD7waAfP
  - some whitespace code
  - Hi there :wave (stegcloak)

- decoding the whitespace we get the password for stegcloak i.e. Arandompassword42
- unhiding the text from stegcloak, will give password to the pastebin
- the pastebin has a crypto wallet address and another pastebin containing abi.json 
- from the location: Mumbai, we can infer that the blockchain is Polygon Mumbai Testnet
- from the abi ,we can see there is a function named getFlag. So we will need to call that function.
- We can use remix and create our own smart contract to call that function
