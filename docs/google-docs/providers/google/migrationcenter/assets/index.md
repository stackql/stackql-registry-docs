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
| `unreachable` | `array` | Locations that could not be reached. |
| `assets` | `array` | A list of assets. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assetsId, locationsId, projectsId` | Gets the details of an asset. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the assets in a given project and location. |
| `delete` | `DELETE` | `assetsId, locationsId, projectsId` | Deletes an asset. |
| `aggregate_values` | `EXEC` | `locationsId, projectsId` | Aggregates the requested fields based on provided function. |
| `batch_delete` | `EXEC` | `locationsId, projectsId` | Deletes list of Assets. |
| `batch_update` | `EXEC` | `locationsId, projectsId` | Updates the parameters of a list of assets. |
| `patch` | `EXEC` | `assetsId, locationsId, projectsId` | Updates the parameters of an asset. |
| `report_asset_frames` | `EXEC` | `locationsId, projectsId` | Reports a set of frames. |
