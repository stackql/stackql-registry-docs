---
title: group_quota_limits
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_limits
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

Creates, updates, deletes, gets or lists a <code>group_quota_limits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_limits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_limits" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_group_quota_limits', value: 'view', },
        { label: 'group_quota_limits', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="$filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="allocated_to_subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupQuotaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="managementGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="region" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceProviderName" /> | `text` | field from the `properties` object |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Group Quota details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceName, resourceProviderName" /> | Gets the GroupQuotaLimits for the specific resource for a specific resource based on the resourceProviders, resourceName and $filter passed.
The $filter=location eq {location} is required to location specific resources groupQuota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, groupQuotaName, managementGroupId, resourceProviderName" /> | Gets the GroupQuotaLimits for the all resource for a specific  resourceProvider and $filter passed.
The $filter=location eq {location} is required to location specific resources groupQuota. |

## `SELECT` examples

Gets the GroupQuotaLimits for the all resource for a specific  resourceProvider and $filter passed.
The $filter=location eq {location} is required to location specific resources groupQuota.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_group_quota_limits', value: 'view', },
        { label: 'group_quota_limits', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
$filter,
allocated_to_subscriptions,
available_limit,
comment,
groupQuotaName,
limit,
managementGroupId,
region,
resourceName,
resourceProviderName,
unit
FROM azure.quota.vw_group_quota_limits
WHERE $filter = '{{ $filter }}'
AND groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND resourceProviderName = '{{ resourceProviderName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.quota.group_quota_limits
WHERE $filter = '{{ $filter }}'
AND groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND resourceProviderName = '{{ resourceProviderName }}';
```
</TabItem></Tabs>

