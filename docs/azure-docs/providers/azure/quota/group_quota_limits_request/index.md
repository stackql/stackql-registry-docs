---
title: group_quota_limits_request
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_limits_request
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
<tr><td><b>Name</b></td><td><code>group_quota_limits_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_limits_request" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId, requestId" /> | Get API to check the status of a GroupQuota request by requestId. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceProviderName" /> | Get API to check the status of a GroupQuota request by requestId. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId, resourceName, resourceProviderName" /> | Put the GroupQuota requests for a specific ResourceProvider/Location/Resource. the location and resourceName ("name": &#123;"value" : "resourceName") properties are specified in the request body. Only 1 resource quota can be requested.<br />Use the polling API - OperationsStatus URI specified in Azure-AsyncOperation header field, with retry-after duration in seconds to check the intermediate status. This API provides the finals status with the request details and status. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupQuotaName, managementGroupId, resourceName, resourceProviderName" /> | Create the GroupQuota requests for a specific ResourceProvider/Location/Resource. the location and resourceName properties are specified in the request body. Only 1 resource quota can be requested. Please note that patch request creates a new groupQuota request.<br />Use the polling API - OperationsStatus URI specified in Azure-AsyncOperation header field, with retry-after duration in seconds to check the intermediate status. This API provides the finals status with the request details and status. |
