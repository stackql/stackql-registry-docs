---
title: benefit_utilization_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - benefit_utilization_summaries
  - cost_management
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
<tr><td><b>Name</b></td><td><code>benefit_utilization_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.benefit_utilization_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="kind" /> | `string` | Kind/type of the benefit. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_billing_account_id" /> | `SELECT` | <CopyableCode code="billingAccountId" /> | Lists savings plan utilization summaries for the enterprise agreement scope. Supported at grain values: 'Daily' and 'Monthly'. |
| <CopyableCode code="list_by_billing_profile_id" /> | `SELECT` | <CopyableCode code="billingAccountId, billingProfileId" /> | Lists savings plan utilization summaries for billing profile. Supported at grain values: 'Daily' and 'Monthly'. |
| <CopyableCode code="list_by_savings_plan_id" /> | `SELECT` | <CopyableCode code="savingsPlanId, savingsPlanOrderId" /> | Lists the savings plan utilization summaries for daily or monthly grain. |
| <CopyableCode code="list_by_savings_plan_order" /> | `SELECT` | <CopyableCode code="savingsPlanOrderId" /> | Lists the savings plan utilization summaries for daily or monthly grain. |
