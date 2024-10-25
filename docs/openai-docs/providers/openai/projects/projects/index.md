---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - projects
  - openai    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage OpenAI and ChatGPT resources using SQL.
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_projects" /> | `SELECT` |  |
| <CopyableCode code="retrieve_project" /> | `SELECT` | <CopyableCode code="project_id" /> |
| <CopyableCode code="create_project" /> | `INSERT` | <CopyableCode code="data__name" /> |
| <CopyableCode code="modify_project" /> | `UPDATE` | <CopyableCode code="project_id, data__name" /> |
| <CopyableCode code="archive_project" /> | `EXEC` | <CopyableCode code="project_id" /> |
