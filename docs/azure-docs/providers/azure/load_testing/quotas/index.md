---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - load_testing
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

Creates, updates, deletes, gets or lists a <code>quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.load_testing.quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="quotaBucketName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="usage" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Quota bucket resource properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaBucketName, subscriptionId" /> | Get the available quota for a quota bucket per region per subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List quotas for a given subscription Id. |
| <CopyableCode code="check_availability" /> | `EXEC` | <CopyableCode code="location, quotaBucketName, subscriptionId" /> | Check Quota Availability on quota bucket per region per subscription. |

## `SELECT` examples

List quotas for a given subscription Id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
limit,
location,
provisioning_state,
quotaBucketName,
subscriptionId,
usage
FROM azure.load_testing.vw_quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.load_testing.quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

