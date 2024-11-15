---
title: registry_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_repositories
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

Creates, updates, deletes, gets or lists a <code>registry_repositories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registry_repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the repository. |
| <CopyableCode code="latest_tag" /> | `object` |  |
| <CopyableCode code="registry_name" /> | `string` | The name of the container registry. |
| <CopyableCode code="tag_count" /> | `integer` | The number of tags in the repository. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_list_repositories" /> | `SELECT` | <CopyableCode code="registry_name" /> | This endpoint has been deprecated in favor of the _List All Container Registry Repositories [V2]_ endpoint. To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories`. |

## `SELECT` examples

This endpoint has been deprecated in favor of the _List All Container Registry Repositories [V2]_ endpoint. To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories`.


```sql
SELECT
name,
latest_tag,
registry_name,
tag_count
FROM digitalocean.container_registry.registry_repositories
WHERE registry_name = '{{ registry_name }}';
```