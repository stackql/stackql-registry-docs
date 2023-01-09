---
title: rooms
hide_title: false
hide_table_of_contents: false
keywords:
  - rooms
  - smartdevicemanagement
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
<tr><td><b>Name</b></td><td><code>rooms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.smartdevicemanagement.rooms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the room. For example: "enterprises/XYZ/structures/ABC/rooms/123". |
| `traits` | `object` | Room traits. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `enterprises_structures_rooms_get` | `SELECT` | `enterprisesId, roomsId, structuresId` | Gets a room managed by the enterprise. |
| `enterprises_structures_rooms_list` | `SELECT` | `enterprisesId, structuresId` | Lists rooms managed by the enterprise. |
