---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
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

Creates, updates, deletes, gets or lists a <code>registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.container_registry.registries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="registry_get" /> | `SELECT` | <CopyableCode code="" /> | To get information about your container registry, send a GET request to `/v2/registry`. |
| <CopyableCode code="registry_create" /> | `INSERT` | <CopyableCode code="data__name, data__subscription_tier_slug" /> | To create your container registry, send a POST request to `/v2/registry`. The `name` becomes part of the URL for images stored in the registry. For example, if your registry is called `example`, an image in it will have the URL `registry.digitalocean.com/example/image:tag`. |
| <CopyableCode code="registry_delete" /> | `DELETE` | <CopyableCode code="" /> | To delete your container registry, destroying all container image data stored in it, send a DELETE request to `/v2/registry`. |
| <CopyableCode code="registry_validate_name" /> | `EXEC` | <CopyableCode code="data__name" /> | To validate that a container registry name is available for use, send a POST request to `/v2/registry/validate-name`. If the name is both formatted correctly and available, the response code will be 204 and contain no body. If the name is already in use, the response will be a 409 Conflict. |

## `SELECT` examples

To get information about your container registry, send a GET request to `/v2/registry`.


```sql
SELECT
column_anon
FROM digitalocean.container_registry.registries
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registries</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.container_registry.registries (
data__name,
data__subscription_tier_slug,
data__region
)
SELECT 
'{{ name }}',
'{{ subscription_tier_slug }}',
'{{ region }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.container_registry.registries (
data__name,
data__subscription_tier_slug
)
SELECT 
'{{ name }}',
'{{ subscription_tier_slug }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: registries
  props:
    - name: data__name
      value: string
    - name: data__subscription_tier_slug
      value: string
    - name: name
      value: string
    - name: subscription_tier_slug
      value: string
    - name: region
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registries</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.container_registry.registries
WHERE  = '{{  }}';
```
