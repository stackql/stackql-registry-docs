---
title: group_quota_subscription_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_subscription_allocations
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

Creates, updates, deletes, gets or lists a <code>group_quota_subscription_allocations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_subscription_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_subscription_allocations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_group_quota_subscription_allocations', value: 'view', },
        { label: 'group_quota_subscription_allocations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="$filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupQuotaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="managementGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="region" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shareable_quota" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Subscription Quota details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceName, subscriptionId" /> | Gets Quota allocated to a subscription for the specific Resource Provider, Location, ResourceName. This will include the GroupQuota and total quota allocated to the subscription. Only the Group quota allocated to the subscription can be allocated back to the MG Group Quota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, subscriptionId" /> | Gets all the quota allocated to a subscription for the specific Resource Provider, Location. This will include the GroupQuota and total quota allocated to the subscription. Only the Group quota allocated to the subscription can be allocated back to the MG Group Quota. Use the $filter parameter to filter out the specific resource based on the ResourceProvider/Location. $filter is a required parameter. |

## `SELECT` examples

Gets all the quota allocated to a subscription for the specific Resource Provider, Location. This will include the GroupQuota and total quota allocated to the subscription. Only the Group quota allocated to the subscription can be allocated back to the MG Group Quota. Use the $filter parameter to filter out the specific resource based on the ResourceProvider/Location. $filter is a required parameter. 

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_group_quota_subscription_allocations', value: 'view', },
        { label: 'group_quota_subscription_allocations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
$filter,
groupQuotaName,
limit,
managementGroupId,
region,
resourceName,
shareable_quota,
subscriptionId
FROM azure.quota.vw_group_quota_subscription_allocations
WHERE $filter = '{{ $filter }}'
AND groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.quota.group_quota_subscription_allocations
WHERE $filter = '{{ $filter }}'
AND groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

