---
title: external_volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - external_volumes
  - external_volume
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>external_volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.external_volume.external_volumes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | String that specifies the identifier (the name) for the external volume; must be unique in your account. |
| <CopyableCode code="allow_writes" /> | `boolean` | Specifies whether write operations are allowed for the external volume; must be set to TRUE for Iceberg tables that use Snowflake as the catalog. |
| <CopyableCode code="comment" /> | `string` | String (literal) that specifies a comment for the external volume. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the external volume was created. |
| <CopyableCode code="owner" /> | `string` | Role that owns the external volume |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the external volume |
| <CopyableCode code="storage_locations" /> | `array` | Set of named cloud storage locations in different regions and, optionally, cloud platforms. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_external_volume" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetch an external volume |
| <CopyableCode code="list_external_volumes" /> | `SELECT` | <CopyableCode code="endpoint" /> | List external volumes |
| <CopyableCode code="create_external_volume" /> | `INSERT` | <CopyableCode code="data__name, data__storage_locations, endpoint" /> | Create an external volume |
| <CopyableCode code="delete_external_volume" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Delete an external volume |
| <CopyableCode code="undrop_external_volume" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | Undrop an external volume |

## `SELECT` examples

List external volumes


```sql
SELECT
name,
allow_writes,
comment,
created_on,
owner,
owner_role_type,
storage_locations
FROM snowflake.external_volume.external_volumes
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_volumes</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.external_volume.external_volumes (
data__storage_locations,
data__name,
endpoint
)
SELECT 
'{ name }',
'{ endpoint }',
'{ storage_locations }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: external_volumes
  props:
  - name: data__name
    value: string
  - name: data__storage_locations
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>external_volumes</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.external_volume.external_volumes
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```
