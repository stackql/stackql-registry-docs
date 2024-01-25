---
title: msix_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - msix_packages
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>msix_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.msix_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Schema for MSIX Package properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId` | Get a msixpackage. |
| `list` | `SELECT` | `hostPoolName, resourceGroupName, subscriptionId` | List MSIX packages in hostpool. |
| `create_or_update` | `INSERT` | `hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId, data__properties` | Create or update a MSIX package. |
| `delete` | `DELETE` | `hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId` | Remove an MSIX Package. |
| `_list` | `EXEC` | `hostPoolName, resourceGroupName, subscriptionId` | List MSIX packages in hostpool. |
| `update` | `EXEC` | `hostPoolName, msixPackageFullName, resourceGroupName, subscriptionId` | Update an  MSIX Package. |
