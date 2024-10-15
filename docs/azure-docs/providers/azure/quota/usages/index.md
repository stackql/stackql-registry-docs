---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.usages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_usages', value: 'view', },
        { label: 'usages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="is_quota_applicable" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Usage properties for the specified resource. |
| <CopyableCode code="quota_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="usages" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | Usage properties for the specified resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceName, scope" /> | Get the current usage of a resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of current usage for all resources for the scope specified. |

## `SELECT` examples

Get a list of current usage for all resources for the scope specified.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_usages', value: 'view', },
        { label: 'usages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
is_quota_applicable,
properties,
quota_period,
resourceName,
resource_type,
scope,
type,
unit,
usages
FROM azure.quota.vw_usages
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.quota.usages
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

