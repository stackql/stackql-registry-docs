---
title: group_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quotas
  - quota
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
<tr><td><b>Name</b></td><td><code>group_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quotas" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Gets the GroupQuotas for the name passed. It will return the GroupQuotas properties only. The details on group quota can be access from the group quota APIs. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managementGroupId" /> | Lists GroupQuotas for the scope passed. It will return the GroupQuotas QuotaEntity properties only.The details on group quota can be access from the group quota APIs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Creates a new GroupQuota for the name passed. A RequestId will be returned by the Service. The status can be polled periodically. The status Async polling is using standards defined at - https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/async-api-reference.md#asynchronous-operations. Use the OperationsStatus URI provided in Azure-AsyncOperation header, the duration will be specified in retry-after header. Once the operation gets to terminal state - Succeeded \| Failed, then the URI will change to Get URI and full details can be checked. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Deletes the GroupQuotas for the name passed. All the remaining shareQuota in the GroupQuotas will be lost. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Updates the GroupQuotas for the name passed. A GroupQuotas RequestId will be returned by the Service. The status can be polled periodically. The status Async polling is using standards defined at - https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/async-api-reference.md#asynchronous-operations. Use the OperationsStatus URI provided in Azure-AsyncOperation header, the duration will be specified in retry-after header. Once the operation gets to terminal state - Succeeded \| Failed, then the URI will change to Get URI and full details can be checked. <br /> Any change in the filters will be applicable to the future quota assignments, existing quota allocated to subscriptions from the GroupQuotas remains unchanged. |
