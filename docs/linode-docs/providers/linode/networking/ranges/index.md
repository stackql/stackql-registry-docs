---
title: ranges
hide_title: false
hide_table_of_contents: false
keywords:
  - ranges
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
<tr><td><b>Name</b></td><td><code>ranges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.networking.ranges</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `range` | `string` | The IPv6 range of addresses in this pool.<br /> |
| `region` | `string` | The region for this range of IPv6 addresses.<br /> |
| `route_target` | `string` | The last address in this block of IPv6 addresses.<br /> |
| `prefix` | `integer` | The prefix length of the address, denoting how many addresses can be assigned from this range calculated as 2 &lt;sup&gt;128-prefix&lt;/sup&gt;.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getIPv6Range` | `SELECT` | `range` | View IPv6 range information.<br /> |
| `getIPv6Ranges` | `SELECT` |  | Displays the IPv6 ranges on your Account.<br /><br /><br />  * An IPv6 range is a `/64` or `/54` block of IPv6 addresses routed to a single Linode in a given [Region](/docs/api/regions/#regions-list).<br /><br />  * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br /><br />  * Access the IPv6 Range Create ([POST /networking/ipv6/ranges](/docs/api/networking/#ipv6-range-create)) endpoint to add a `/64` or `/56` block of IPv6 addresses to your account.<br /> |
| `deleteIPv6Range` | `DELETE` | `range` | Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.<br /><br />**Note:** Shared IPv6 ranges cannot be deleted at this time. Please contact Customer Support for assistance.<br /> |
| `_getIPv6Range` | `EXEC` | `range` | View IPv6 range information.<br /> |
| `_getIPv6Ranges` | `EXEC` |  | Displays the IPv6 ranges on your Account.<br /><br /><br />  * An IPv6 range is a `/64` or `/54` block of IPv6 addresses routed to a single Linode in a given [Region](/docs/api/regions/#regions-list).<br /><br />  * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br /><br />  * Access the IPv6 Range Create ([POST /networking/ipv6/ranges](/docs/api/networking/#ipv6-range-create)) endpoint to add a `/64` or `/56` block of IPv6 addresses to your account.<br /> |
| `postIPv6Range` | `EXEC` | `data__prefix_length` | Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the `ipv6` property when accessing the Linode View ([GET /linode/instances/&#123;linodeId&#125;](/docs/api/linode-instances/#linode-view)) endpoint to view a Linode's IPv6 SLAAC address.<br />  * Either `linode_id` or `route_target` is required in a request.<br />  * `linode_id` and `route_target` are mutually exclusive. Submitting values for both properties in a request results in an error.<br />  * Upon a successful request, an IPv6 range is created in the [Region](/docs/api/regions/#regions-list) that corresponds to the provided `linode_id` or `route_target`.<br />  * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br />  * Access the IP Addresses Assign ([POST /networking/ips/assign](/docs/api/networking/#ip-addresses-assign)) endpoint to re-assign IPv6 Ranges to your Linodes.<br /><br />**Note**: The following restrictions apply:<br />  * A Linode can only have one IPv6 range targeting its SLAAC address.<br />  * An account can only have one IPv6 range in each [Region](/docs/api/regions/#regions-list).<br />  * [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request expansion of these restrictions.<br /> |
