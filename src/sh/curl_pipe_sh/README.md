#curl | sh

This tactic is designed to prey on `curl | sh` pattern that is frequently used for installing software.

Piping curl into shell is a voluntary remote code execution.
Many people (including me) would argue that piping curl into shell is more vulnerable than the average software install.

The goal behind this tactic is to use the `curl | sh` pattern as a watering hole and instead of passing useful software, pass a malicious scriot
In the example install.sh script, the malicious script is a simple `rm -rf` on the root filesystem.
The sky is the limit and you shouldn't hinder your creativity.
Try hiding your tracks or more elaborate scripts.

Injecting your script into their download is the hardest part.
(I would argue) a good sysadmin shouldn't really be using `curl | sh` but it's so easy, so it's still likely.
MITM servers or social engineering (phishing, spoofing) methods are probably the best delivery method for a dumb attack like this.
