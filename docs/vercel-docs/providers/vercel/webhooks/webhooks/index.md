---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - webhooks
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
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.webhooks.webhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The webhook id |
| <CopyableCode code="createdAt" /> | `number` | A number containing the date when the webhook was created in in milliseconds |
| <CopyableCode code="events" /> | `array` | The webhooks events |
| <CopyableCode code="ownerId" /> | `string` | The unique ID of the team the webhook belongs to |
| <CopyableCode code="projectIds" /> | `array` | The ID of the projects the webhook is associated with |
| <CopyableCode code="updatedAt" /> | `number` | A number containing the date when the webhook was updated in in milliseconds |
| <CopyableCode code="url" /> | `string` | A string with the URL of the webhook |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_webhook" /> | `SELECT` | <CopyableCode code="id, teamId" /> | Get a webhook |
| <CopyableCode code="get_webhooks" /> | `SELECT` | <CopyableCode code="teamId" /> | Get a list of webhooks |
| <CopyableCode code="create_webhook" /> | `INSERT` | <CopyableCode code="teamId, data__events, data__url" /> | Creates a webhook |
| <CopyableCode code="delete_webhook" /> | `DELETE` | <CopyableCode code="id, teamId" /> | Deletes a webhook |
