---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Certificate resource specific properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get a certificate. |
| `list` | `SELECT` | `subscriptionId` | Description for Get all certificates for a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all certificates in a resource group. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Create or update a certificate. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete a certificate. |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all certificates for a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Get all certificates in a resource group. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update a certificate. |
