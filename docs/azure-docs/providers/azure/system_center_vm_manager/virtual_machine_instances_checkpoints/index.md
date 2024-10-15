---
title: virtual_machine_instances_checkpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances_checkpoints
  - system_center_vm_manager
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_instances_checkpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_instances_checkpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.virtual_machine_instances_checkpoints" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceUri" /> | Creates a checkpoint in virtual machine instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | Deletes a checkpoint in virtual machine instance. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_instances_checkpoints</code> resource.

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
INSERT INTO azure.system_center_vm_manager.virtual_machine_instances_checkpoints (
resourceUri,
name,
description
)
SELECT 
'{{ resourceUri }}',
'{{ name }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_machine_instances_checkpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.system_center_vm_manager.virtual_machine_instances_checkpoints
WHERE resourceUri = '{{ resourceUri }}';
```
