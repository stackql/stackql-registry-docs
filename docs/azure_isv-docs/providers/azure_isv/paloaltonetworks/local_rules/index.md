---
title: local_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rules
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>local_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.local_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | definition of rule |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Get a LocalRulesResource |
| <CopyableCode code="list_by_local_rulestacks" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | List LocalRulesResource resources by LocalRulestacks |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId, data__properties" /> | Create a LocalRulesResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Delete a LocalRulesResource |
| <CopyableCode code="_list_by_local_rulestacks" /> | `EXEC` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | List LocalRulesResource resources by LocalRulestacks |
| <CopyableCode code="refresh_counters" /> | `EXEC` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Refresh counters |
| <CopyableCode code="reset_counters" /> | `EXEC` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Reset counters |
