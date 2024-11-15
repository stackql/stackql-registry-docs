---
title: volumes_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_snapshots
  - block_storage
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

Creates, updates, deletes, gets or lists a <code>volumes_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.block_storage.volumes_snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="volume_snapshots_get_by_id" /> | `SELECT` | <CopyableCode code="snapshot_id" /> | To retrieve the details of a snapshot that has been created from a volume, send a GET request to `/v2/volumes/snapshots/$VOLUME_SNAPSHOT_ID`. |
| <CopyableCode code="volume_snapshots_list" /> | `SELECT` | <CopyableCode code="volume_id" /> | To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`. |
| <CopyableCode code="volume_snapshots_create" /> | `INSERT` | <CopyableCode code="volume_id, data__name" /> | To create a snapshot from a volume, sent a POST request to `/v2/volumes/$VOLUME_ID/snapshots`. |
| <CopyableCode code="volume_snapshots_delete_by_id" /> | `DELETE` | <CopyableCode code="snapshot_id" /> | To delete a volume snapshot, send a DELETE request to `/v2/volumes/snapshots/$VOLUME_SNAPSHOT_ID`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |

## `SELECT` examples

To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`.


```sql
SELECT
column_anon
FROM digitalocean.block_storage.volumes_snapshots
WHERE volume_id = '{{ volume_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes_snapshots</code> resource.

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
INSERT INTO digitalocean.block_storage.volumes_snapshots (
data__name,
data__tags,
volume_id
)
SELECT 
'{{ name }}',
'{{ tags }}',
'{{ volume_id }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.block_storage.volumes_snapshots (
data__name,
volume_id
)
SELECT 
'{{ name }}',
'{{ volume_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: volumes_snapshots
  props:
    - name: volume_id
      value: string
    - name: data__name
      value: string
    - name: name
      value: string
    - name: tags
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volumes_snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.block_storage.volumes_snapshots
WHERE snapshot_id = '{{ snapshot_id }}';
```
