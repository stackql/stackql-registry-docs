---
title: buildings
hide_title: false
hide_table_of_contents: false
keywords:
  - buildings
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buildings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.buildings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A brief description of the building. For example, "Chelsea Market". |
| `etags` | `string` | ETag of the resource. |
| `floorNames` | `array` | The display names for all floors in this building. The floors are expected to be sorted in ascending order, from lowest floor to highest floor. For example, ["B2", "B1", "L", "1", "2", "2M", "3", "PH"] Must contain at least one entry. |
| `kind` | `string` | Kind of resource this is. |
| `address` | `object` | Public API: Resources.buildings |
| `buildingId` | `string` | Unique identifier for the building. The maximum length is 100 characters. |
| `buildingName` | `string` | The building name as seen by users in Calendar. Must be unique for the customer. For example, "NYC-CHEL". The maximum length is 100 characters. |
| `coordinates` | `object` | Public API: Resources.buildings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `buildingId, customer` | Retrieves a building. |
| `list` | `SELECT` | `customer` | Retrieves a list of buildings for an account. |
| `insert` | `INSERT` | `customer` | Inserts a building. |
| `delete` | `DELETE` | `buildingId, customer` | Deletes a building. |
| `_list` | `EXEC` | `customer` | Retrieves a list of buildings for an account. |
| `patch` | `EXEC` | `buildingId, customer` | Patches a building. |
| `update` | `EXEC` | `buildingId, customer` | Updates a building. |
