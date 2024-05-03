---
title: webhook_delivery
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook_delivery
  - apps
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhook_delivery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.apps.webhook_delivery" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the delivery. |
| <CopyableCode code="action" /> | `string` | The type of activity for the event that triggered the delivery. |
| <CopyableCode code="delivered_at" /> | `string` | Time when the delivery was delivered. |
| <CopyableCode code="duration" /> | `number` | Time spent delivering. |
| <CopyableCode code="event" /> | `string` | The event that triggered the delivery. |
| <CopyableCode code="guid" /> | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| <CopyableCode code="installation_id" /> | `integer` | The id of the GitHub App installation associated with this event. |
| <CopyableCode code="redelivery" /> | `boolean` | Whether the delivery is a redelivery. |
| <CopyableCode code="repository_id" /> | `integer` | The id of the repository associated with this event. |
| <CopyableCode code="request" /> | `object` |  |
| <CopyableCode code="response" /> | `object` |  |
| <CopyableCode code="status" /> | `string` | Description of the status of the attempted delivery |
| <CopyableCode code="status_code" /> | `integer` | Status code received when delivery was made. |
| <CopyableCode code="url" /> | `string` | The URL target of the delivery. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_webhook_delivery" /> | `SELECT` | <CopyableCode code="delivery_id" /> | Returns a delivery for the webhook configured for a GitHub App.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| <CopyableCode code="redeliver_webhook_delivery" /> | `EXEC` | <CopyableCode code="delivery_id" /> | Redeliver a delivery for the webhook configured for a GitHub App.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
