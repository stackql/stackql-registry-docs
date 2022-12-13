---
title: volume_quota_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_quota_rules
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
<tr><td><b>Name</b></td><td><code>volume_quota_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.volume_quota_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Volume Quota Rule properties |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VolumeQuotaRules_Get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Get details of the specified quota rule |
| `VolumeQuotaRules_ListByVolume` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all quota rules associated with the volume |
| `VolumeQuotaRules_Create` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Create the specified quota rule within the given volume |
| `VolumeQuotaRules_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Delete quota rule |
| `VolumeQuotaRules_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Patch a quota rule |
