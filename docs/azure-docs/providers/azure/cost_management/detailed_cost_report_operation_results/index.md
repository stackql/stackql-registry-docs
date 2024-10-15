---
title: detailed_cost_report_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - detailed_cost_report_operation_results
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>detailed_cost_report_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detailed_cost_report_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.detailed_cost_report_operation_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_detailed_cost_report_operation_results', value: 'view', },
        { label: 'detailed_cost_report_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ARM resource id of the long running operation. |
| <CopyableCode code="name" /> | `text` | The name of the long running operation. |
| <CopyableCode code="download_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the long running operation. |
| <CopyableCode code="valid_till" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ARM resource id of the long running operation. |
| <CopyableCode code="name" /> | `string` | The name of the long running operation. |
| <CopyableCode code="properties" /> | `object` | The URL to download the generated report. |
| <CopyableCode code="type" /> | `string` | The type of the long running operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, scope" /> | Gets the result of the specified operation. The link with this operationId is provided as a response header of the initial request. |

## `SELECT` examples

Gets the result of the specified operation. The link with this operationId is provided as a response header of the initial request.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_detailed_cost_report_operation_results', value: 'view', },
        { label: 'detailed_cost_report_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
download_url,
expiry_time,
operationId,
scope,
type,
valid_till
FROM azure.cost_management.vw_detailed_cost_report_operation_results
WHERE operationId = '{{ operationId }}'
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
FROM azure.cost_management.detailed_cost_report_operation_results
WHERE operationId = '{{ operationId }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>

