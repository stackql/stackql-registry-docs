---
title: group_quota_limits
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_limits
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
<tr><td><b>Name</b></td><td><code>group_quota_limits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_limits" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceName, resourceProviderName" /> | Gets the GroupQuotaLimits for the specific resource for a specific resource based on the resourceProviders, resourceName and $filter passed.<br />The $filter=location eq &#123;location&#125; is required to location specific resources groupQuota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceProviderName" /> | Gets the GroupQuotaLimits for the all resource for a specific  resourceProvider and $filter passed.<br />The $filter=location eq &#123;location&#125; is required to location specific resources groupQuota. |
