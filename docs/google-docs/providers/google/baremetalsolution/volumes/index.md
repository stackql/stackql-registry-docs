---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `volumes` | `array` | The list of storage volumes. |
| `nextPageToken` | `string` | A token identifying a page of results from the server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, volumesId` | Get details of a single storage volume. |
| `list` | `SELECT` | `locationsId, projectsId` | List storage volumes in a given project and location. |
| `evict` | `EXEC` | `locationsId, projectsId, volumesId` | Skips volume's cooloff and deletes it now. Volume must be in cooloff state. |
| `patch` | `EXEC` | `locationsId, projectsId, volumesId` | Update details of a single storage volume. |
| `rename` | `EXEC` | `locationsId, projectsId, volumesId` | RenameVolume sets a new name for a volume. Use with caution, previous names become immediately invalidated. |
| `resize` | `EXEC` | `locationsId, projectsId, volumesId` | Emergency Volume resize. |
