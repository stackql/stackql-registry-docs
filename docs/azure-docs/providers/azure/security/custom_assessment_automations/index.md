---
title: custom_assessment_automations
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_assessment_automations
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
<tr><td><b>Name</b></td><td><code>custom_assessment_automations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.custom_assessment_automations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | describes the Custom Assessment Automation properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, customAssessmentAutomationName, resourceGroupName, subscriptionId" /> | Gets a single custom assessment automation by name for the provided subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List custom assessment automations by provided subscription and resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List custom assessment automations by provided subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, customAssessmentAutomationName, resourceGroupName, subscriptionId" /> | Creates or updates a custom assessment automation for the provided subscription. Please note that providing an existing custom assessment automation will replace the existing record. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, customAssessmentAutomationName, resourceGroupName, subscriptionId" /> | Deletes a custom assessment automation by name for a provided subscription |
