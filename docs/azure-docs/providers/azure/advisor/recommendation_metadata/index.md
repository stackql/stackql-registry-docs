---
title: recommendation_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendation_metadata
  - advisor
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

Creates, updates, deletes, gets or lists a <code>recommendation_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommendation_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.advisor.recommendation_metadata" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recommendation_metadata', value: 'view', },
        { label: 'recommendation_metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource Id of the metadata entity. |
| <CopyableCode code="name" /> | `text` | The name of the metadata entity. |
| <CopyableCode code="applicable_scenarios" /> | `text` | field from the `properties` object |
| <CopyableCode code="depends_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_values" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the metadata entity. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id of the metadata entity. |
| <CopyableCode code="name" /> | `string` | The name of the metadata entity. |
| <CopyableCode code="properties" /> | `object` | The metadata entity properties |
| <CopyableCode code="type" /> | `string` | The type of the metadata entity. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recommendation_metadata', value: 'view', },
        { label: 'recommendation_metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applicable_scenarios,
depends_on,
display_name,
supported_values,
type
FROM azure.advisor.vw_recommendation_metadata
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.advisor.recommendation_metadata
;
```
</TabItem></Tabs>

