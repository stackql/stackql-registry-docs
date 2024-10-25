---
title: project_service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - project_service_accounts
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_project_service_accounts" /> | `SELECT` | <CopyableCode code="project_id" /> |
| <CopyableCode code="retrieve_project_service_account" /> | `SELECT` | <CopyableCode code="project_id, service_account_id" /> |
| <CopyableCode code="create_project_service_account" /> | `INSERT` | <CopyableCode code="project_id, data__name" /> |
| <CopyableCode code="delete_project_service_account" /> | `DELETE` | <CopyableCode code="project_id, service_account_id" /> |
