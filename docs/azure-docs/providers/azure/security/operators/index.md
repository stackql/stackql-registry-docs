---
title: operators
hide_title: false
hide_table_of_contents: false
keywords:
  - operators
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
<tr><td><b>Name</b></td><td><code>operators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.operators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, pricingName, securityOperatorName, subscriptionId" /> | Get a specific security operator for the requested scope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, pricingName, subscriptionId" /> | Lists Microsoft Defender for Cloud securityOperators in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, pricingName, securityOperatorName, subscriptionId" /> | Creates Microsoft Defender for Cloud security operator on the given scope. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, pricingName, securityOperatorName, subscriptionId" /> | Delete Microsoft Defender for Cloud securityOperator in the subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, pricingName, subscriptionId" /> | Lists Microsoft Defender for Cloud securityOperators in the subscription. |
