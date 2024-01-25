---
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
  - search
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
<tr><td><b>Name</b></td><td><code>shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.search.shared_private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes the properties of an existing Shared Private Link Resource managed by the search service. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, searchServiceName, sharedPrivateLinkResourceName, subscriptionId` | Gets the details of the shared private link resource managed by the search service in the given resource group. |
| `list_by_service` | `SELECT` | `resourceGroupName, searchServiceName, subscriptionId` | Gets a list of all shared private link resources managed by the given service. |
| `create_or_update` | `INSERT` | `resourceGroupName, searchServiceName, sharedPrivateLinkResourceName, subscriptionId` | Initiates the creation or update of a shared private link resource managed by the search service in the given resource group. |
| `delete` | `DELETE` | `resourceGroupName, searchServiceName, sharedPrivateLinkResourceName, subscriptionId` | Initiates the deletion of the shared private link resource from the search service. |
| `_list_by_service` | `EXEC` | `resourceGroupName, searchServiceName, subscriptionId` | Gets a list of all shared private link resources managed by the given service. |
