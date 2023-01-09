---
title: players
hide_title: false
hide_table_of_contents: false
keywords:
  - players
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
<tr><td><b>Name</b></td><td><code>players</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.players</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | A representation of the individual components of the name. |
| `avatarImageUrl` | `string` | The base URL for the image that represents the player. |
| `profileSettings` | `object` | Profile settings |
| `title` | `string` | The player's title rewarded for their game activities. |
| `gamePlayerId` | `string` | Per-application unique player identifier. |
| `originalPlayerId` | `string` | The player ID that was used for this player the first time they signed into the game in question. This is only populated for calls to player.get for the requesting player, only if the player ID has subsequently changed, and only to clients that support remapping player IDs. |
| `friendStatus` | `string` | The friend status of the given player, relative to the requester. This is unset if the player is not sharing their friends list with the game. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#player` |
| `displayName` | `string` | The name to display for the player. |
| `bannerUrlLandscape` | `string` | The url to the landscape mode player banner image. |
| `playerId` | `string` | The ID of the player. |
| `bannerUrlPortrait` | `string` | The url to the portrait mode player banner image. |
| `experienceInfo` | `object` | 1P/3P metadata about the player's experience. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `playerId` | Retrieves the Player resource with the given ID. To retrieve the player for the currently authenticated user, set `playerId` to `me`. |
| `list` | `SELECT` | `collection` | Get the collection of players for the currently authenticated user. |
