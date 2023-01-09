---
title: metagame__metagame_config
hide_title: false
hide_table_of_contents: false
keywords:
  - metagame__metagame_config
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
<tr><td><b>Name</b></td><td><code>metagame__metagame_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.games.metagame__metagame_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `currentVersion` | `integer` | Current version of the metagame configuration data. When this data is updated, the version number will be increased by one. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `games#metagameConfig`. |
| `playerLevels` | `array` | The list of player levels. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `metagame_getMetagameConfig` | `SELECT` |  |
