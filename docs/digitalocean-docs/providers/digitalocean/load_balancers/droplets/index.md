---
title: droplets
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets
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
<tr><td><b>Name</b></td><td><code>droplets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.load_balancers.droplets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="loadBalancers_remove_droplets" /> | `DELETE` | <CopyableCode code="lb_id, data__droplet_ids" /> | To remove a Droplet from a load balancer instance, send a DELETE request to<br />`/v2/load_balancers/$LOAD_BALANCER_ID/droplets`. In the body of the request,<br />there should be a `droplet_ids` attribute containing a list of Droplet IDs.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
| <CopyableCode code="loadBalancers_add_droplets" /> | `EXEC` | <CopyableCode code="lb_id, data__droplet_ids" /> | To assign a Droplet to a load balancer instance, send a POST request to<br />`/v2/load_balancers/$LOAD_BALANCER_ID/droplets`. In the body of the request,<br />there should be a `droplet_ids` attribute containing a list of Droplet IDs.<br />Individual Droplets can not be added to a load balancer configured with a<br />Droplet tag. Attempting to do so will result in a "422 Unprocessable Entity"<br />response from the API.<br /><br />No response body will be sent back, but the response code will indicate<br />success. Specifically, the response code will be a 204, which means that the<br />action was successful with no returned body data.<br /> |
