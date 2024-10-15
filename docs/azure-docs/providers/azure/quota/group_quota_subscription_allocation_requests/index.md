---
title: group_quota_subscription_allocation_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_subscription_allocation_requests
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

Creates, updates, deletes, gets or lists a <code>group_quota_subscription_allocation_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_subscription_allocation_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_subscription_allocation_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="allocationId, groupQuotaName, managementGroupId, subscriptionId" /> | Get the quota allocation request status for the subscriptionId by allocationId. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceProviderName, subscriptionId" /> | Get all the quotaAllocationRequests for a resourceProvider/location. The filter paramter for location is required. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId, resourceName, resourceProviderName, subscriptionId" /> | Request to assign quota from group quota to a specific Subscription. The assign GroupQuota to subscriptions or reduce the quota allocated to subscription to give back the unused quota ( quota >= usages) to the groupQuota. So, this API can be used to assign Quota to subscriptions and assign back unused quota to group quota, which can be assigned to another subscriptions in the GroupQuota. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupQuotaName, managementGroupId, resourceName, resourceProviderName, subscriptionId" /> | Request to assign quota from group quota to a specific Subscription. The assign GroupQuota to subscriptions or reduce the quota allocated to subscription to give back the unused quota ( quota >= usages) to the groupQuota. So, this API can be used to assign Quota to subscriptions and assign back unused quota to group quota, which can be assigned to another subscriptions in the GroupQuota. User can collect unused quotas from multiple subscriptions within the groupQuota and assign the groupQuota to the subscription, where it's needed. |

## `SELECT` examples

Get the quota allocation request status for the subscriptionId by allocationId.


```sql
SELECT
properties
FROM azure.quota.group_quota_subscription_allocation_requests
WHERE allocationId = '{{ allocationId }}'
AND groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group_quota_subscription_allocation_requests</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.quota.group_quota_subscription_allocation_requests (
groupQuotaName,
managementGroupId,
resourceName,
resourceProviderName,
subscriptionId,
properties
)
SELECT 
'{{ groupQuotaName }}',
'{{ managementGroupId }}',
'{{ resourceName }}',
'{{ resourceProviderName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: requestedResource
          value:
            - name: properties
              value:
                - name: limit
                  value: integer
                - name: name
                  value:
                    - name: value
                      value: string
                    - name: localizedValue
                      value: string
                - name: region
                  value: string
        - name: requestSubmitTime
          value: string
        - name: provisioningState
          value: []
        - name: faultCode
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>group_quota_subscription_allocation_requests</code> resource.

```sql
/*+ update */
UPDATE azure.quota.group_quota_subscription_allocation_requests
SET 
properties = '{{ properties }}'
WHERE 
groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND resourceName = '{{ resourceName }}'
AND resourceProviderName = '{{ resourceProviderName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
