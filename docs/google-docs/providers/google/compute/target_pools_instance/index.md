---
title: target_pools_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - target_pools_instance
  - compute
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>target_pools_instance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_pools_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_pools_instance" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_instance" /> | `INSERT` | <CopyableCode code="project, region, targetPool" /> | Adds an instance to a target pool. |
| <CopyableCode code="remove_instance" /> | `DELETE` | <CopyableCode code="project, region, targetPool" /> | Removes instance URL from a target pool. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>target_pools_instance</code> resource.

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
INSERT INTO google.compute.target_pools_instance (
project,
region,
targetPool,
instances
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ targetPool }}',
'{{ instances }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: instances
      value:
        - - name: instance
            value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>target_pools_instance</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.target_pools_instance
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND targetPool = '{{ targetPool }}';
```
