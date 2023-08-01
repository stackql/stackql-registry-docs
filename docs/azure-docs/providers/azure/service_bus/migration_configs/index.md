---
title: migration_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_configs
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
<tr><td><b>Name</b></td><td><code>migration_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.migration_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `` | Properties required to the Create Migration Configuration |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MigrationConfigs_Get` | `SELECT` | `configName, namespaceName, resourceGroupName, subscriptionId` | Retrieves Migration Config |
| `MigrationConfigs_List` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets all migrationConfigurations |
| `MigrationConfigs_Delete` | `DELETE` | `configName, namespaceName, resourceGroupName, subscriptionId` | Deletes a MigrationConfiguration |
| `MigrationConfigs_CompleteMigration` | `EXEC` | `configName, namespaceName, resourceGroupName, subscriptionId` | This operation Completes Migration of entities by pointing the connection strings to Premium namespace and any entities created after the operation will be under Premium Namespace. CompleteMigration operation will fail when entity migration is in-progress. |
| `MigrationConfigs_CreateAndStartMigration` | `EXEC` | `configName, namespaceName, resourceGroupName, subscriptionId` | Creates Migration configuration and starts migration of entities from Standard to Premium namespace |
| `MigrationConfigs_Revert` | `EXEC` | `configName, namespaceName, resourceGroupName, subscriptionId` | This operation reverts Migration |
