---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
  - elastic_san
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
<tr><td><b>Name</b></td><td><code>volume_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.elastic_san.volume_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `properties` | `object` | VolumeGroup response properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Get an VolumeGroups. |
| `list_by_elastic_san` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId` | List VolumeGroups. |
| `create` | `INSERT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Create a Volume Group. |
| `delete` | `DELETE` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Delete an VolumeGroup. |
| `_list_by_elastic_san` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId` | List VolumeGroups. |
| `update` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Update an VolumeGroup. |
