---
title: replication_recovery_services_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_services_providers
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
<tr><td><b>Name</b></td><td><code>replication_recovery_services_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_recovery_services_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Recovery services provider properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | Gets the details of registered recovery services provider. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the registered recovery services providers in the vault. |
| `list_by_replication_fabrics` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the registered recovery services providers for the specified fabric. |
| `create` | `INSERT` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to add a recovery services provider. |
| `delete` | `DELETE` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | The operation to removes/delete(unregister) a recovery services provider from the vault. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the registered recovery services providers in the vault. |
| `_list_by_replication_fabrics` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the registered recovery services providers for the specified fabric. |
| `purge` | `EXEC` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | The operation to purge(force delete) a recovery services provider from the vault. |
| `refresh_provider` | `EXEC` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | The operation to refresh the information from the recovery services provider. |
