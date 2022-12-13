---
title: received_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - received_routes
  - peering
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>received_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.received_routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `receivedTimestamp` | `string` | The received timestamp associated with the prefix. |
| `rpkiValidationState` | `string` | The RPKI validation state for the prefix and origin AS that's listed in the AS path. |
| `trustAnchor` | `string` | The authority which holds the Route Origin Authorization record for the prefix, if any. |
| `asPath` | `string` | The AS path for the prefix. |
| `nextHop` | `string` | The next hop for the prefix. |
| `originAsValidationState` | `string` | The origin AS change information for the prefix. |
| `prefix` | `string` | The prefix. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ReceivedRoutes_ListByPeering` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` |
