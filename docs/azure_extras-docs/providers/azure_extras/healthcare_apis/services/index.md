---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - healthcare_apis
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `tags` | `object` | The resource tags. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| `kind` | `string` | The kind of the service. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The properties of a service instance. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The resource type. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a service instance. |
| `Services_List` | `SELECT` | `subscriptionId` | Get all the service instances in a subscription. |
| `Services_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `Services_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a service instance. |
| `Services_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a service instance. |
| `Services_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Check if a service instance name is available. |
| `Services_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a service instance. |
