---
title: disaster_recovery_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs
  - service_bus
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
<tr><td><b>Id</b></td><td><code>azure.service_bus.disaster_recovery_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `` | Properties required to the Create Or Update Alias(Disaster Recovery configurations) |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alias, namespaceName, resourceGroupName, subscriptionId` | Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace |
| `list` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all Alias(Disaster Recovery configurations) |
| `create_or_update` | `INSERT` | `alias, namespaceName, resourceGroupName, subscriptionId` | Creates or updates a new Alias(Disaster Recovery configuration) |
| `delete` | `DELETE` | `alias, namespaceName, resourceGroupName, subscriptionId` | Deletes an Alias(Disaster Recovery configuration) |
| `_list` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets all Alias(Disaster Recovery configurations) |
| `break_pairing` | `EXEC` | `alias, namespaceName, resourceGroupName, subscriptionId` | This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces |
| `check_name_availability` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, data__name` | Check the give namespace name availability. |
| `fail_over` | `EXEC` | `alias, namespaceName, resourceGroupName, subscriptionId` | Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace |
