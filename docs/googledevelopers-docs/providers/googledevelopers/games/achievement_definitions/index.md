---
title: achievement_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - achievement_definitions
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
<tr><td><b>Name</b></td><td><code>achievement_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.achievement_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the achievement. |
| `name` | `string` | The name of the achievement. |
| `description` | `string` | The description of the achievement. |
| `isRevealedIconUrlDefault` | `boolean` | Indicates whether the revealed icon image being returned is a default image, or is provided by the game. |
| `revealedIconUrl` | `string` | The image URL for the revealed achievement icon. |
| `unlockedIconUrl` | `string` | The image URL for the unlocked achievement icon. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#achievementDefinition`. |
| `experiencePoints` | `string` | Experience points which will be earned when unlocking this achievement. |
| `initialState` | `string` | The initial state of the achievement. |
| `isUnlockedIconUrlDefault` | `boolean` | Indicates whether the unlocked icon image being returned is a default image, or is game-provided. |
| `achievementType` | `string` | The type of the achievement. |
| `totalSteps` | `integer` | The total steps for an incremental achievement. |
| `formattedTotalSteps` | `string` | The total steps for an incremental achievement as a string. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `achievementDefinitions_list` | `SELECT` |  |
