---
title: inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - inventories
  - osconfig
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
<tr><td><b>Name</b></td><td><code>inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.inventories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inventories` | `array` | List of inventory objects. |
| `nextPageToken` | `string` | The pagination token to retrieve the next page of inventory objects. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned. |
| `list` | `SELECT` | `instancesId, locationsId, projectsId` | List inventory data for all VM instances in the specified zone. |
