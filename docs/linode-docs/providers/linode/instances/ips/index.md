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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.ips" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipv4" /> | `object` | Information about this Linode's IPv4 addresses.<br /> |
| <CopyableCode code="ipv6" /> | `object` | Information about this Linode's IPv6 addresses.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLinodeIP" /> | `SELECT` | <CopyableCode code="address, linodeId" /> | View information about the specified IP address associated with the specified Linode.<br /> |
| <CopyableCode code="getLinodeIPs" /> | `SELECT` | <CopyableCode code="linodeId" /> | Returns networking information for a single Linode.<br /> |
| <CopyableCode code="addLinodeIP" /> | `INSERT` | <CopyableCode code="linodeId, data__public, data__type" /> | Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode.<br /> |
| <CopyableCode code="removeLinodeIP" /> | `DELETE` | <CopyableCode code="address, linodeId" /> | Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode's last remaining public IPv4 address.<br /> |
| <CopyableCode code="_getLinodeIP" /> | `EXEC` | <CopyableCode code="address, linodeId" /> | View information about the specified IP address associated with the specified Linode.<br /> |
| <CopyableCode code="_getLinodeIPs" /> | `EXEC` | <CopyableCode code="linodeId" /> | Returns networking information for a single Linode.<br /> |
| <CopyableCode code="updateLinodeIP" /> | `EXEC` | <CopyableCode code="address, linodeId, data__rdns" /> | Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.<br /><br />Setting the RDNS to `null` for a public IPv4 address, resets it to the default "ip.linodeusercontent.com" RDNS value.<br /> |
