---
title: content_item
hide_title: false
hide_table_of_contents: false
keywords:
  - content_item
  - api_management
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
<tr><td><b>Name</b></td><td><code>content_item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.content_item</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Returns the developer portal's content item specified by its identifier. |
| `list_by_service` | `SELECT` | `contentTypeId, resourceGroupName, serviceName, subscriptionId` | Lists developer portal's content items specified by the provided content type. |
| `create_or_update` | `INSERT` | `contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Creates a new developer portal's content item specified by the provided content type. |
| `delete` | `DELETE` | `If-Match, contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Removes the specified developer portal's content item. |
| `_list_by_service` | `EXEC` | `contentTypeId, resourceGroupName, serviceName, subscriptionId` | Lists developer portal's content items specified by the provided content type. |
