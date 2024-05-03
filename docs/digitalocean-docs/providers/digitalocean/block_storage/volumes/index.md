---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - block_storage
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.block_storage.volumes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier for the block storage volume. |
| <CopyableCode code="name" /> | `string` | A human-readable name for the block storage volume. Must be lowercase and be composed only of numbers, letters and "-", up to a limit of 64 characters. The name must begin with a letter. |
| <CopyableCode code="description" /> | `string` | An optional free-form text field to describe a block storage volume. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the block storage volume was created. |
| <CopyableCode code="droplet_ids" /> | `array` | An array containing the IDs of the Droplets the volume is attached to. Note that at this time, a volume can only be attached to a single Droplet. |
| <CopyableCode code="filesystem_label" /> | `string` | The label currently applied to the filesystem. |
| <CopyableCode code="filesystem_type" /> | `string` | The type of filesystem currently in-use on the volume. |
| <CopyableCode code="region" /> | `object` | The region that the block storage volume is located in. When setting a region, the value should be the slug identifier for the region. When you query a block storage volume, the entire region object will be returned. |
| <CopyableCode code="size_gigabytes" /> | `integer` | The size of the block storage volume in GiB (1024^3). |
| <CopyableCode code="tags" /> | `array` | A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="volume_id" /> | To show information about a block storage volume, send a GET request to `/v2/volumes/$VOLUME_ID`.<br /><br /> |
| <CopyableCode code="list" /> | `SELECT` |  | To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`.<br />## Filtering Results<br />### By Region<br />The `region` may be provided as query parameter in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1`<br />### By Name<br />It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`.<br />**Note:** You can only create one volume per region with the same name.<br />### By Name and Region<br />It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.<br /><br /><br /> |
| <CopyableCode code="create" /> | `INSERT` |  | To create a new volume, send a POST request to `/v2/volumes`. Optionally, a `filesystem_type` attribute may be provided in order to automatically format the volume's filesystem. Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without support for auto-mounting is not recommended. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="volume_id" /> | To delete a block storage volume, destroying all data and removing it from your account, send a DELETE request to `/v2/volumes/$VOLUME_ID`.<br />No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data.<br /><br /> |
| <CopyableCode code="delete_byName" /> | `DELETE` |  | Block storage volumes may also be deleted by name by sending a DELETE request with the volume's **name** and the **region slug** for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.<br />No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data.<br /><br /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="volume_id" /> | To show information about a block storage volume, send a GET request to `/v2/volumes/$VOLUME_ID`.<br /><br /> |
| <CopyableCode code="_list" /> | `EXEC` |  | To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`.<br />## Filtering Results<br />### By Region<br />The `region` may be provided as query parameter in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1`<br />### By Name<br />It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`.<br />**Note:** You can only create one volume per region with the same name.<br />### By Name and Region<br />It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.<br /><br /><br /> |
