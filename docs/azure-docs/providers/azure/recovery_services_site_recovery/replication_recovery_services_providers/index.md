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
| `ReplicationRecoveryServicesProviders_Get` | `SELECT` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | Gets the details of registered recovery services provider. |
| `ReplicationRecoveryServicesProviders_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the registered recovery services providers in the vault. |
| `ReplicationRecoveryServicesProviders_ListByReplicationFabrics` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the registered recovery services providers for the specified fabric. |
| `ReplicationRecoveryServicesProviders_Create` | `INSERT` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId, data__properties` | The operation to add a recovery services provider. |
| `ReplicationRecoveryServicesProviders_Delete` | `DELETE` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | The operation to removes/delete(unregister) a recovery services provider from the vault. |
| `ReplicationRecoveryServicesProviders_Purge` | `EXEC` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | The operation to purge(force delete) a recovery services provider from the vault. |
| `ReplicationRecoveryServicesProviders_RefreshProvider` | `EXEC` | `api-version, fabricName, providerName, resourceGroupName, resourceName, subscriptionId` | The operation to refresh the information from the recovery services provider. |
