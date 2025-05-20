---
title: api_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - api_integrations
  - api_integration
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

Creates, updates, deletes, gets or lists a <code>api_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.api_integration.api_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the API integration. |
| <CopyableCode code="api_allowed_prefixes" /> | `array` | A comma-separated list of endpoints and resources that Snowflake can access. |
| <CopyableCode code="api_blocked_prefixes" /> | `array` | A comma-separated list of endpoints and resources that are not allowed to be called from Snowflake. |
| <CopyableCode code="api_hook" /> | `object` |  |
| <CopyableCode code="comment" /> | `string` | Comment for the API integration. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the API integration was created. |
| <CopyableCode code="enabled" /> | `boolean` | Whether the API integration is enabled. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_api_integration" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetch an API integration |
| <CopyableCode code="list_api_integrations" /> | `SELECT` | <CopyableCode code="endpoint" /> | List API integrations |
| <CopyableCode code="create_api_integration" /> | `INSERT` | <CopyableCode code="data__api_allowed_prefixes, data__api_hook, data__enabled, data__name, endpoint" /> | Create an API integration |
| <CopyableCode code="delete_api_integration" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Delete an API integration |
| <CopyableCode code="create_or_alter_api_integration" /> | `REPLACE` | <CopyableCode code="name, data__api_allowed_prefixes, data__api_hook, data__enabled, data__name, endpoint" /> | Create an (or alter an existing) API integration. Note that API_KEY is not currently altered by this operation and is supported for a newly-created object only. Unsetting API_BLOCKED_PREFIXES is also unsupported. |

## `SELECT` examples

List API integrations


```sql
SELECT
name,
api_allowed_prefixes,
api_blocked_prefixes,
api_hook,
comment,
created_on,
enabled
FROM snowflake.api_integration.api_integrations
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_integrations</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.api_integration.api_integrations (
data__name,
endpoint,
data__api_hook,
data__api_allowed_prefixes,
data__enabled
)
SELECT 
'{ endpoint }',
'{ enabled }',
'{ api_allowed_prefixes }',
'{ name }',
'{ api_hook }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: api_integrations
  props:
  - name: data__api_allowed_prefixes
    value: string
  - name: data__api_hook
    value: string
  - name: data__enabled
    value: string
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>api_integrations</code> resource.

```sql
/*+ update */
REPLACE snowflake.api_integration.api_integrations
SET 

WHERE 
name = '{ name }' AND data__api_allowed_prefixes = '{ data__api_allowed_prefixes }' AND data__api_hook = '{ data__api_hook }' AND data__enabled = '{ data__enabled }' AND data__name = '{ data__name }' AND endpoint = '{ endpoint }';
```

## `DELETE` example

Deletes the specified <code>api_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.api_integration.api_integrations
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```
