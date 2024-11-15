---
title: logsinks
hide_title: false
hide_table_of_contents: false
keywords:
  - logsinks
  - databases
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

Creates, updates, deletes, gets or lists a <code>logsinks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logsinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.logsinks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_get_logsink" /> | `SELECT` | <CopyableCode code="database_cluster_uuid, logsink_id" /> | To get a logsink for a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/logsink/$LOGSINK_ID`. |
| <CopyableCode code="databases_list_logsink" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list logsinks for a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/logsink`. |
| <CopyableCode code="databases_create_logsink" /> | `INSERT` | <CopyableCode code="database_cluster_uuid" /> | To create logsink for a database cluster, send a POST request to `/v2/databases/$DATABASE_ID/logsink`. |
| <CopyableCode code="databases_delete_logsink" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, logsink_id" /> | To delete a logsink for a database cluster, send a DELETE request to `/v2/databases/$DATABASE_ID/logsink/$LOGSINK_ID`. |
| <CopyableCode code="databases_update_logsink" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, logsink_id, data__config" /> | To update a logsink for a database cluster, send a PUT request to `/v2/databases/$DATABASE_ID/logsink/$LOGSINK_ID`. |

## `SELECT` examples

To list logsinks for a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/logsink`.


```sql
SELECT
column_anon
FROM digitalocean.databases.logsinks
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logsinks</code> resource.

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
INSERT INTO digitalocean.databases.logsinks (
database_cluster_uuid
)
SELECT 
'{{ database_cluster_uuid }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: logsinks
  props:
    - name: database_cluster_uuid
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>logsinks</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.logsinks
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND logsink_id = '{{ logsink_id }}';
```
