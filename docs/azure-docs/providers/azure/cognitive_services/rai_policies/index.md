---
title: rai_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_policies
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>rai_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.rai_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | Azure OpenAI Content Filters properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, raiPolicyName, resourceGroupName, subscriptionId" /> | Gets the specified Content Filters associated with the Azure OpenAI account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the content filters associated with the Azure OpenAI account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, raiPolicyName, resourceGroupName, subscriptionId" /> | Update the state of specified Content Filters associated with the Azure OpenAI account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, raiPolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified Content Filters associated with the Azure OpenAI account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the content filters associated with the Azure OpenAI account. |
