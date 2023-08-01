---
title: luns
hide_title: false
hide_table_of_contents: false
keywords:
  - luns
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
<tr><td><b>Name</b></td><td><code>luns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.luns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `luns` | `array` | The list of luns. |
| `nextPageToken` | `string` | A token identifying a page of results from the server. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, lunsId, projectsId, volumesId` | Get details of a single storage logical unit number(LUN). |
| `list` | `SELECT` | `locationsId, projectsId, volumesId` | List storage volume luns for given storage volume. |
| `evict` | `EXEC` | `locationsId, lunsId, projectsId, volumesId` | Skips lun's cooloff and deletes it now. Lun must be in cooloff state. |
