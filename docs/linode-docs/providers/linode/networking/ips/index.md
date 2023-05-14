---
title: ips
hide_title: false
hide_table_of_contents: false
keywords:
  - ips
  - networking
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
<tr><td><b>Id</b></td><td><code>linode.networking.ips</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `type` | `string` | The type of address this is.<br /> |
| `address` | `string` | The IP address.<br /> |
| `public` | `boolean` | Whether this is a public or private IP address.<br /> |
| `prefix` | `integer` | The number of bits set in the subnet mask.<br /> |
| `region` | `string` | The Region this IP address resides in.<br /> |
| `subnet_mask` | `string` | The mask that separates host bits from network bits for this address.<br /> |
| `gateway` | `string` | The default gateway for this address.<br /> |
| `linode_id` | `integer` | The ID of the Linode this address currently belongs to. For IPv4 addresses, this is by default the Linode that this address was assigned to on creation, and these addresses my be moved using the [/networking/ipv4/assign](/docs/api/networking/#ips-to-linodes-assign) endpoint. For SLAAC and link-local addresses, this value may not be changed.<br /> |
| `rdns` | `string` | The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getIP` | `SELECT` | `address` | Returns information about a single IP Address on your Account.<br /> |
| `getIPs` | `SELECT` |  | Returns a paginated list of IP Addresses on your Account, excluding private addresses.<br /> |
| `_getIP` | `EXEC` | `address` | Returns information about a single IP Address on your Account.<br /> |
| `_getIPs` | `EXEC` |  | Returns a paginated list of IP Addresses on your Account, excluding private addresses.<br /> |
| `allocateIP` | `EXEC` | `data__linode_id, data__public, data__type` | Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [open a support ticket](/docs/api/support/#support-ticket-open) requesting additional addresses before attempting allocation.<br /> |
| `assignIPs` | `EXEC` | `data__assignments, data__region` | Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.<br /><br />The following restrictions apply:<br />* All Linodes involved must have at least one public IPv4 address after assignment.<br />* Linodes may have no more than one assigned private IPv4 address.<br />* Linodes may have no more than one assigned IPv6 range.<br /><br />[Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.<br /><br />**Note**: Removing an IP address that has been set as a Managed Linode's `ssh.ip` causes the Managed Linode's SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands:<br />* **Linode's Managed Settings View** ([GET /managed/linode-settings/&#123;linodeId&#125;](/docs/api/managed/#linodes-managed-settings-view))<br />* **Linode's Managed Settings Update** ([PUT /managed/linode-settings/&#123;linodeId&#125;](/docs/api/managed/#linodes-managed-settings-update))<br /> |
| `shareIPs` | `EXEC` | `data__ips, data__linode_id` | Configure shared IPs.<br /><br />IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode's IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.<br /><br />IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode.<br /> |
| `updateIP` | `EXEC` | `address, data__rdns` | Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to `null` for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value.<br /> |
