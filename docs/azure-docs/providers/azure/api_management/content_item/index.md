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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContentItem_Get` | `SELECT` | `contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Returns the developer portal's content item specified by its identifier. |
| `ContentItem_ListByService` | `SELECT` | `contentTypeId, resourceGroupName, serviceName, subscriptionId` | Lists developer portal's content items specified by the provided content type. |
| `ContentItem_CreateOrUpdate` | `INSERT` | `contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Creates a new developer portal's content item specified by the provided content type. |
| `ContentItem_Delete` | `DELETE` | `If-Match, contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Removes the specified developer portal's content item. |
| `ContentItem_GetEntityTag` | `EXEC` | `contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId` | Returns the entity state (ETag) version of the developer portal's content item specified by its identifier. |
