---
title: volume_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_snapshots
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
<tr><td><b>Name</b></td><td><code>volume_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.elastic_san.volume_snapshots</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName` | Get a Volume Snapshot. |
| `list_by_volume_group` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter |
| `create` | `INSERT` | `elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName, data__properties` | Create a Volume Snapshot. |
| `delete` | `DELETE` | `elasticSanName, resourceGroupName, snapshotName, subscriptionId, volumeGroupName` | Delete a Volume Snapshot. |
| `_list_by_volume_group` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId, volumeGroupName` | List Snapshots in a VolumeGroup or List Snapshots by Volume (name) in a VolumeGroup using filter |
