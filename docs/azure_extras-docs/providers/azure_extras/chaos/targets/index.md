---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - chaos
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
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.chaos.targets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | Location of the target resource. |
| `properties` | `object` | Model that represents the base Target properties model. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Targets_Get` | `SELECT` | `api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName` | Get a Target resource that extends a tracked regional resource. |
| `Targets_List` | `SELECT` | `api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId` | Get a list of Target resources that extend a tracked regional resource. |
| `Targets_CreateOrUpdate` | `INSERT` | `api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName, data__properties` | Create or update a Target resource that extends a tracked regional resource. |
| `Targets_Delete` | `DELETE` | `api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName` | Delete a Target resource that extends a tracked regional resource. |
