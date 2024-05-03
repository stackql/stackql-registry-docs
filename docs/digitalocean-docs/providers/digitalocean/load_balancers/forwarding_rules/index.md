---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
  - load_balancers
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.load_balancers.forwarding_rules" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="loadBalancers_remove_forwardingRules" /> | `DELETE` | <CopyableCode code="lb_id, data__forwarding_rules" /> | To remove forwarding rules from a load balancer instance, send a DELETE<br />request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the<br />body of the request, there should be a `forwarding_rules` attribute containing<br />an array of rules to be removed.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
| <CopyableCode code="loadBalancers_add_forwardingRules" /> | `EXEC` | <CopyableCode code="lb_id, data__forwarding_rules" /> | To add an additional forwarding rule to a load balancer instance, send a POST<br />request to `/v2/load_balancers/$LOAD_BALANCER_ID/forwarding_rules`. In the body<br />of the request, there should be a `forwarding_rules` attribute containing an<br />array of rules to be added.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
