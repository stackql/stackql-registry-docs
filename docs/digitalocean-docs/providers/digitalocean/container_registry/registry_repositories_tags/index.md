---
title: registry_repositories_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_repositories_tags
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

Creates, updates, deletes, gets or lists a <code>registry_repositories_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_repositories_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registry_repositories_tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="compressed_size_bytes" /> | `integer` | The compressed size of the tag in bytes. |
| <CopyableCode code="manifest_digest" /> | `string` | The digest of the manifest associated with the tag. |
| <CopyableCode code="registry_name" /> | `string` | The name of the container registry. |
| <CopyableCode code="repository" /> | `string` | The name of the repository. |
| <CopyableCode code="size_bytes" /> | `integer` | The uncompressed size of the tag in bytes (this size is calculated asynchronously so it may not be immediately available). |
| <CopyableCode code="tag" /> | `string` | The name of the tag. |
| <CopyableCode code="updated_at" /> | `string` | The time the tag was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_list_repository_tags" /> | `SELECT` | <CopyableCode code="registry_name, repository_name" /> | To list all tags in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`. Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list tags for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags`. |
| <CopyableCode code="registry_delete_repository_tag" /> | `DELETE` | <CopyableCode code="registry_name, repository_name, repository_tag" /> | To delete a container repository tag, send a DELETE request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags/$TAG`. Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to delete `registry.digitalocean.com/example/my/repo:mytag`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags/mytag`. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |

## `SELECT` examples

To list all tags in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`. Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list tags for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags`.


```sql
SELECT
compressed_size_bytes,
manifest_digest,
registry_name,
repository,
size_bytes,
tag,
updated_at
FROM digitalocean.container_registry.registry_repositories_tags
WHERE registry_name = '{{ registry_name }}'
AND repository_name = '{{ repository_name }}';
```
## `DELETE` example

Deletes the specified <code>registry_repositories_tags</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.container_registry.registry_repositories_tags
WHERE registry_name = '{{ registry_name }}'
AND repository_name = '{{ repository_name }}'
AND repository_tag = '{{ repository_tag }}';
```
