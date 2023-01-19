---
title: achievement_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - achievement_configurations
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
<tr><td><b>Name</b></td><td><code>achievement_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.gamesConfiguration.achievement_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the achievement. |
| `stepsToUnlock` | `integer` | Steps to unlock. Only applicable to incremental achievements. |
| `token` | `string` | The token for this resource. |
| `achievementType` | `string` | The type of the achievement. |
| `draft` | `object` | An achievement configuration detail. |
| `initialState` | `string` | The initial state of the achievement. |
| `kind` | `string` | Uniquely identifies the type of this resource. Value is always the fixed string `gamesConfiguration#achievementConfiguration`. |
| `published` | `object` | An achievement configuration detail. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `achievementConfigurations_get` | `SELECT` | `achievementId` | Retrieves the metadata of the achievement configuration with the given ID. |
| `achievementConfigurations_list` | `SELECT` | `applicationId` | Returns a list of the achievement configurations in this application. |
| `achievementConfigurations_delete` | `DELETE` | `achievementId` | Delete the achievement configuration with the given ID. |
| `achievementConfigurations_insert` | `EXEC` | `applicationId` | Insert a new achievement configuration in this application. |
| `achievementConfigurations_update` | `EXEC` | `achievementId` | Update the metadata of the achievement configuration with the given ID. |
