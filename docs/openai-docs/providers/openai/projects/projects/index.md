---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - projects
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.projects.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints |
| <CopyableCode code="name" /> | `string` | The name of the project. This appears in reporting. |
| <CopyableCode code="archived_at" /> | `integer` | The Unix timestamp (in seconds) of when the project was archived or `null`. |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) of when the project was created. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `organization.project` |
| <CopyableCode code="status" /> | `string` | `active` or `archived` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_projects" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="retrieve_project" /> | `SELECT` | <CopyableCode code="project_id" /> |  |
| <CopyableCode code="create_project" /> | `INSERT` | <CopyableCode code="data__name" /> |  |
| <CopyableCode code="modify_project" /> | `UPDATE` | <CopyableCode code="project_id, data__name" /> |  |
| <CopyableCode code="archive_project" /> | `EXEC` | <CopyableCode code="project_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
archived_at,
created_at,
object,
status
FROM openai.projects.projects
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>projects</code> resource.

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
INSERT INTO openai.projects.projects (
data__name
)
SELECT 
'{{ name }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: projects
  props:
    - name: data__name
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>projects</code> resource.

```sql
/*+ update */
UPDATE openai.projects.projects
SET 
name = '{{ name }}'
WHERE 
project_id = '{{ project_id }}'
AND data__name = '{{ data__name }}';
```
