---
title: buckets_object_list
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets_object_list
  - object_storage
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets_object_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.object_storage.buckets_object_list</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this object or prefix.<br /> |
| `next_marker` | `string` | Returns the value you should pass to the `marker` query parameter to get the next page of objects. If there is no next page, `null` will be returned.<br /> |
| `owner` | `string` | The owner of this object, as a UUID. `null` if this object represents a prefix.<br /> |
| `size` | `integer` | The size of this object, in bytes. `null` if this object represents a prefix.<br /> |
| `etag` | `string` | An MD-5 hash of the object. `null` if this object represents a prefix.<br /> |
| `is_truncated` | `boolean` | Designates if there is another page of bucket objects. |
| `last_modified` | `string` | The date and time this object was last modified. `null` if this object represents a prefix.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getObjectStorageBucketContent` | `SELECT` | `bucket, clusterId` |
| `_getObjectStorageBucketContent` | `EXEC` | `bucket, clusterId` |
