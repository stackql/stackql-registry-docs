---
title: structures
hide_title: false
hide_table_of_contents: false
keywords:
  - structures
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
<tr><td><b>Name</b></td><td><code>structures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.smartdevicemanagement.structures</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the structure. For example: "enterprises/XYZ/structures/ABC". |
| `traits` | `object` | Structure traits. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `enterprises_structures_get` | `SELECT` | `enterprisesId, structuresId` | Gets a structure managed by the enterprise. |
| `enterprises_structures_list` | `SELECT` | `enterprisesId` | Lists structures managed by the enterprise. |
