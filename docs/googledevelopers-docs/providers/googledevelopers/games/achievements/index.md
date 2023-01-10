---
title: achievements
hide_title: false
hide_table_of_contents: false
keywords:
  - achievements
  - games
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>achievements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.achievements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the achievement. |
| `achievementState` | `string` | The state of the achievement. |
| `currentSteps` | `integer` | The current steps for an incremental achievement. |
| `experiencePoints` | `string` | Experience points earned for the achievement. This field is absent for achievements that have not yet been unlocked and 0 for achievements that have been unlocked by testers but that are unpublished. |
| `formattedCurrentStepsString` | `string` | The current steps for an incremental achievement as a string. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#playerAchievement`. |
| `lastUpdatedTimestamp` | `string` | The timestamp of the last modification to this achievement's state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `playerId` | Lists the progress for all your application's achievements for the currently authenticated player. |
| `increment` | `EXEC` | `achievementId, stepsToIncrement` | Increments the steps of the achievement with the given ID for the currently authenticated player. |
| `reveal` | `EXEC` | `achievementId` | Sets the state of the achievement with the given ID to `REVEALED` for the currently authenticated player. |
| `setStepsAtLeast` | `EXEC` | `achievementId, steps` | Sets the steps for the currently authenticated player towards unlocking an achievement. If the steps parameter is less than the current number of steps that the player already gained for the achievement, the achievement is not modified. |
| `unlock` | `EXEC` | `achievementId` | Unlocks this achievement for the currently authenticated player. |
| `updateMultiple` | `EXEC` |  | Updates multiple achievements for the currently authenticated player. |
