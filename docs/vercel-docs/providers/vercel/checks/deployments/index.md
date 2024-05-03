---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - checks
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.checks.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="blocking" /> | `boolean` |
| <CopyableCode code="completedAt" /> | `number` |
| <CopyableCode code="conclusion" /> | `string` |
| <CopyableCode code="createdAt" /> | `number` |
| <CopyableCode code="deploymentId" /> | `string` |
| <CopyableCode code="detailsUrl" /> | `string` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="integrationId" /> | `string` |
| <CopyableCode code="output" /> | `object` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="rerequestable" /> | `boolean` |
| <CopyableCode code="startedAt" /> | `number` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="updatedAt" /> | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_checks" /> | `SELECT` | <CopyableCode code="deploymentId, teamId" /> | List all of the checks created for a deployment. |
| <CopyableCode code="get_check" /> | `SELECT` | <CopyableCode code="checkId, deploymentId, teamId" /> | Return a detailed response for a single check. |
| <CopyableCode code="create_check" /> | `INSERT` | <CopyableCode code="deploymentId, teamId, data__blocking, data__name" /> | Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error. |
| <CopyableCode code="_get_all_checks" /> | `EXEC` | <CopyableCode code="deploymentId, teamId" /> | List all of the checks created for a deployment. |
| <CopyableCode code="rerequest_check" /> | `EXEC` | <CopyableCode code="checkId, deploymentId, teamId" /> | Rerequest a selected check that has failed. |
| <CopyableCode code="update_check" /> | `EXEC` | <CopyableCode code="checkId, deploymentId, teamId" /> | Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error. |
