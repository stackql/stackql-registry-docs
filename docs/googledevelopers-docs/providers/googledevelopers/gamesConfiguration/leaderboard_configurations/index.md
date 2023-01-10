---
title: leaderboard_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - leaderboard_configurations
  - gamesConfiguration
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
<tr><td><b>Name</b></td><td><code>leaderboard_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.gamesConfiguration.leaderboard_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the leaderboard. |
| `scoreMin` | `string` | Minimum score that can be posted to this leaderboard. |
| `scoreOrder` | `string` |  |
| `token` | `string` | The token for this resource. |
| `draft` | `object` | A leaderboard configuration detail. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#leaderboardConfiguration`. |
| `published` | `object` | A leaderboard configuration detail. |
| `scoreMax` | `string` | Maximum score that can be posted to this leaderboard. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `leaderboardConfigurations_get` | `SELECT` | `leaderboardId` | Retrieves the metadata of the leaderboard configuration with the given ID. |
| `leaderboardConfigurations_list` | `SELECT` | `applicationId` | Returns a list of the leaderboard configurations in this application. |
| `leaderboardConfigurations_delete` | `DELETE` | `leaderboardId` | Delete the leaderboard configuration with the given ID. |
| `leaderboardConfigurations_insert` | `EXEC` | `applicationId` | Insert a new leaderboard configuration in this application. |
| `leaderboardConfigurations_update` | `EXEC` | `leaderboardId` | Update the metadata of the leaderboard configuration with the given ID. |
