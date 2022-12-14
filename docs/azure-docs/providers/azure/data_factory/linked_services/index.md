---
title: linked_services
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_services
  - data_factory
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
<tr><td><b>Name</b></td><td><code>linked_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.linked_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `type` | `string` | The resource type. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | The nested object which contains the information and credential which can be used to connect with related store or compute resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LinkedServices_Get` | `SELECT` | `api-version, factoryName, linkedServiceName, resourceGroupName, subscriptionId` | Gets a linked service. |
| `LinkedServices_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists linked services. |
| `LinkedServices_CreateOrUpdate` | `INSERT` | `api-version, factoryName, linkedServiceName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a linked service. |
| `LinkedServices_Delete` | `DELETE` | `api-version, factoryName, linkedServiceName, resourceGroupName, subscriptionId` | Deletes a linked service. |
