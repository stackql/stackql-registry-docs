---
title: tickets
hide_title: false
hide_table_of_contents: false
keywords:
  - tickets
  - abuse
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tickets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.abuse.tickets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="closed" /> | `boolean` | Is this abuse ticket closed? |
| <CopyableCode code="closedAt" /> | `string` | The date the abuse ticket was closed |
| <CopyableCode code="createdAt" /> | `string` | The date the abuse ticket was created |
| <CopyableCode code="domainIp" /> | `string` | The domain or IP the suspected abuse was reported against |
| <CopyableCode code="reporter" /> | `string` | The shopper id of the person who reported the suspected abuse |
| <CopyableCode code="source" /> | `string` | The single URL or IP the suspected abuse was reported against |
| <CopyableCode code="target" /> | `string` | The company the suspected abuse is targeting |
| <CopyableCode code="ticketId" /> | `string` | Abuse ticket ID |
| <CopyableCode code="type" /> | `string` | The type of abuse being reported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ticket_info" /> | `SELECT` | <CopyableCode code="ticket_id" /> | Return the abuse ticket data for a given ticket id |
| <CopyableCode code="get_tickets" /> | `SELECT` |  | List all abuse tickets ids that match user provided filters |
| <CopyableCode code="create_ticket" /> | `INSERT` |  | Create a new abuse ticket |
| <CopyableCode code="_get_tickets" /> | `EXEC` |  | List all abuse tickets ids that match user provided filters |
