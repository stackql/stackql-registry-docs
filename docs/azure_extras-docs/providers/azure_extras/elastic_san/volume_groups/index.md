---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
  - elastic_san
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.elastic_san.volume_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
| `properties` | `object` | VolumeGroup response properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VolumeGroups_Get` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Get an VolumeGroups. |
| `VolumeGroups_ListByElasticSan` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId` | List VolumeGroups. |
| `VolumeGroups_Create` | `INSERT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Create a Volume Group. |
| `VolumeGroups_Delete` | `DELETE` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Delete an VolumeGroup. |
| `VolumeGroups_Update` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | Update an VolumeGroup. |
