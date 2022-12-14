---
title: disaster_recovery_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs
  - event_hub
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
<tr><td><b>Name</b></td><td><code>disaster_recovery_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hub.disaster_recovery_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `` | Properties required to the Create Or Update Alias(Disaster Recovery configurations) |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DisasterRecoveryConfigs_Get` | `SELECT` | `alias, namespaceName, resourceGroupName, subscriptionId` | Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace |
| `DisasterRecoveryConfigs_List` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all Alias(Disaster Recovery configurations) |
| `DisasterRecoveryConfigs_CreateOrUpdate` | `INSERT` | `alias, namespaceName, resourceGroupName, subscriptionId` | Creates or updates a new Alias(Disaster Recovery configuration) |
| `DisasterRecoveryConfigs_Delete` | `DELETE` | `alias, namespaceName, resourceGroupName, subscriptionId` | Deletes an Alias(Disaster Recovery configuration) |
| `DisasterRecoveryConfigs_BreakPairing` | `EXEC` | `alias, namespaceName, resourceGroupName, subscriptionId` | This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces |
| `DisasterRecoveryConfigs_CheckNameAvailability` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, data__name` | Check the give Namespace name availability. |
| `DisasterRecoveryConfigs_FailOver` | `EXEC` | `alias, namespaceName, resourceGroupName, subscriptionId` | Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace |
| `DisasterRecoveryConfigs_GetAuthorizationRule` | `EXEC` | `alias, authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets an AuthorizationRule for a Namespace by rule name. |
| `DisasterRecoveryConfigs_ListAuthorizationRules` | `EXEC` | `alias, namespaceName, resourceGroupName, subscriptionId` | Gets a list of authorization rules for a Namespace. |
| `DisasterRecoveryConfigs_ListKeys` | `EXEC` | `alias, authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets the primary and secondary connection strings for the Namespace. |
