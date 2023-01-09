---
title: scores
hide_title: false
hide_table_of_contents: false
keywords:
  - scores
  - gamesManagement
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
<tr><td><b>Name</b></td><td><code>scores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.gamesManagement.scores</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reset` | `EXEC` | `leaderboardId` | Resets scores for the leaderboard with the given ID for the currently authenticated player. This method is only accessible to whitelisted tester accounts for your application. |
| `resetAll` | `EXEC` |  | Resets all scores for all leaderboards for the currently authenticated players. This method is only accessible to whitelisted tester accounts for your application. |
| `resetAllForAllPlayers` | `EXEC` |  | Resets scores for all draft leaderboards for all players. This method is only available to user accounts for your developer console. |
| `resetForAllPlayers` | `EXEC` | `leaderboardId` | Resets scores for the leaderboard with the given ID for all players. This method is only available to user accounts for your developer console. Only draft leaderboards can be reset. |
| `resetMultipleForAllPlayers` | `EXEC` |  | Resets scores for the leaderboards with the given IDs for all players. This method is only available to user accounts for your developer console. Only draft leaderboards may be reset. |
