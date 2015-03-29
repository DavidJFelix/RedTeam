# The MacGuyver RJ45 10BASE-T/100BASE-TX Tap

The MacGuyver tap is named for its simplicity and ability to be created with only 1 additional RJ45 cable.
This was inspired by the "throwing star LAN Tap" and the 5-in-1 network administrators cables.
Rather than pay somebody else money, you can simply destroy cables that you have lying around and create your own.

## Supplies

* RJ45 Cable with known pinning
* Wirecutters (optional)
* Wirestrippers (optional)
* Electrical tape (optional)

## Disclaimer

* Don't destroy other people's property.
* Tapping wires that aren't yours, without your permission may be a crime, but I'm not a laywer, nor is this legal advice.
* As with all of this project, don't be stupid.
* Don't blame me if you're stupid.
* This type of tap only works on RJ45 10/100 Mb connections.
1000BASE-TX will not work as it uses more of the wires within an RJ45.
There are ways to force a gigabit connection to downgrade to 10/100, but those aren't mentioned in this module.

## Directions

* Determine the pinning of the RJ45 cable that you're intending on tapping.
A TIA/EIA-568A pinning will have the green pair on one end while a TIA/EIA-568B pinning will have the orange pair on one end.
Both pinnings have the brown pair on the opposite end.
* If the connectors are opaque and you can't see the ends of the cable, you can still continue the instructions, but you'll have to infer the directionality later rather than immediately.
* Determine the pinning of the RJ45 that you'll be using for the tap.
If you have a TIA/EIA-568A, your tapping pair will be green;
If you have a TIA/EIA-568B, your tapping pair will be orange;
It's important that you ensure you're using the correct pair, as a reverse could result in creating a way to broadcast but not listen.
If you're unsure of the pinning or the wires are nonstandard, you're looking to tap with the pair connected at pinout 3 and pinout 6.
* Cut or break the RJ45 cable that you'll be using to tap entirely in half.
Sever all wires within the cable at the cut.
* Strip a working are from each side of the cable.
6cm should be enough area.
* Cut all pairs except your tapping pair down to the edge of the working area.
It can be helpful to cut them at different lengths to prevent them from crossing.
Folding them back or taping (tape - ing) their ends can ensure this.
* Strip about 1cm from each wire in the tapping pair and unwind them a bit to give yourself more room.
* Strip the casing on the wire that you intend to tap, ensuring that you don't cut any of the wires with it.
It may be helpful to remove up to 10cm of casing for easy access, but 5cm should be sufficient if you have tape.
* Strip (without cutting) the orange pair in areas close to eachother but not next to eachother.
* Cross your tapping wires from one of your tapping cable halves with the orange pair.
Striped to striped; solid to solid.
If you have a wierd pair, your goal is to cross your pin 3 with the tapped wire pin 1 and your pin 6 with the tapped wire pin 2.
Ensure that these crosses are not touching eachother.
Using electrical tape to isolate and secure the connection may be a good idea.
* Strip (without cutting) the green pair of the cable you're tapping.
These should be stripped near eachother, but you can place it away from the orange stripped wires if you need room.
The two taps act seperately.
* Cross the tapping wires from the other half of your tapping cable with the tapped green pair.
Striped to striped; solid to solid.
If you have a wierd pair, your goal is to cross your pin 3 with the tapped wire pin 3 and your pin 6 with the tapped wire pin 6.

You're done!

## Use

One of your tap cables will be able to monitor traffic in one direction.
The other tap cable will be able to monitor traffic in the other direction.
The pinning and network topology will allow you to determine which tap monitors which direction.
