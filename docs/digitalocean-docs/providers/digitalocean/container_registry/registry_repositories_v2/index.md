---
title: registry_repositories_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_repositories_v2
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

Creates, updates, deletes, gets or lists a <code>registry_repositories_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_repositories_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registry_repositories_v2" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the repository. |
| <CopyableCode code="latest_manifest" /> | `object` |  |
| <CopyableCode code="manifest_count" /> | `integer` | The number of manifests in the repository. |
| <CopyableCode code="registry_name" /> | `string` | The name of the container registry. |
| <CopyableCode code="tag_count" /> | `integer` | The number of tags in the repository. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_list_repositories_v2" /> | `SELECT` | <CopyableCode code="registry_name" /> | To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositoriesV2`. |

## `SELECT` examples

To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositoriesV2`.


```sql
SELECT
name,
latest_manifest,
manifest_count,
registry_name,
tag_count
FROM digitalocean.container_registry.registry_repositories_v2
WHERE registry_name = '{{ registry_name }}';
```