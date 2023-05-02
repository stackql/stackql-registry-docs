---
title: items
hide_title: false
hide_table_of_contents: false
keywords:
  - items
  - cloudsearch
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the Item. Format: datasources/&#123;source_id&#125;/items/&#123;item_id&#125; This is a required field. The maximum length is 1536 characters. |
| `queue` | `string` | Queue this item belongs to. The maximum length is 100 characters. |
| `content` | `object` | Content of an item to be indexed and surfaced by Cloud Search. Only UTF-8 encoded strings are allowed as inlineContent. If the content is uploaded and not binary, it must be UTF-8 encoded. |
| `structuredData` | `object` | Available structured data fields for the item. |
| `acl` | `object` | Access control list information for the item. For more information see [Map ACLs](https://developers.google.com/cloud-search/docs/guides/acls). |
| `itemType` | `string` | The type for this item. |
| `status` | `object` | This contains item's status and any errors. |
| `metadata` | `object` | Available metadata fields for the item. |
| `payload` | `string` | Additional state connector can store for this item. The maximum length is 10000 bytes. |
| `version` | `string` | Required. The indexing system stores the version from the datasource as a byte string and compares the Item version in the index to the version of the queued Item using lexical ordering. Cloud Search Indexing won't index or delete any queued item with a version value that is less than or equal to the version of the currently indexed item. The maximum length for this field is 1024 bytes. For information on how item version affects the deletion process, refer to [Handle revisions after manual deletes](https://developers.google.com/cloud-search/docs/guides/operations). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `indexing_datasources_items_get` | `SELECT` | `datasourcesId, itemsId` | Gets Item resource by item name. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `indexing_datasources_items_list` | `SELECT` | `datasourcesId` | Lists all or a subset of Item resources. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `indexing_datasources_items_delete` | `DELETE` | `datasourcesId, itemsId` | Deletes Item resource for the specified resource name. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `debug_datasources_items_checkAccess` | `EXEC` | `datasourcesId, itemsId` | Checks whether an item is accessible by specified principal. Principal must be a user; groups and domain values aren't supported. **Note:** This API requires an admin account to execute. |
| `debug_datasources_items_searchByViewUrl` | `EXEC` | `datasourcesId` | Fetches the item whose viewUrl exactly matches that of the URL provided in the request. **Note:** This API requires an admin account to execute. |
| `indexing_datasources_items_index` | `EXEC` | `datasourcesId, itemsId` | Updates Item ACL, metadata, and content. It will insert the Item if it does not exist. This method does not support partial updates. Fields with no provided values are cleared out in the Cloud Search index. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `indexing_datasources_items_poll` | `EXEC` | `datasourcesId` | Polls for unreserved items from the indexing queue and marks a set as reserved, starting with items that have the oldest timestamp from the highest priority ItemStatus. The priority order is as follows: ERROR MODIFIED NEW_ITEM ACCEPTED Reserving items ensures that polling from other threads cannot create overlapping sets. After handling the reserved items, the client should put items back into the unreserved state, either by calling index, or by calling push with the type REQUEUE. Items automatically become available (unreserved) after 4 hours even if no update or push method is called. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `indexing_datasources_items_push` | `EXEC` | `datasourcesId, itemsId` | Pushes an item onto a queue for later polling and updating. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `indexing_datasources_items_unreserve` | `EXEC` | `datasourcesId` | Unreserves all items from a queue, making them all eligible to be polled. This method is useful for resetting the indexing queue after a connector has been restarted. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
| `indexing_datasources_items_upload` | `EXEC` | `datasourcesId, itemsId` | Creates an upload session for uploading item content. For items smaller than 100 KB, it's easier to embed the content inline within an index request. This API requires an admin or service account to execute. The service account used is the one whitelisted in the corresponding data source. |
