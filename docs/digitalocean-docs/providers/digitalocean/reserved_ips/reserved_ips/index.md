---
title: reserved_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_ips
  - reserved_ips
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
<tr><td><b>Name</b></td><td><code>reserved_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.reserved_ips.reserved_ips</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `project_id` | `string` | The UUID of the project to which the reserved IP currently belongs. |
| `region` | `object` | The region that the reserved IP is reserved to. When you query a reserved IP, the entire region object will be returned. |
| `droplet` | `` | The Droplet that the reserved IP has been assigned to. When you query a reserved IP, if it is assigned to a Droplet, the entire Droplet object will be returned. If it is not assigned, the value will be null. |
| `ip` | `string` | The public IP address of the reserved IP. It also serves as its identifier. |
| `locked` | `boolean` | A boolean value indicating whether or not the reserved IP has pending actions preventing new ones from being submitted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reservedIPs_get` | `SELECT` | `reserved_ip` | To show information about a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP_ADDR`. |
| `reservedIPs_list` | `SELECT` |  | To list all of the reserved IPs available on your account, send a GET request to `/v2/reserved_ips`. |
| `reservedIPs_create` | `INSERT` |  | On creation, a reserved IP must be either assigned to a Droplet or reserved to a region.<br />* To create a new reserved IP assigned to a Droplet, send a POST<br />  request to `/v2/reserved_ips` with the `droplet_id` attribute.<br /><br />* To create a new reserved IP reserved to a region, send a POST request to<br />  `/v2/reserved_ips` with the `region` attribute.<br /><br />**Note**:  In addition to the standard rate limiting, only 12 reserved IPs may be created per 60 seconds. |
| `reservedIPs_delete` | `DELETE` | `reserved_ip` | To delete a reserved IP and remove it from your account, send a DELETE request<br />to `/v2/reserved_ips/$RESERVED_IP_ADDR`.<br /><br />A successful request will receive a 204 status code with no body in response.<br />This indicates that the request was processed successfully.<br /> |
| `_reservedIPs_get` | `EXEC` | `reserved_ip` | To show information about a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP_ADDR`. |
| `_reservedIPs_list` | `EXEC` |  | To list all of the reserved IPs available on your account, send a GET request to `/v2/reserved_ips`. |
