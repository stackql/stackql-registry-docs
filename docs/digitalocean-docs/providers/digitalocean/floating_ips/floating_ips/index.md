---
title: floating_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - floating_ips
  - floating_ips
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
<tr><td><b>Name</b></td><td><code>floating_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.floating_ips.floating_ips" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="droplet" /> | `` | The Droplet that the floating IP has been assigned to. When you query a floating IP, if it is assigned to a Droplet, the entire Droplet object will be returned. If it is not assigned, the value will be null. |
| <CopyableCode code="ip" /> | `string` | The public IP address of the floating IP. It also serves as its identifier. |
| <CopyableCode code="locked" /> | `boolean` | A boolean value indicating whether or not the floating IP has pending actions preventing new ones from being submitted. |
| <CopyableCode code="project_id" /> | `string` | The UUID of the project to which the reserved IP currently belongs. |
| <CopyableCode code="region" /> | `object` | The region that the floating IP is reserved to. When you query a floating IP, the entire region object will be returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="floatingIPs_get" /> | `SELECT` | <CopyableCode code="floating_ip" /> | To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`. |
| <CopyableCode code="floatingIPs_list" /> | `SELECT` |  | To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`. |
| <CopyableCode code="floatingIPs_create" /> | `INSERT` |  | On creation, a floating IP must be either assigned to a Droplet or reserved to a region.<br />* To create a new floating IP assigned to a Droplet, send a POST<br />  request to `/v2/floating_ips` with the `droplet_id` attribute.<br /><br />* To create a new floating IP reserved to a region, send a POST request to<br />  `/v2/floating_ips` with the `region` attribute.<br /><br />**Note**:  In addition to the standard rate limiting, only 12 floating IPs may be created per 60 seconds. |
| <CopyableCode code="floatingIPs_delete" /> | `DELETE` | <CopyableCode code="floating_ip" /> | To delete a floating IP and remove it from your account, send a DELETE request<br />to `/v2/floating_ips/$FLOATING_IP_ADDR`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| <CopyableCode code="_floatingIPs_get" /> | `EXEC` | <CopyableCode code="floating_ip" /> | To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`. |
| <CopyableCode code="_floatingIPs_list" /> | `EXEC` |  | To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`. |
