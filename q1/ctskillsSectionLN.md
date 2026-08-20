# Computational Thinking Exercise
## [Smart Vending Machine]
**Name:** Heinrich David M. Lo
**Section:** Beryllium
**Last Name:** Lo
**Date:** 08/19/2026
---

## Step 1: Identify the Big Problem
### Main Problem
Sometimes, the vending machine has trouble with giving the correct amount of change.

---
## Step 2: Identify the Sub-Problems
1. Student entering an big sum of cash in the machine
2. Vending machine only accepts bills and not coins
3. Vending Machine is having a malfunction
4. Vending machine is calibrated wrongly
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| entering an big sum of cash in the machine | algorithm design | Make a sequence of steps that aims to reduce amount of cash inserted |
| only accepts bills and not coins | algorithm design | Make a sequence of steps to find the appropriate bill to enter |
| Vending Machine is having a malfunction | abstraction | Focus on the cause of the malfunction rather than around it |
| Vending machine is calibrated wrongly | decomposition | Break down the calibration process into smaller, manageable parts|
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Vending machine is calibrated wrongly.
### Pseudocode
START

Ask user if they want to recalibrate

If user picks 'yes':

Open calibration panel

If user picks 'recalibrate':

Ask user what they want to recalibrate

If user picks 'float':

System recalibrates float

Shows user "Recalibration Complete"

END

Else if user picks 'int':

System recalibrates int

Shows user "Recalibration Complete"

END

If user picks 'return':

return to Start

If user picks 'no':

END

END
