---
title: resource_quota_limits
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_quota_limits
  - netapp
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

Creates, updates, deletes, gets or lists a <code>resource_quota_limits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_quota_limits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.resource_quota_limits" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_quota_limits', value: 'view', },
        { label: 'resource_quota_limits', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="current" /> | `text` | field from the `properties` object |
| <CopyableCode code="default" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="quotaLimitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SubscriptionQuotaItem Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaLimitName, subscriptionId" /> | Get the default and current subscription quota limit |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the default and current limits for quotas |

## `SELECT` examples

Get the default and current limits for quotas

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_quota_limits', value: 'view', },
        { label: 'resource_quota_limits', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
current,
default,
location,
quotaLimitName,
subscriptionId
FROM azure_isv.netapp.vw_resource_quota_limits
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.netapp.resource_quota_limits
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

