---
title: project_service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - project_service_accounts
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

Creates, updates, deletes, gets or lists a <code>project_service_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.projects.project_service_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints |
| <CopyableCode code="name" /> | `string` | The name of the service account |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) of when the service account was created |
| <CopyableCode code="object" /> | `string` | The object type, which is always `organization.project.service_account` |
| <CopyableCode code="role" /> | `string` | `owner` or `member` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_project_service_accounts" /> | `SELECT` | <CopyableCode code="project_id" /> |  |
| <CopyableCode code="retrieve_project_service_account" /> | `SELECT` | <CopyableCode code="project_id, service_account_id" /> |  |
| <CopyableCode code="create_project_service_account" /> | `INSERT` | <CopyableCode code="project_id, data__name" /> |  |
| <CopyableCode code="delete_project_service_account" /> | `DELETE` | <CopyableCode code="project_id, service_account_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
created_at,
object,
role
FROM openai.projects.project_service_accounts
WHERE project_id = '{{ project_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project_service_accounts</code> resource.

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
INSERT INTO openai.projects.project_service_accounts (
data__name,
project_id
)
SELECT 
'{{ name }}',
'{{ project_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: project_service_accounts
  props:
    - name: project_id
      value: string
    - name: data__name
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>project_service_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM openai.projects.project_service_accounts
WHERE project_id = '{{ project_id }}'
AND service_account_id = '{{ service_account_id }}';
```
