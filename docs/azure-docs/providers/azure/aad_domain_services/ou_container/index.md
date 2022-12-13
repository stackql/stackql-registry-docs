---
title: ou_container
hide_title: false
hide_table_of_contents: false
keywords:
  - ou_container
  - aad_domain_services
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
<tr><td><b>Name</b></td><td><code>ou_container</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_domain_services.ou_container</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the OuContainer. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OuContainer_Get` | `SELECT` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | Get OuContainer in DomainService instance. |
| `OuContainer_List` | `SELECT` | `domainServiceName, resourceGroupName, subscriptionId` | The List of OuContainers in DomainService instance. |
| `OuContainer_Create` | `INSERT` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Create OuContainer operation creates a new OuContainer under the specified Domain Service instance. |
| `OuContainer_Delete` | `DELETE` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Delete OuContainer operation deletes specified OuContainer. |
| `OuContainer_Update` | `EXEC` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Update OuContainer operation can be used to update the existing OuContainers. |
