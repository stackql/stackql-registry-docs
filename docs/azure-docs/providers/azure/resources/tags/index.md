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
| `count` | `object` | Tag count. |
| `tagName` | `string` | The tag name. |
| `values` | `array` | The list of tag values. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result. |
| `create_or_update` | `INSERT` | `subscriptionId, tagName` | This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'. |
| `delete` | `DELETE` | `subscriptionId, tagName` | This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted. |
| `_list` | `EXEC` | `subscriptionId` | This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result. |
