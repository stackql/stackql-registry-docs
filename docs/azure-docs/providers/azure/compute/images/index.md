---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - compute
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of an Image. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `imageName, resourceGroupName, subscriptionId` | Gets an image. |
| `list` | `SELECT` | `subscriptionId` | Gets the list of Images in the subscription. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of images under a resource group. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images. |
| `create_or_update` | `INSERT` | `imageName, resourceGroupName, subscriptionId` | Create or update an image. |
| `delete` | `DELETE` | `imageName, resourceGroupName, subscriptionId` | Deletes an Image. |
| `_list` | `EXEC` | `subscriptionId` | Gets the list of Images in the subscription. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the list of images under a resource group. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images. |
| `update` | `EXEC` | `imageName, resourceGroupName, subscriptionId` | Update an image. |
