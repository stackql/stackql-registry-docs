---
title: garbage_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - garbage_collection
  - container_registry
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>garbage_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.container_registry.garbage_collection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `uuid` | `string` | A string specifying the UUID of the garbage collection. |
| `blobs_deleted` | `integer` | The number of blobs deleted as a result of this garbage collection. |
| `created_at` | `string` | The time the garbage collection was created. |
| `freed_bytes` | `integer` | The number of bytes freed as a result of this garbage collection. |
| `registry_name` | `string` | The name of the container registry. |
| `status` | `string` | The current status of this garbage collection. |
| `updated_at` | `string` | The time the garbage collection was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `registry_list_garbageCollections` | `SELECT` | `registry_name` | To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`. |
| `_registry_get_garbageCollection` | `EXEC` | `registry_name` | To get information about the currently-active garbage collection for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collection`. |
| `_registry_list_garbageCollections` | `EXEC` | `registry_name` | To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`. |
| `registry_get_garbageCollection` | `EXEC` | `registry_name` | To get information about the currently-active garbage collection for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collection`. |
| `registry_run_garbageCollection` | `EXEC` | `registry_name` | Garbage collection enables users to clear out unreferenced blobs (layer &<br />manifest data) after deleting one or more manifests from a repository. If<br />there are no unreferenced blobs resulting from the deletion of one or more<br />manifests, garbage collection is effectively a noop.<br />[See here for more information](https://www.digitalocean.com/docs/container-registry/how-to/clean-up-container-registry/)<br />about how and why you should clean up your container registry periodically.<br /><br />To request a garbage collection run on your registry, send a POST request to<br />`/v2/registry/$REGISTRY_NAME/garbage-collection`. This will initiate the<br />following sequence of events on your registry.<br /><br />* Set the registry to read-only mode, meaning no further write-scoped<br />  JWTs will be issued to registry clients. Existing write-scoped JWTs will<br />  continue to work until they expire which can take up to 15 minutes.<br />* Wait until all existing write-scoped JWTs have expired.<br />* Scan all registry manifests to determine which blobs are unreferenced.<br />* Delete all unreferenced blobs from the registry.<br />* Record the number of blobs deleted and bytes freed, mark the garbage<br />  collection status as `success`.<br />* Remove the read-only mode restriction from the registry, meaning write-scoped<br />  JWTs will once again be issued to registry clients.<br /> |
| `registry_update_garbageCollection` | `EXEC` | `garbage_collection_uuid, registry_name` | To cancel the currently-active garbage collection for a registry, send a PUT request to `/v2/registry/$REGISTRY_NAME/garbage-collection/$GC_UUID` and specify one or more of the attributes below. |
