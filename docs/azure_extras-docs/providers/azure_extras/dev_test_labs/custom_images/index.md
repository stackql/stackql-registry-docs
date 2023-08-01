---
title: custom_images
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_images
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.custom_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a custom image. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomImages_Get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Get custom image. |
| `CustomImages_List` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId` | List custom images in a given lab. |
| `CustomImages_CreateOrUpdate` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, data__properties` | Create or replace an existing custom image. This operation can take a while to complete. |
| `CustomImages_Delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId` | Delete custom image. This operation can take a while to complete. |
| `CustomImages_Update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Allows modifying tags of custom images. All other properties will be ignored. |
