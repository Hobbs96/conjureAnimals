# conjureCreaturesDnD5e
A utility for randomly generating the creatures created by Conjuration spells in D&D 5e, since they are notoriously under-specified.

This was originally written to help me facilitate my home game (with two druids), and thus a local app was fine. I intend to move this to a simple web app, deprecate the Python application, and add coverage for all of the remaining conjuration spells that have the same issues with under-specification in their descriptions.

Don't hesitate to contact clarklindsay96@gmail.com with any feedback, feature requests, or other questions.

This is a small GUI application to simplify the use of creature conjuration spells.
The rules implemented by the app follow the Sage Advice post about the spell
(here: https://www.sageadvice.eu/2015/09/28/conjure-animals-does-the-player-pick-the-specific-animals-or-the-dm/),
as well as some minor tweaks made in conjunction with my players.
The application loads in a creature list in a JSON format, meaning that it is extensible, even with custom creatures.

Due to legal reasons, there cannot be a database to retrieve stat-blocks for the creatures that are generated. That being the case,
it is still necessary to have D&D material on hand, e.g. a monster manual. 
