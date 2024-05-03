---
title: webhook_deliveries
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook_deliveries
  - orgs
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
<tr><td><b>Name</b></td><td><code>webhook_deliveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.orgs.webhook_deliveries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the webhook delivery. |
| <CopyableCode code="action" /> | `string` | The type of activity for the event that triggered the delivery. |
| <CopyableCode code="delivered_at" /> | `string` | Time when the webhook delivery occurred. |
| <CopyableCode code="duration" /> | `number` | Time spent delivering. |
| <CopyableCode code="event" /> | `string` | The event that triggered the delivery. |
| <CopyableCode code="guid" /> | `string` | Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event). |
| <CopyableCode code="installation_id" /> | `integer` | The id of the GitHub App installation associated with this event. |
| <CopyableCode code="redelivery" /> | `boolean` | Whether the webhook delivery is a redelivery. |
| <CopyableCode code="repository_id" /> | `integer` | The id of the repository associated with this event. |
| <CopyableCode code="status" /> | `string` | Describes the response returned after attempting the delivery. |
| <CopyableCode code="status_code" /> | `integer` | Status code received when delivery was made. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_webhook_deliveries" /> | `SELECT` | <CopyableCode code="hook_id, org" /> |
