---
title: env
hide_title: false
hide_table_of_contents: false
keywords:
  - env
  - projects
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>env</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.projects.env" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="configurationId" /> | `string` |  |
| <CopyableCode code="contentHint" /> | `` |  |
| <CopyableCode code="createdAt" /> | `number` |  |
| <CopyableCode code="createdBy" /> | `string` |  |
| <CopyableCode code="decrypted" /> | `boolean` | Whether `value` is decrypted. |
| <CopyableCode code="edgeConfigId" /> | `string` |  |
| <CopyableCode code="edgeConfigTokenId" /> | `string` |  |
| <CopyableCode code="gitBranch" /> | `string` |  |
| <CopyableCode code="key" /> | `string` |  |
| <CopyableCode code="target" /> | `` |  |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updatedAt" /> | `number` |  |
| <CopyableCode code="updatedBy" /> | `string` |  |
| <CopyableCode code="value" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project_env" /> | `SELECT` | <CopyableCode code="id, idOrName, teamId" /> | Retrieve the environment variable for a given project. |
| <CopyableCode code="create_project_env" /> | `INSERT` | <CopyableCode code="idOrName, teamId" /> | Create one ore more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. |
| <CopyableCode code="remove_project_env" /> | `DELETE` | <CopyableCode code="id, idOrName, teamId" /> | Delete a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL. |
| <CopyableCode code="edit_project_env" /> | `EXEC` | <CopyableCode code="id, idOrName, teamId" /> | Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL. |
| <CopyableCode code="filter_project_envs" /> | `EXEC` | <CopyableCode code="idOrName, teamId" /> | Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL. |
