---
title: governance_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_rules
  - security
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
<tr><td><b>Name</b></td><td><code>governance_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.governance_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Describes properties of an governance rule |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, ruleId, scope" /> | Get a specific governance rule for the requested scope by ruleId |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, scope" /> | Get a list of all relevant governance rules over a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, ruleId, scope" /> | Creates or updates a governance rule over a given scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, ruleId, scope" /> | Delete a Governance rule over a given scope |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, scope" /> | Get a list of all relevant governance rules over a scope |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="api-version, ruleId, scope" /> | Execute a governance rule |
| <CopyableCode code="operation_results" /> | `EXEC` | <CopyableCode code="api-version, operationId, ruleId, scope" /> | Get governance rules long run operation result for the requested scope by ruleId and operationId |
