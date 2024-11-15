---
title: registry_repositories_digests
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_repositories_digests
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

Creates, updates, deletes, gets or lists a <code>registry_repositories_digests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_repositories_digests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registry_repositories_digests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobs" /> | `array` | All blobs associated with this manifest |
| <CopyableCode code="compressed_size_bytes" /> | `integer` | The compressed size of the manifest in bytes. |
| <CopyableCode code="digest" /> | `string` | The manifest digest |
| <CopyableCode code="registry_name" /> | `string` | The name of the container registry. |
| <CopyableCode code="repository" /> | `string` | The name of the repository. |
| <CopyableCode code="size_bytes" /> | `integer` | The uncompressed size of the manifest in bytes (this size is calculated asynchronously so it may not be immediately available). |
| <CopyableCode code="tags" /> | `array` | All tags associated with this manifest |
| <CopyableCode code="updated_at" /> | `string` | The time the manifest was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_list_repository_manifests" /> | `SELECT` | <CopyableCode code="registry_name, repository_name" /> | To list all manifests in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/digests`. Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list manifests for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/digests`. |
| <CopyableCode code="registry_delete_repository_manifest" /> | `DELETE` | <CopyableCode code="manifest_digest, registry_name, repository_name" /> | To delete a container repository manifest by digest, send a DELETE request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/digests/$MANIFEST_DIGEST`. Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to delete `registry.digitalocean.com/example/my/repo@sha256:abcd`, the path would be `/v2/registry/example/repositories/my%2Frepo/digests/sha256:abcd`. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |

## `SELECT` examples

To list all manifests in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/digests`. Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list manifests for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/digests`.


```sql
SELECT
blobs,
compressed_size_bytes,
digest,
registry_name,
repository,
size_bytes,
tags,
updated_at
FROM digitalocean.container_registry.registry_repositories_digests
WHERE registry_name = '{{ registry_name }}'
AND repository_name = '{{ repository_name }}';
```
## `DELETE` example

Deletes the specified <code>registry_repositories_digests</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.container_registry.registry_repositories_digests
WHERE manifest_digest = '{{ manifest_digest }}'
AND registry_name = '{{ registry_name }}'
AND repository_name = '{{ repository_name }}';
```
