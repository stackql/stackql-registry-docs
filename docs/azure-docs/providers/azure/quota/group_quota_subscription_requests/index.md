---
title: group_quota_subscription_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_subscription_requests
  - quota
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>group_quota_subscription_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_subscription_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_subscription_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId, requestId" /> | Get API to check the status of a subscriptionIds request by requestId.  Use the polling API - OperationsStatus URI specified in Azure-AsyncOperation header field, with retry-after duration in seconds to check the intermediate status. This API provides the finals status with the request details and status. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | List API to check the status of a subscriptionId requests by requestId. Request history is maintained for 1 year. |

## `SELECT` examples

List API to check the status of a subscriptionId requests by requestId. Request history is maintained for 1 year.


```sql
SELECT
properties
FROM azure.quota.group_quota_subscription_requests
WHERE groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}';
```