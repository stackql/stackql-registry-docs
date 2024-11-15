---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - projects
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.projects.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_get" /> | `SELECT` | <CopyableCode code="project_id" /> | To get a project, send a GET request to `/v2/projects/$PROJECT_ID`. |
| <CopyableCode code="projects_list" /> | `SELECT` | <CopyableCode code="" /> | To list all your projects, send a GET request to `/v2/projects`. |
| <CopyableCode code="projects_create" /> | `INSERT` | <CopyableCode code="" /> | To create a project, send a POST request to `/v2/projects`. |
| <CopyableCode code="projects_delete" /> | `DELETE` | <CopyableCode code="project_id" /> | To delete a project, send a DELETE request to `/v2/projects/$PROJECT_ID`. To be deleted, a project must not have any resources assigned to it. Any existing resources must first be reassigned or destroyed, or you will receive a 412 error. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |
| <CopyableCode code="projects_patch" /> | `UPDATE` | <CopyableCode code="project_id" /> | To update only specific attributes of a project, send a PATCH request to `/v2/projects/$PROJECT_ID`. At least one of the following attributes needs to be sent. |
| <CopyableCode code="projects_update" /> | `EXEC` | <CopyableCode code="project_id" /> | To update a project, send a PUT request to `/v2/projects/$PROJECT_ID`. All of the following attributes must be sent. |

## `SELECT` examples

To list all your projects, send a GET request to `/v2/projects`.


```sql
SELECT
column_anon
FROM digitalocean.projects.projects
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
INSERT INTO digitalocean.projects.projects (

)
SELECT 

;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: projects
  props: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>projects</code> resource.

```sql
/*+ update */
UPDATE digitalocean.projects.projects
SET 
name = '{{ name }}',
description = '{{ description }}',
purpose = '{{ purpose }}',
environment = '{{ environment }}',
is_default = true|false
WHERE 
project_id = '{{ project_id }}';
```

## `DELETE` example

Deletes the specified <code>projects</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.projects.projects
WHERE project_id = '{{ project_id }}';
```
