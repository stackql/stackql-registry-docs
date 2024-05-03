---
title: mongo_clusters_firewall_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters_firewall_rule
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>mongo_clusters_firewall_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongo_clusters_firewall_rule" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallRuleName, mongoClusterName, resourceGroupName, subscriptionId" /> | Gets information about a mongo cluster firewall rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | List all the firewall rules in a given mongo cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallRuleName, mongoClusterName, resourceGroupName, subscriptionId, data__properties" /> | Creates a new firewall rule or updates an existing firewall rule on a mongo cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallRuleName, mongoClusterName, resourceGroupName, subscriptionId" /> | Deletes a mongo cluster firewall rule. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | List all the firewall rules in a given mongo cluster. |
