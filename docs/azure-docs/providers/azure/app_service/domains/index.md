---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - app_service
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Domain resource specific properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | Description for Get a domain. |
| `list` | `SELECT` | `subscriptionId` | Description for Get all domains in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all domains in a resource group. |
| `create_or_update` | `INSERT` | `domainName, resourceGroupName, subscriptionId` | Description for Creates or updates a domain. |
| `delete` | `DELETE` | `domainName, resourceGroupName, subscriptionId` | Description for Delete a domain. |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all domains in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Get all domains in a resource group. |
| `check_availability` | `EXEC` | `subscriptionId` | Description for Check if a domain is available for registration. |
| `renew` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Description for Renew a domain. |
| `transfer_out` | `EXEC` | `domainName, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Description for Creates or updates a domain. |
