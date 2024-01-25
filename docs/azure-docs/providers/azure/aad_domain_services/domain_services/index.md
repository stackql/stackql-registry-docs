---
title: domain_services
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_services
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
<tr><td><b>Name</b></td><td><code>domain_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_domain_services.domain_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `etag` | `string` | Resource etag |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties of the Domain Service. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainServiceName, resourceGroupName, subscriptionId` | The Get Domain Service operation retrieves a json representation of the Domain Service. |
| `list` | `SELECT` | `subscriptionId` | The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription). |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The List Domain Services in Resource Group operation lists all the domain services available under the given resource group. |
| `create_or_update` | `INSERT` | `domainServiceName, resourceGroupName, subscriptionId` | The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged. |
| `delete` | `DELETE` | `domainServiceName, resourceGroupName, subscriptionId` | The Delete Domain Service operation deletes an existing Domain Service. |
| `_list` | `EXEC` | `subscriptionId` | The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription). |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The List Domain Services in Resource Group operation lists all the domain services available under the given resource group. |
| `update` | `EXEC` | `domainServiceName, resourceGroupName, subscriptionId` | The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body. |
