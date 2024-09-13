---
title: apps_script_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_script_projects
  - integrations
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

Creates, updates, deletes or gets an <code>apps_script_project</code> resource or lists <code>apps_script_projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps_script_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.apps_script_projects" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apps_script_projects_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Apps Script project. |
| <CopyableCode code="projects_locations_apps_script_projects_link" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Links a existing Apps Script project. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apps_script_projects</code> resource.

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
INSERT INTO google.integrations.apps_script_projects (
locationsId,
projectsId,
authConfigId,
appsScriptProject
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ authConfigId }}',
'{{ appsScriptProject }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: authConfigId
        value: '{{ authConfigId }}'
      - name: appsScriptProject
        value: '{{ appsScriptProject }}'

```
</TabItem>
</Tabs>
