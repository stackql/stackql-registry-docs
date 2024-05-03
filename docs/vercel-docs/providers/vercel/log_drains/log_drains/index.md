---
title: log_drains
hide_title: false
hide_table_of_contents: false
keywords:
  - log_drains
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
<tr><td><b>Name</b></td><td><code>log_drains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.log_drains.log_drains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="branch" /> | `string` |
| <CopyableCode code="clientId" /> | `string` |
| <CopyableCode code="configurationId" /> | `string` |
| <CopyableCode code="createdAt" /> | `number` |
| <CopyableCode code="createdFrom" /> | `string` |
| <CopyableCode code="deliveryFormat" /> | `string` |
| <CopyableCode code="disabledAt" /> | `number` |
| <CopyableCode code="disabledBy" /> | `string` |
| <CopyableCode code="disabledReason" /> | `string` |
| <CopyableCode code="environment" /> | `string` |
| <CopyableCode code="firstErrorTimestamp" /> | `number` |
| <CopyableCode code="headers" /> | `object` |
| <CopyableCode code="ownerId" /> | `string` |
| <CopyableCode code="projectIds" /> | `array` |
| <CopyableCode code="secret" /> | `string` |
| <CopyableCode code="sources" /> | `array` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="teamId" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_configurable_log_drain" /> | `SELECT` | <CopyableCode code="id, teamId" /> | Retrieves a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed. |
| <CopyableCode code="get_configurable_log_drains" /> | `SELECT` | <CopyableCode code="teamId" /> | Retrieves a list of Configurable Log Drains. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed. |
| <CopyableCode code="create_configurable_log_drain" /> | `INSERT` | <CopyableCode code="teamId, data__deliveryFormat, data__sources, data__url" /> | Creates a configurable log drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed) |
| <CopyableCode code="delete_configurable_log_drain" /> | `DELETE` | <CopyableCode code="id, teamId" /> | Deletes a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be deleted. |
