---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - kubernetes
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
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.registries" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_add_registry" /> | `INSERT` | <CopyableCode code="" /> | To integrate the container registry with Kubernetes clusters, send a POST request to `/v2/kubernetes/registry`. |
| <CopyableCode code="kubernetes_remove_registry" /> | `DELETE` | <CopyableCode code="" /> | To remove the container registry from Kubernetes clusters, send a DELETE request to `/v2/kubernetes/registry`. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registries</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.kubernetes.registries (
data__cluster_uuids
)
SELECT 
'{{ cluster_uuids }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: registries
  props:
    - name: cluster_uuids
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registries</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.kubernetes.registries
WHERE  = '{{  }}';
```
