---
title: disk_accesses_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses_private_link_resources
  - compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_accesses_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_accesses_private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | private link resource Id |
| `name` | `string` | private link resource name |
| `properties` | `object` | Properties of a private link resource. |
| `type` | `string` | private link resource type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `diskAccessName, resourceGroupName, subscriptionId` |
| `_get` | `EXEC` | `diskAccessName, resourceGroupName, subscriptionId` |
