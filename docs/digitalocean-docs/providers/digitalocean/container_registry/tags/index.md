---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.tags" /></td></tr>
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
| <CopyableCode code="registry_list_repositoryTags" /> | `SELECT` | <CopyableCode code="registry_name, repository_name" /> | To list all tags in your container registry repository, send a GET<br />request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`.<br /><br />Note that if your repository name contains `/` characters, it must be<br />URL-encoded in the request URL. For example, to list tags for<br />`registry.digitalocean.com/example/my/repo`, the path would be<br />`/v2/registry/example/repositories/my%2Frepo/tags`.<br /> |
| <CopyableCode code="registry_delete_repositoryTag" /> | `DELETE` | <CopyableCode code="registry_name, repository_name, repository_tag" /> | To delete a container repository tag, send a DELETE request to<br />`/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags/$TAG`.<br /><br />Note that if your repository name contains `/` characters, it must be<br />URL-encoded in the request URL. For example, to delete<br />`registry.digitalocean.com/example/my/repo:mytag`, the path would be<br />`/v2/registry/example/repositories/my%2Frepo/tags/mytag`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| <CopyableCode code="_registry_list_repositoryTags" /> | `EXEC` | <CopyableCode code="registry_name, repository_name" /> | To list all tags in your container registry repository, send a GET<br />request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`.<br /><br />Note that if your repository name contains `/` characters, it must be<br />URL-encoded in the request URL. For example, to list tags for<br />`registry.digitalocean.com/example/my/repo`, the path would be<br />`/v2/registry/example/repositories/my%2Frepo/tags`.<br /> |
