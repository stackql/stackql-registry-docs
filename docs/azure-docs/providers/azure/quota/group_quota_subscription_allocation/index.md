---
title: group_quota_subscription_allocation
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_subscription_allocation
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
<tr><td><b>Name</b></td><td><code>group_quota_subscription_allocation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_subscription_allocation" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceName, subscriptionId" /> | Gets Quota allocated to a subscription for the specific Resource Provider, Location, ResourceName. This will include the GroupQuota and total quota allocated to the subscription. Only the Group quota allocated to the subscription can be allocated back to the MG Group Quota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, subscriptionId" /> | Gets all the quota allocated to a subscription for the specific Resource Provider, Location. This will include the GroupQuota and total quota allocated to the subscription. Only the Group quota allocated to the subscription can be allocated back to the MG Group Quota. Use the $filter parameter to filter out the specific resource based on the ResourceProvider/Location. $filter is a required parameter.  |
