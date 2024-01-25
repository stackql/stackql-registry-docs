---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - security
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | describes security alert properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `api-version, subscriptionId` | List all the alerts that are associated with the subscription |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List all the alerts that are associated with the resource group |
| `_list` | `EXEC` | `api-version, subscriptionId` | List all the alerts that are associated with the subscription |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List all the alerts that are associated with the resource group |
| `simulate` | `EXEC` | `api-version, ascLocation, subscriptionId` | Simulate security alerts |
