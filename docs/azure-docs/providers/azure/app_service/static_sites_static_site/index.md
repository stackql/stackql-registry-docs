---
title: static_sites_static_site
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_static_site
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
<tr><td><b>Name</b></td><td><code>static_sites_static_site</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.static_sites_static_site</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Managed service identity. |
| `properties` | `object` | A static site. |
| `sku` | `object` | Description of a SKU for a scalable resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the details of a static site. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Creates a new static site in an existing resource group, or updates an existing static site. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Deletes a static site. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a new static site in an existing resource group, or updates an existing static site. |
