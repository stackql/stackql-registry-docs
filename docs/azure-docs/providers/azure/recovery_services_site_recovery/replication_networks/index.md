---
title: replication_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_networks
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Network Properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, networkName, resourceGroupName, resourceName, subscriptionId` | Gets the details of a network. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the networks available in a vault. |
| `list_by_replication_fabrics` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the networks available for a fabric. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the networks available in a vault. |
| `_list_by_replication_fabrics` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the networks available for a fabric. |
