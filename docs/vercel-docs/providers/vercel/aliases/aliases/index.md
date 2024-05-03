---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
  - aliases
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
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.aliases.aliases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alias" /> | `string` | The alias name, it could be a `.vercel.app` subdomain or a custom domain |
| <CopyableCode code="created" /> | `string` | The date when the alias was created |
| <CopyableCode code="createdAt" /> | `number` | The date when the alias was created in milliseconds since the UNIX epoch |
| <CopyableCode code="creator" /> | `object` | Information of the user who created the alias |
| <CopyableCode code="deletedAt" /> | `number` | The date when the alias was deleted in milliseconds since the UNIX epoch |
| <CopyableCode code="deployment" /> | `object` | A map with the deployment ID, URL and metadata |
| <CopyableCode code="deploymentId" /> | `string` | The deployment ID |
| <CopyableCode code="projectId" /> | `string` | The unique identifier of the project |
| <CopyableCode code="protectionBypass" /> | `object` | The protection bypass for the alias |
| <CopyableCode code="redirect" /> | `string` | Target destination domain for redirect when the alias is a redirect |
| <CopyableCode code="redirectStatusCode" /> | `number` | Status code to be used on redirect |
| <CopyableCode code="uid" /> | `string` | The unique identifier of the alias |
| <CopyableCode code="updatedAt" /> | `number` | The date when the alias was updated in milliseconds since the UNIX epoch |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_alias" /> | `SELECT` | <CopyableCode code="idOrAlias, teamId" /> | Retrieves an Alias for the given host name or alias ID. |
| <CopyableCode code="list_aliases" /> | `SELECT` | <CopyableCode code="teamId" /> | Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases. |
| <CopyableCode code="delete_alias" /> | `DELETE` | <CopyableCode code="aliasId, teamId" /> | Delete an Alias with the specified ID. |
| <CopyableCode code="_list_aliases" /> | `EXEC` | <CopyableCode code="teamId" /> | Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases. |
