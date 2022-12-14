---
title: snapshot_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_policies
  - netapp
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
<tr><td><b>Name</b></td><td><code>snapshot_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.snapshot_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Snapshot policy properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SnapshotPolicies_Get` | `SELECT` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Get a snapshot Policy |
| `SnapshotPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List snapshot policy |
| `SnapshotPolicies_Create` | `INSERT` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId, data__location, data__properties` | Create a snapshot policy |
| `SnapshotPolicies_Delete` | `DELETE` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Delete snapshot policy |
| `SnapshotPolicies_ListVolumes` | `EXEC` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Get volumes associated with snapshot policy |
| `SnapshotPolicies_Update` | `EXEC` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` | Patch a snapshot policy |
