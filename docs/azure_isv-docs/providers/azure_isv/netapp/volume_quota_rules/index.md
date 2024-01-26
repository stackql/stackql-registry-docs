---
title: volume_quota_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_quota_rules
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
<tr><td><b>Name</b></td><td><code>volume_quota_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.volume_quota_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Volume Quota Rule properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Get details of the specified quota rule |
| `list_by_volume` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all quota rules associated with the volume |
| `create` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Create the specified quota rule within the given volume |
| `delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Delete quota rule |
| `_list_by_volume` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all quota rules associated with the volume |
| `update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName, volumeQuotaRuleName` | Patch a quota rule |
