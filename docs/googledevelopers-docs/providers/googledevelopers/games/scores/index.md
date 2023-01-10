---
title: scores
hide_title: false
hide_table_of_contents: false
keywords:
  - scores
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
<tr><td><b>Name</b></td><td><code>scores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.scores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `timeSpan` | `string` | The time span of this score. |
| `scoreTag` | `string` | Additional information about the score. Values must contain no more than 64 URI-safe characters as defined by section 2.3 of RFC 3986. |
| `writeTimestamp` | `string` | The timestamp at which this score was recorded, in milliseconds since the epoch in UTC. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#playerLeaderboardScore`. |
| `leaderboard_id` | `string` | The ID of the leaderboard this score is in. |
| `scoreString` | `string` | The formatted value of this score. |
| `scoreValue` | `string` | The numerical value of this score. |
| `friendsRank` | `object` | A score rank in a leaderboard. |
| `publicRank` | `object` | A score rank in a leaderboard. |
| `socialRank` | `object` | A score rank in a leaderboard. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `leaderboardId, playerId, timeSpan` | Get high scores, and optionally ranks, in leaderboards for the currently authenticated player. For a specific time span, `leaderboardId` can be set to `ALL` to retrieve data for all leaderboards in a given time span. `NOTE: You cannot ask for 'ALL' leaderboards and 'ALL' timeSpans in the same request; only one parameter may be set to 'ALL'. |
| `list` | `SELECT` | `collection, leaderboardId, timeSpan` | Lists the scores in a leaderboard, starting from the top. |
| `submit` | `EXEC` | `leaderboardId, score` | Submits a score to the specified leaderboard. |
| `submitMultiple` | `EXEC` |  | Submits multiple scores to leaderboards. |
