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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.secrets.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the secret. |
| `created` | `string` | The date when the secret was created. |
| `createdAt` | `number` | Timestamp for when the secret was created. |
| `decryptable` | `boolean` | Indicates whether the secret value can be decrypted after it has been created. |
| `projectId` | `string` | The unique identifier of the project which the secret belongs to. |
| `teamId` | `string` | The unique identifier of the team the secret was created for. |
| `uid` | `string` | The unique identifier of the secret. |
| `userId` | `string` | The unique identifier of the user who created the secret. |
| `value` | `string` | The value of the secret. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_secret` | `SELECT` | `idOrName, teamId` | Retrieves the information for a specific secret by passing either the secret id or name in the URL. |
| `get_secrets` | `SELECT` | `teamId` | Retrieves the active Vercel secrets for the authenticated user or team. By default it returns 20 secrets. The rest can be retrieved using the pagination options. The body will contain an entry for each secret. |
| `create_secret` | `INSERT` | `name, teamId, data__name, data__value` | Allows to create a new secret. |
| `delete_secret` | `DELETE` | `idOrName, teamId` | This deletes the user or team’s secret defined in the URL. |
| `_get_secrets` | `EXEC` | `teamId` | Retrieves the active Vercel secrets for the authenticated user or team. By default it returns 20 secrets. The rest can be retrieved using the pagination options. The body will contain an entry for each secret. |
| `rename_secret` | `EXEC` | `name, teamId, data__name` | Enables to edit the name of a secret. The name has to be unique to the user or team’s secrets. |
