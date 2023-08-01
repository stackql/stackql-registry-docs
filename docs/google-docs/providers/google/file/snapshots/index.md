---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - file
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.file.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token you can use to retrieve the next page of results. Not returned if there are no more results in the list. |
| `snapshots` | `array` | A list of snapshots in the project for the specified instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId, snapshotsId` | Gets the details of a specific snapshot. |
| `list` | `SELECT` | `instancesId, locationsId, projectsId` | Lists all snapshots in a project for either a specified location or for all locations. |
| `create` | `INSERT` | `instancesId, locationsId, projectsId` | Creates a snapshot. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId, snapshotsId` | Deletes a snapshot. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId, snapshotsId` | Updates the settings of a specific snapshot. |
