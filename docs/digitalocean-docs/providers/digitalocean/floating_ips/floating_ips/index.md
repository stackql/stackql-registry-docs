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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>floating_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.floating_ips.floating_ips</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `locked` | `boolean` | A boolean value indicating whether or not the floating IP has pending actions preventing new ones from being submitted. |
| `project_id` | `string` | The UUID of the project to which the reserved IP currently belongs. |
| `region` | `object` | The region that the floating IP is reserved to. When you query a floating IP, the entire region object will be returned. |
| `droplet` | `` | The Droplet that the floating IP has been assigned to. When you query a floating IP, if it is assigned to a Droplet, the entire Droplet object will be returned. If it is not assigned, the value will be null. |
| `ip` | `string` | The public IP address of the floating IP. It also serves as its identifier. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `floatingIPs_get` | `SELECT` | `floating_ip` | To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`. |
| `floatingIPs_list` | `SELECT` |  | To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`. |
| `floatingIPs_create` | `INSERT` |  | On creation, a floating IP must be either assigned to a Droplet or reserved to a region.<br />* To create a new floating IP assigned to a Droplet, send a POST<br />  request to `/v2/floating_ips` with the `droplet_id` attribute.<br /><br />* To create a new floating IP reserved to a region, send a POST request to<br />  `/v2/floating_ips` with the `region` attribute.<br /><br />**Note**:  In addition to the standard rate limiting, only 12 floating IPs may be created per 60 seconds. |
| `floatingIPs_delete` | `DELETE` | `floating_ip` | To delete a floating IP and remove it from your account, send a DELETE request<br />to `/v2/floating_ips/$FLOATING_IP_ADDR`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| `_floatingIPs_get` | `EXEC` | `floating_ip` | To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`. |
| `_floatingIPs_list` | `EXEC` |  | To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`. |
