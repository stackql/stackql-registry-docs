---
title: project_api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - project_api_keys
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
<tr><td><b>Name</b></td><td><code>project_api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.projects.project_api_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints |
| <CopyableCode code="name" /> | `string` | The name of the API key |
| <CopyableCode code="created_at" /> | `integer` | The Unix timestamp (in seconds) of when the API key was created |
| <CopyableCode code="object" /> | `string` | The object type, which is always `organization.project.api_key` |
| <CopyableCode code="owner" /> | `object` |  |
| <CopyableCode code="redacted_value" /> | `string` | The redacted value of the API key |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_project_api_keys" /> | `SELECT` | <CopyableCode code="project_id" /> |
| <CopyableCode code="retrieve_project_api_key" /> | `SELECT` | <CopyableCode code="key_id, project_id" /> |
| <CopyableCode code="delete_project_api_key" /> | `DELETE` | <CopyableCode code="key_id, project_id" /> |
