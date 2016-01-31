TODO Next
=========

**Priority**

- Setup inside virtual environment

  + make testing (esp. command line) easier

- Comply with one function = one reponsibility principal

- Write some useful unit tests

**in no particular order**

- Add command line script with argparser
	
  + --config, --tag, etc...

- Move settings/configuration to dedicated module
	
  + `will greatly simplify input validation`

- Rewrite input validation in first_run() logic

  + `KeyboardInterrupts broken, poor validation, etc.`

- Break up make_post() into smaller, simpler functions
	
  + `too many nested statements\too much logic for one function`

- Build a 'Bot' class for better attribute handling
	
  + `this will simplify interactions in the future`

- Add checks throughout code for invalid/missing configurations
	
  + `right now only checking if the files EXIST on __init__`

- Add/improve console and txt file logging