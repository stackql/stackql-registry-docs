---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - dyn365_fraud_protection
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dyn365_fraud_protection.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | Location of the DFP resource. |
| `properties` | `object` | Properties of DFP resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Instances_List` | `SELECT` | `subscriptionId` | Lists all the Dedicated instances for the given subscription. |
| `Instances_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Dedicated instance for the given resource group. |
| `Instances_Create` | `INSERT` | `instanceName, resourceGroupName, subscriptionId, data__location` | Provisions the specified DFP instance based on the configuration specified in the request. |
| `Instances_Delete` | `DELETE` | `instanceName, resourceGroupName, subscriptionId` | Deletes the specified DFP instance. |
| `Instances_CheckNameAvailability` | `EXEC` | `location, subscriptionId` | Check the name availability in the target location. |
| `Instances_GetDetails` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Gets details about the specified instances. |
| `Instances_Update` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Updates the current state of the specified DFP instance. |
