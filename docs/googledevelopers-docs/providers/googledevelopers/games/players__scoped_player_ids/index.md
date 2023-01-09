---
title: players__scoped_player_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - players__scoped_player_ids
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
<tr><td><b>Name</b></td><td><code>players__scoped_player_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.players__scoped_player_ids</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `gamePlayerId` | `string` | Game-scoped player identifier. This is the same id that is returned in GetPlayer game_player_id field. |
| `developerPlayerKey` | `string` | Identifier of the player across all games of the given developer. Every player has the same developer_player_key in all games of one developer. Developer player key changes for the game if the game is transferred to another developer. Note that game_player_id will stay unchanged. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `players_getScopedPlayerIds` | `SELECT` |  |
