---
title: outbound_firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_firewall_rules
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
<tr><td><b>Name</b></td><td><code>outbound_firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.outbound_firewall_rules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="outboundRuleFqdn, resourceGroupName, serverName, subscriptionId" /> | Gets an outbound firewall rule. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets all outbound firewall rules on a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="outboundRuleFqdn, resourceGroupName, serverName, subscriptionId" /> | Create a outbound firewall rule with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="outboundRuleFqdn, resourceGroupName, serverName, subscriptionId" /> | Deletes a outbound firewall rule with a given name. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets all outbound firewall rules on a server. |
