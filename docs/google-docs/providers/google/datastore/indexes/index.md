---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
  - datastore
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastore.indexes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `array` | Required. An ordered sequence of property names and their index attributes. |
| `state` | `string` | Output only. The state of the index. |
| `ancestor` | `string` | Required. The index's ancestor mode. Must not be ANCESTOR_MODE_UNSPECIFIED. |
| `indexId` | `string` | Output only. The resource ID of the index. |
| `kind` | `string` | Required. The entity kind to which this index applies. |
| `projectId` | `string` | Output only. Project ID. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_indexes_get` | `SELECT` | `indexId, projectId` | Gets an index. |
| `projects_indexes_list` | `SELECT` | `projectId` | Lists the indexes that match the specified filters. Datastore uses an eventually consistent query to fetch the list of indexes and may occasionally return stale results. |
| `projects_indexes_create` | `INSERT` | `projectId` | Creates the specified index. A newly created index's initial state is `CREATING`. On completion of the returned google.longrunning.Operation, the state will be `READY`. If the index already exists, the call will return an `ALREADY_EXISTS` status. During index creation, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, removing the index with delete, then re-creating the index with create. Indexes with a single property cannot be created. |
| `projects_indexes_delete` | `DELETE` | `indexId, projectId` | Deletes an existing index. An index can only be deleted if it is in a `READY` or `ERROR` state. On successful execution of the request, the index will be in a `DELETING` state. And on completion of the returned google.longrunning.Operation, the index will be removed. During index deletion, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, followed by calling delete again. |
