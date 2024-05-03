---
title: tickets_replies
hide_title: false
hide_table_of_contents: false
keywords:
  - tickets_replies
  - support
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tickets_replies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.support.tickets_replies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique ID of this Support Ticket reply.<br /> |
| <CopyableCode code="description" /> | `string` | The body of this Support Ticket reply.<br /> |
| <CopyableCode code="created" /> | `string` | The date and time this Ticket reply was created.<br /> |
| <CopyableCode code="created_by" /> | `string` | The User who submitted this reply.<br /> |
| <CopyableCode code="from_linode" /> | `boolean` | If set to true, this reply came from a Linode employee.<br /> |
| <CopyableCode code="gravatar_id" /> | `string` | The Gravatar ID of the User who created this reply.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getTicketReplies" /> | `SELECT` | <CopyableCode code="ticketId" /> | Returns a collection of replies to a Support Ticket on your Account.<br /> |
| <CopyableCode code="createTicketReply" /> | `INSERT` | <CopyableCode code="ticketId, data__description" /> | Adds a reply to an existing Support Ticket.<br /> |
| <CopyableCode code="_getTicketReplies" /> | `EXEC` | <CopyableCode code="ticketId" /> | Returns a collection of replies to a Support Ticket on your Account.<br /> |
