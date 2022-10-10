# Based

## Description
This challenge is just an encoding challenge. While it's in the crypto category, it's not really a crypto challenge. It does make the text look mangled and "encrypted" but there's no key or anything. The string is just encoded in a bunch of different bases in a row.

## Solution
I Hiiiiiighly recommend using something like [CyberChef](https://gchq.github.io/CyberChef/) to solve this challenge. It's a handy tool for doing all sorts of encoding, decoding and a lot more.
The hint for this challenge was `based` which is a reference to the encoding used in this challenge.

The _recipe_ for this challenge can be found here: [CyberChef_recipe](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Base85('!-u',true)From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',false)From_Base45('0-9A-Z%20$%25*%2B%5C%5C-./:',true)From_Base32('A-Z2-7%3D',false)&input=Ukhab2VWUnlkWEo1YUhSeFJGWnpabkoxU3pOVU9HUlNla050WjFNeGJXbEZTSHBXTmxaRGNrRmhTMjlxV0VaRmNtNWlWVTF0WVU1M1IxTTNZM1E0WldKak1XUnVjMk5oWVV0b09WZG9UV1pZU3pnMVFXOVRRMlJEVkZOamVVcEZhbUZyT0VwWVVqSnFOMXBwZDB3ME5YQktVRWhMU0VnMFJGRkdTMmRJTkZCVlVESjVjM1J1TmpkcGVVWjNSVmN5VWtSRFJUZzJNM0ZqU2pJMVZFMVVkVEZaYzBwcGFFdElOR1kzT1ZOTFpFc3pSbWhVYmpOck5VVk9aRE5HWW5odmRVeHpiVTVZY0hGV2QzWnhWVFJqUkVwT1VGRkVOSE53UVdwT1ZXNTVZMWt4WlZGa1NEZzJOWEZtVW1WdGNYWnFXR1pUWlU1eFpUZDJjMW95VURKb1ozSkNVMWh5V0RWeFNESjRkSE40V1dKV1FrMUlhM0pYUm5GSFV6aDFkbE00VEdORVlsQk1XVE5YWlZKTGFFVlVPRlkxWkV3MmJWTnpjRTVNVFhsUU1VdE9RbkpLYldoVE5saEhOVGxYYzFVelFVeDNha05UYW1GTVNEVkZSMVY0Wm1OMWRGUk9NMjF5YmxScFpYTk9aalJrU2xadVVVTkhjelk9)