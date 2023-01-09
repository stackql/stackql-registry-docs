---
title: players
hide_title: false
hide_table_of_contents: false
keywords:
  - players
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
<tr><td><b>Name</b></td><td><code>players</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.gamesManagement.players</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `hide` | `EXEC` | `applicationId, playerId` | Hide the given player's leaderboard scores from the given application. This method is only available to user accounts for your developer console. |
| `unhide` | `EXEC` | `applicationId, playerId` | Unhide the given player's leaderboard scores from the given application. This method is only available to user accounts for your developer console. |
