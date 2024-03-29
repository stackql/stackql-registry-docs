---
title: gallery_items
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_items
  - gallery_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>gallery_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.gallery_admin.gallery_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of a gallery item. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `galleryItemName, subscriptionId` |
| `list` | `SELECT` | `subscriptionId` |
| `create` | `INSERT` | `subscriptionId` |
| `delete` | `DELETE` | `galleryItemName, subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
