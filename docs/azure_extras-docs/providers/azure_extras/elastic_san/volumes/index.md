---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.elastic_san.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `properties` | `object` | Volume response properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Volumes_Get` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Get an Volume. |
| `Volumes_ListByVolumeGroup` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | List Volumes in a VolumeGroup. |
| `Volumes_Create` | `INSERT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Create a Volume. |
| `Volumes_Delete` | `DELETE` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Delete an Volume. |
| `Volumes_Update` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName, volumeName` | Update an Volume. |
