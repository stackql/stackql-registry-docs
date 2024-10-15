---
title: alerts_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_summaries
  - alerts_management
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

Creates, updates, deletes, gets or lists a <code>alerts_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alerts_summaries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_summaries', value: 'view', },
        { label: 'alerts_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="groupby" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupedby" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="smart_groups_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="total" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
| <CopyableCode code="values" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Group the result set. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupby, scope" /> | Get a summarized count of your alerts grouped by various parameters (e.g. grouping by 'Severity' returns the count of alerts for each severity). |

## `SELECT` examples

Get a summarized count of your alerts grouped by various parameters (e.g. grouping by 'Severity' returns the count of alerts for each severity).

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_summaries', value: 'view', },
        { label: 'alerts_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
groupby,
groupedby,
scope,
smart_groups_count,
total,
type,
values
FROM azure.alerts_management.vw_alerts_summaries
WHERE groupby = '{{ groupby }}'
AND scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.alerts_management.alerts_summaries
WHERE groupby = '{{ groupby }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>

