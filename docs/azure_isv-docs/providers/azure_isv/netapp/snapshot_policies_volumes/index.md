---
title: snapshot_policies_volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_policies_volumes
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>snapshot_policies_volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.snapshot_policies_volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Volume properties |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | Availability Zone |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` |
| `_list` | `EXEC` | `accountName, resourceGroupName, snapshotPolicyName, subscriptionId` |
