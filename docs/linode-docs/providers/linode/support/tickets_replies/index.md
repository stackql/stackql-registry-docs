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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tickets_replies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.support.tickets_replies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of this Support Ticket reply.<br /> |
| `description` | `string` | The body of this Support Ticket reply.<br /> |
| `created` | `string` | The date and time this Ticket reply was created.<br /> |
| `created_by` | `string` | The User who submitted this reply.<br /> |
| `from_linode` | `boolean` | If set to true, this reply came from a Linode employee.<br /> |
| `gravatar_id` | `string` | The Gravatar ID of the User who created this reply.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getTicketReplies` | `SELECT` | `ticketId` | Returns a collection of replies to a Support Ticket on your Account.<br /> |
| `createTicketReply` | `INSERT` | `ticketId, data__description` | Adds a reply to an existing Support Ticket.<br /> |
| `_getTicketReplies` | `EXEC` | `ticketId` | Returns a collection of replies to a Support Ticket on your Account.<br /> |
