---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - secrets
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.secrets.secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the secret. |
| <CopyableCode code="created" /> | `string` | The date when the secret was created. |
| <CopyableCode code="createdAt" /> | `number` | Timestamp for when the secret was created. |
| <CopyableCode code="decryptable" /> | `boolean` | Indicates whether the secret value can be decrypted after it has been created. |
| <CopyableCode code="projectId" /> | `string` | The unique identifier of the project which the secret belongs to. |
| <CopyableCode code="teamId" /> | `string` | The unique identifier of the team the secret was created for. |
| <CopyableCode code="uid" /> | `string` | The unique identifier of the secret. |
| <CopyableCode code="userId" /> | `string` | The unique identifier of the user who created the secret. |
| <CopyableCode code="value" /> | `string` | The value of the secret. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_secret" /> | `SELECT` | <CopyableCode code="idOrName, teamId" /> | Retrieves the information for a specific secret by passing either the secret id or name in the URL. |
| <CopyableCode code="get_secrets" /> | `SELECT` | <CopyableCode code="teamId" /> | Retrieves the active Vercel secrets for the authenticated user or team. By default it returns 20 secrets. The rest can be retrieved using the pagination options. The body will contain an entry for each secret. |
| <CopyableCode code="create_secret" /> | `INSERT` | <CopyableCode code="name, teamId, data__name, data__value" /> | Allows to create a new secret. |
| <CopyableCode code="delete_secret" /> | `DELETE` | <CopyableCode code="idOrName, teamId" /> | This deletes the user or team’s secret defined in the URL. |
| <CopyableCode code="_get_secrets" /> | `EXEC` | <CopyableCode code="teamId" /> | Retrieves the active Vercel secrets for the authenticated user or team. By default it returns 20 secrets. The rest can be retrieved using the pagination options. The body will contain an entry for each secret. |
| <CopyableCode code="rename_secret" /> | `EXEC` | <CopyableCode code="name, teamId, data__name" /> | Enables to edit the name of a secret. The name has to be unique to the user or team’s secrets. |
