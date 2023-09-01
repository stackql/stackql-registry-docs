---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - migrationcenter
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the asset. |
| `assignedGroups` | `array` | Output only. The list of groups that the asset is assigned to. |
| `labels` | `object` | Labels as key value pairs. |
| `performanceData` | `object` | Performance data for an asset. |
| `createTime` | `string` | Output only. The timestamp when the asset was created. |
| `sources` | `array` | Output only. The list of sources contributing to the asset. |
| `insightList` | `object` | Message containing insights list. |
| `machineDetails` | `object` | Details of a machine. |
| `updateTime` | `string` | Output only. The timestamp when the asset was last updated. |
| `attributes` | `object` | Generic asset attributes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assetsId, locationsId, projectsId` | Gets the details of an asset. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the assets in a given project and location. |
| `delete` | `DELETE` | `assetsId, locationsId, projectsId` | Deletes an asset. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all the assets in a given project and location. |
| `aggregate_values` | `EXEC` | `locationsId, projectsId` | Aggregates the requested fields based on provided function. |
| `batch_delete` | `EXEC` | `locationsId, projectsId` | Deletes list of Assets. |
| `batch_update` | `EXEC` | `locationsId, projectsId` | Updates the parameters of a list of assets. |
| `patch` | `EXEC` | `assetsId, locationsId, projectsId` | Updates the parameters of an asset. |
| `report_asset_frames` | `EXEC` | `locationsId, projectsId` | Reports a set of frames. |
