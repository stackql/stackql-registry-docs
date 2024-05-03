---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - data_lake_analytics
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
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.firewall_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The firewall rule properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Analytics firewall rule. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Analytics firewall rules within the specified Data Lake Analytics account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the specified firewall rule. During update, the firewall rule with the specified name will be replaced with this new firewall rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId" /> | Deletes the specified firewall rule from the specified Data Lake Analytics account |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Analytics firewall rules within the specified Data Lake Analytics account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, firewallRuleName, resourceGroupName, subscriptionId" /> | Updates the specified firewall rule. |
