---
title: ips
hide_title: false
hide_table_of_contents: false
keywords:
  - ips
  - instances
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
<tr><td><b>Name</b></td><td><code>ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.ips</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ipv4` | `object` | Information about this Linode's IPv4 addresses.<br /> |
| `ipv6` | `object` | Information about this Linode's IPv6 addresses.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLinodeIP` | `SELECT` | `address, linodeId` | View information about the specified IP address associated with the specified Linode.<br /> |
| `getLinodeIPs` | `SELECT` | `linodeId` | Returns networking information for a single Linode.<br /> |
| `addLinodeIP` | `INSERT` | `linodeId, data__public, data__type` | Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode.<br /> |
| `removeLinodeIP` | `DELETE` | `address, linodeId` | Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode's last remaining public IPv4 address.<br /> |
| `_getLinodeIP` | `EXEC` | `address, linodeId` | View information about the specified IP address associated with the specified Linode.<br /> |
| `_getLinodeIPs` | `EXEC` | `linodeId` | Returns networking information for a single Linode.<br /> |
| `updateLinodeIP` | `EXEC` | `address, linodeId, data__rdns` | Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.<br /><br />Setting the RDNS to `null` for a public IPv4 address, resets it to the default "ip.linodeusercontent.com" RDNS value.<br /> |
