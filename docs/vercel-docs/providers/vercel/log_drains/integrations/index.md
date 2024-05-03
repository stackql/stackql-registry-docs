---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - log_drains
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
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.log_drains.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the log drain. Always prefixed with `ld_` |
| <CopyableCode code="name" /> | `string` | The name of the log drain |
| <CopyableCode code="branch" /> | `string` | The branch regexp of log drain |
| <CopyableCode code="clientId" /> | `string` | The oauth2 client application id that created this log drain |
| <CopyableCode code="configurationId" /> | `string` | The client configuration this log drain was created with |
| <CopyableCode code="createdAt" /> | `number` | A timestamp that tells you when the log drain was created |
| <CopyableCode code="createdFrom" /> | `string` | Whether the log drain was created by an integration or by a user |
| <CopyableCode code="deliveryFormat" /> | `string` | The delivery log format |
| <CopyableCode code="environment" /> | `string` | The environment of log drain |
| <CopyableCode code="headers" /> | `object` | The headers to send with the request |
| <CopyableCode code="ownerId" /> | `string` | The identifier of the team or user whose events will trigger the log drain |
| <CopyableCode code="projectId" /> | `string` |  |
| <CopyableCode code="projectIds" /> | `array` | The identifier of the projects this log drain is associated with |
| <CopyableCode code="sources" /> | `array` | The sources from which logs are currently being delivered to this log drain. |
| <CopyableCode code="url" /> | `string` | The URL to call when logs are generated |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_integration_log_drains" /> | `SELECT` | <CopyableCode code="teamId" /> | Retrieves a list of all Integration log drains that are defined for the authenticated user or team. When using an OAuth2 token, the list is limited to log drains created by the authenticated integration. |
| <CopyableCode code="create_log_drain" /> | `INSERT` | <CopyableCode code="teamId, data__name, data__url" /> | Creates an Integration log drain. This endpoint must be called with an OAuth2 client (integration), since log drains are tied to integrations. If it is called with a different token type it will produce a 400 error. |
| <CopyableCode code="delete_integration_log_drain" /> | `DELETE` | <CopyableCode code="id, teamId" /> | Deletes the Integration log drain with the provided `id`. When using an OAuth2 Token, the log drain can be deleted only if the integration owns it. |
