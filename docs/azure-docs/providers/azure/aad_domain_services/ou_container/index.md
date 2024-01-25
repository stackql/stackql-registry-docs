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
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `etag` | `string` | Resource etag |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties of the OuContainer. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | Get OuContainer in DomainService instance. |
| `list` | `SELECT` | `domainServiceName, resourceGroupName, subscriptionId` | The List of OuContainers in DomainService instance. |
| `create` | `INSERT` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Create OuContainer operation creates a new OuContainer under the specified Domain Service instance. |
| `delete` | `DELETE` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Delete OuContainer operation deletes specified OuContainer. |
| `_list` | `EXEC` | `domainServiceName, resourceGroupName, subscriptionId` | The List of OuContainers in DomainService instance. |
| `update` | `EXEC` | `domainServiceName, ouContainerName, resourceGroupName, subscriptionId` | The Update OuContainer operation can be used to update the existing OuContainers. |
