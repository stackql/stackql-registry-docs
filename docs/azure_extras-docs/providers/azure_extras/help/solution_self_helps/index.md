---
title: solution_self_helps
hide_title: false
hide_table_of_contents: false
keywords:
  - solution_self_helps
  - help
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

Creates, updates, deletes, gets or lists a <code>solution_self_helps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solution_self_helps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.solution_self_helps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solution_self_helps', value: 'view', },
        { label: 'solution_self_helps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="replacement_maps" /> | `text` | field from the `properties` object |
| <CopyableCode code="sections" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Solution result |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="solutionId" /> | Gets Self Help Solutions for a given solutionId. Self Help Solutions consist of rich instructional video tutorials, links and guides to public documentation related to a specific problem that enables users to troubleshoot Azure issues. |

## `SELECT` examples

Gets Self Help Solutions for a given solutionId. Self Help Solutions consist of rich instructional video tutorials, links and guides to public documentation related to a specific problem that enables users to troubleshoot Azure issues.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solution_self_helps', value: 'view', },
        { label: 'solution_self_helps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
content,
replacement_maps,
sections,
solutionId,
solution_id,
title
FROM azure_extras.help.vw_solution_self_helps
WHERE solutionId = '{{ solutionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.help.solution_self_helps
WHERE solutionId = '{{ solutionId }}';
```
</TabItem></Tabs>

