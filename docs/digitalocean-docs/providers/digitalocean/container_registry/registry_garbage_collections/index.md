---
title: registry_garbage_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_garbage_collections
  - container_registry
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>registry_garbage_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_garbage_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registry_garbage_collections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobs_deleted" /> | `integer` | The number of blobs deleted as a result of this garbage collection. |
| <CopyableCode code="created_at" /> | `string` | The time the garbage collection was created. |
| <CopyableCode code="freed_bytes" /> | `integer` | The number of bytes freed as a result of this garbage collection. |
| <CopyableCode code="registry_name" /> | `string` | The name of the container registry. |
| <CopyableCode code="status" /> | `string` | The current status of this garbage collection. |
| <CopyableCode code="updated_at" /> | `string` | The time the garbage collection was last updated. |
| <CopyableCode code="uuid" /> | `string` | A string specifying the UUID of the garbage collection. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_list_garbage_collections" /> | `SELECT` | <CopyableCode code="registry_name" /> | To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`. |
| <CopyableCode code="registry_get_garbage_collection" /> | `EXEC` | <CopyableCode code="registry_name" /> | To get information about the currently-active garbage collection for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collection`. |
| <CopyableCode code="registry_run_garbage_collection" /> | `EXEC` | <CopyableCode code="registry_name" /> | Garbage collection enables users to clear out unreferenced blobs (layer & manifest data) after deleting one or more manifests from a repository. If there are no unreferenced blobs resulting from the deletion of one or more manifests, garbage collection is effectively a noop. [See here for more information](https://docs.digitalocean.com/products/container-registry/how-to/clean-up-container-registry/) about how and why you should clean up your container registry periodically. To request a garbage collection run on your registry, send a POST request to `/v2/registry/$REGISTRY_NAME/garbage-collection`. This will initiate the following sequence of events on your registry. * Set the registry to read-only mode, meaning no further write-scoped JWTs will be issued to registry clients. Existing write-scoped JWTs will continue to work until they expire which can take up to 15 minutes. * Wait until all existing write-scoped JWTs have expired. * Scan all registry manifests to determine which blobs are unreferenced. * Delete all unreferenced blobs from the registry. * Record the number of blobs deleted and bytes freed, mark the garbage collection status as `success`. * Remove the read-only mode restriction from the registry, meaning write-scoped JWTs will once again be issued to registry clients. |
| <CopyableCode code="registry_update_garbage_collection" /> | `EXEC` | <CopyableCode code="garbage_collection_uuid, registry_name" /> | To cancel the currently-active garbage collection for a registry, send a PUT request to `/v2/registry/$REGISTRY_NAME/garbage-collection/$GC_UUID` and specify one or more of the attributes below. |

## `SELECT` examples

To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`.


```sql
SELECT
blobs_deleted,
created_at,
freed_bytes,
registry_name,
status,
updated_at,
uuid
FROM digitalocean.container_registry.registry_garbage_collections
WHERE registry_name = '{{ registry_name }}';
```