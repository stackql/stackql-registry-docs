---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.elastic_san.volumes</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Get an Volume. |
| `list_by_volume_group` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | List Volumes in a VolumeGroup. |
| `create` | `INSERT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName, data__properties` | Create a Volume. |
| `delete` | `DELETE` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Delete an Volume. |
| `_list_by_volume_group` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | List Volumes in a VolumeGroup. |
| `update` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Update an Volume. |
