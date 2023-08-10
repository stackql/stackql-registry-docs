---
title: objects
hide_title: false
hide_table_of_contents: false
keywords:
  - objects
  - storage
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
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.objects</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bucket, object` | Retrieves an object or its metadata. |
| `list` | `SELECT` | `bucket` | Retrieves a list of objects matching the criteria. |
| `insert` | `INSERT` | `bucket` | Stores a new object and metadata. |
| `delete` | `DELETE` | `bucket, object` | Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used. |
| `_list` | `EXEC` | `bucket` | Retrieves a list of objects matching the criteria. |
| `compose` | `EXEC` | `destinationBucket, destinationObject` | Concatenates a list of existing objects into a new object in the same bucket. |
| `copy` | `EXEC` | `destinationBucket, destinationObject, sourceBucket, sourceObject` | Copies a source object to a destination object. Optionally overrides metadata. |
| `patch` | `EXEC` | `bucket, object` | Patches an object's metadata. |
| `rewrite` | `EXEC` | `destinationBucket, destinationObject, sourceBucket, sourceObject` | Rewrites a source object to a destination object. Optionally overrides metadata. |
| `update` | `EXEC` | `bucket, object` | Updates an object's metadata. |
| `watch_all` | `EXEC` | `bucket` | Watch for changes on all objects in a bucket. |
