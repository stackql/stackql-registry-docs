---
title: i_pv6_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - i_pv6_firewall_rules
  - sql
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>i_pv6_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.i_pv6_firewall_rules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Gets an IPv6 firewall rule. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of IPv6 firewall rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an IPv6 firewall rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallRuleName, resourceGroupName, serverName, subscriptionId" /> | Deletes an IPv6 firewall rule. |
