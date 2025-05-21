---
title: notebooks
hide_title: false
hide_table_of_contents: false
keywords:
  - notebooks
  - notebook
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

Creates, updates, deletes, gets or lists a <code>notebooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.notebook.notebooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the notebook |
| <CopyableCode code="budget" /> | `string` | Name of the budget if the notebook is monitored by a budget |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="compute_pool" /> | `string` | Compute pool name where the snowservice runs |
| <CopyableCode code="created_on" /> | `string` | Date and time when the notebook was created. |
| <CopyableCode code="database_name" /> | `string` | Database in which the notebook is stored |
| <CopyableCode code="default_packages" /> | `string` | Default packages of the notebook |
| <CopyableCode code="default_version" /> | `string` | The default version name of a file based entity. |
| <CopyableCode code="default_version_details" /> | `object` | The version details of a file based entity |
| <CopyableCode code="external_access_integrations" /> | `array` | List of external access integrations attached to this function |
| <CopyableCode code="external_access_secrets" /> | `string` | Secrets to be used with this function for external access |
| <CopyableCode code="fromLocation" /> | `string` | Location to copy the file from. This must be a Snowflake stage location. |
| <CopyableCode code="idle_auto_shutdown_time_seconds" /> | `integer` | Sets the time in seconds for when to shutdown an idle Notebook. |
| <CopyableCode code="import_urls" /> | `array` | List of urls |
| <CopyableCode code="last_version_details" /> | `object` | The version details of a file based entity |
| <CopyableCode code="live_version_location_uri" /> | `string` | The current version location |
| <CopyableCode code="main_file" /> | `string` | Name + path of the file for the Notebook |
| <CopyableCode code="owner" /> | `string` | Role that owns the notebook |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the notebook |
| <CopyableCode code="query_warehouse" /> | `string` | Warehouse against which the queries issued by the Streamlit app are run against |
| <CopyableCode code="runtime_name" /> | `string` | The runtime to run the Streamlit or Notebook on. If this is not set, the warehouse is assumed |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the notebook is stored |
| <CopyableCode code="title" /> | `string` | User facing title of the Streamlit app or an Organization Profile |
| <CopyableCode code="url_id" /> | `string` | Unique ID associated with the notebook object. |
| <CopyableCode code="user_packages" /> | `string` | User packages of the notebook |
| <CopyableCode code="version" /> | `string` | User specified version alias |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_notebook" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Fetch a notebook |
| <CopyableCode code="list_notebooks" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | List notebooks |
| <CopyableCode code="create_notebook" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | Create a notebook |
| <CopyableCode code="delete_notebook" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Delete a notebook |
| <CopyableCode code="add_live_version_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Adds a LIVE version to the notebook |
| <CopyableCode code="commit_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | If a Git connection is set up for the notebook, commits the LIVE version of the notebook to the Git repository |
| <CopyableCode code="execute_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Execute a Notebook |
| <CopyableCode code="rename_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetName, endpoint" /> | Changes the name of the notebook to new name. The new identifier must be unique for the schema. |

## `SELECT` examples

List notebooks


```sql
SELECT
name,
budget,
comment,
compute_pool,
created_on,
database_name,
default_packages,
default_version,
default_version_details,
external_access_integrations,
external_access_secrets,
fromLocation,
idle_auto_shutdown_time_seconds,
import_urls,
last_version_details,
live_version_location_uri,
main_file,
owner,
owner_role_type,
query_warehouse,
runtime_name,
schema_name,
title,
url_id,
user_packages,
version
FROM snowflake.notebook.notebooks
WHERE database_name = '{{ database_name }}' AND schema_name = '{{ schema_name }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notebooks</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.notebook.notebooks (
database_name,
data__name,
schema_name,
endpoint
)
SELECT 
'{ endpoint }',
'{ database_name }',
'{ name }',
'{ schema_name }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: notebooks
  props:
  - name: database_name
    value: string
  - name: schema_name
    value: string
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notebooks</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.notebook.notebooks
WHERE database_name = '{ database_name }' AND name = '{ name }' AND schema_name = '{ schema_name }' AND endpoint = '{ endpoint }';
```
