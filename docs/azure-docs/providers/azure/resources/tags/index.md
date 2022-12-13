---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - resources
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The tag name ID. |
| `tagName` | `string` | The tag name. |
| `values` | `array` | The list of tag values. |
| `count` | `object` | Tag count. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tags_List` | `SELECT` | `subscriptionId` | This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result. |
| `Tags_CreateOrUpdate` | `INSERT` | `subscriptionId, tagName` | This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'. |
| `Tags_Delete` | `DELETE` | `subscriptionId, tagName` | This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted. |
| `Tags_CreateOrUpdateAtScope` | `EXEC` | `scope, data__properties` | This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags. |
| `Tags_CreateOrUpdateValue` | `EXEC` | `subscriptionId, tagName, tagValue` | This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters. |
| `Tags_DeleteAtScope` | `EXEC` | `scope` |  |
| `Tags_DeleteValue` | `EXEC` | `subscriptionId, tagName, tagValue` | This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource. |
| `Tags_GetAtScope` | `EXEC` | `scope` |  |
| `Tags_UpdateAtScope` | `EXEC` | `scope` | This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The 'replace' option replaces the entire set of existing tags with a new set. The 'merge' option allows adding tags with new names and updating the values of tags with existing names. The 'delete' option allows selectively deleting tags based on given names or name/value pairs. |
