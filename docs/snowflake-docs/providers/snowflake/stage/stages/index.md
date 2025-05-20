---
title: stages
hide_title: false
hide_table_of_contents: false
keywords:
  - stages
  - stage
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

Creates, updates, deletes, gets or lists a <code>stages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.stage.stages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="cloud" /> | `string` | Cloud provider; always NULL for an internal stage. |
| <CopyableCode code="comment" /> | `string` | Specifies a comment for the stage. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the stage was created. |
| <CopyableCode code="credentials" /> | `object` | Specifies the credentials of the stage. |
| <CopyableCode code="directory_table" /> | `object` | Directory table parameters of the stage. |
| <CopyableCode code="encryption" /> | `object` | Encryption parameters of the stage. |
| <CopyableCode code="endpoint" /> | `string` | The S3-compatible API endpoint associated with the stage; always NULL for stages that are not S3-compatible. |
| <CopyableCode code="has_credentials" /> | `boolean` | Indicates that the external stage has access credentials; always false for an internal stage. |
| <CopyableCode code="has_encryption_key" /> | `boolean` | Indicates that the external stage contains encrypted files; always false for an internal stage. |
| <CopyableCode code="kind" /> | `string` | Specifies whether the stage is permanent or temporary. |
| <CopyableCode code="owner" /> | `string` | Role that owns the stage. |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the object, either ROLE or DATABASE_ROLE. If a Snowflake Native App owns the object, the value is APPLICATION. Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| <CopyableCode code="region" /> | `string` | Region where the stage is located. |
| <CopyableCode code="storage_integration" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="url" /> | `string` | URL for the external stage; blank for an internal stage. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_stage" /> | `SELECT` | <CopyableCode code="database, name, schema, endpoint" /> | Fetch a stage using the describe command output. |
| <CopyableCode code="list_stages" /> | `SELECT` | <CopyableCode code="database, schema, endpoint" /> | Lists stages under the database and schema, with show options as query parameters. |
| <CopyableCode code="create_stage" /> | `INSERT` | <CopyableCode code="database, schema, data__name, endpoint" /> | Create a stage, with standard create modifiers as query parameters. See the Stage component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_stage" /> | `DELETE` | <CopyableCode code="database, name, schema, endpoint" /> | Delete a stage with the stage name. If ifExists is used, the operation will succeed even if the object does not exist. Otherwise, there will be a failure if the drop is unsuccessful. |

## `SELECT` examples

Lists stages under the database and schema, with show options as query parameters.


```sql
SELECT
name,
cloud,
comment,
created_on,
credentials,
directory_table,
encryption,
endpoint,
has_credentials,
has_encryption_key,
kind,
owner,
owner_role_type,
region,
storage_integration,
url
FROM snowflake.stage.stages
WHERE database = '{{ database }}' AND schema = '{{ schema }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>stages</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.stage.stages (
data__name,
endpoint,
schema,
database
)
SELECT 
'{ endpoint }',
'{ name }',
'{ database }',
'{ schema }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: stages
  props:
  - name: database
    value: string
  - name: schema
    value: string
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>stages</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.stage.stages
WHERE database = '{ database }' AND name = '{ name }' AND schema = '{ schema }' AND endpoint = '{ endpoint }';
```
