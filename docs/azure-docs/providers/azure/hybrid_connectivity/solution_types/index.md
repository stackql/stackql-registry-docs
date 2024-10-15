---
title: solution_types
hide_title: false
hide_table_of_contents: false
keywords:
  - solution_types
  - hybrid_connectivity
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

Creates, updates, deletes, gets or lists a <code>solution_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solution_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.solution_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solution_types', value: 'view', },
        { label: 'solution_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionType" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_azure_regions" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of Solution type resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionType, subscriptionId" /> | Get a SolutionTypeResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List SolutionTypeResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List SolutionTypeResource resources by subscription ID |

## `SELECT` examples

List SolutionTypeResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solution_types', value: 'view', },
        { label: 'solution_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
resourceGroupName,
solutionType,
solution_settings,
solution_type,
subscriptionId,
supported_azure_regions
FROM azure.hybrid_connectivity.vw_solution_types
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.hybrid_connectivity.solution_types
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

