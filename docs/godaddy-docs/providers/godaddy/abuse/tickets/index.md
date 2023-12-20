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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tickets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.abuse.tickets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `closed` | `boolean` | Is this abuse ticket closed? |
| `closedAt` | `string` | The date the abuse ticket was closed |
| `createdAt` | `string` | The date the abuse ticket was created |
| `domainIp` | `string` | The domain or IP the suspected abuse was reported against |
| `reporter` | `string` | The shopper id of the person who reported the suspected abuse |
| `source` | `string` | The single URL or IP the suspected abuse was reported against |
| `target` | `string` | The company the suspected abuse is targeting |
| `ticketId` | `string` | Abuse ticket ID |
| `type` | `string` | The type of abuse being reported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_ticket_info` | `SELECT` | `ticket_id` | Return the abuse ticket data for a given ticket id |
| `get_tickets` | `SELECT` |  | List all abuse tickets ids that match user provided filters |
| `create_ticket` | `INSERT` |  | Create a new abuse ticket |
| `_get_tickets` | `EXEC` |  | List all abuse tickets ids that match user provided filters |
