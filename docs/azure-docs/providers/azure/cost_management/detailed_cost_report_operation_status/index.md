---
title: detailed_cost_report_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - detailed_cost_report_operation_status
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

Creates, updates, deletes, gets or lists a <code>detailed_cost_report_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detailed_cost_report_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.detailed_cost_report_operation_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_detailed_cost_report_operation_status', value: 'view', },
        { label: 'detailed_cost_report_operation_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the long running operation. |
| <CopyableCode code="name" /> | `text` | The name of the long running operation. |
| <CopyableCode code="download_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | The details of the error. |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | The status of the long running operation. |
| <CopyableCode code="type" /> | `text` | The type of the long running operation. |
| <CopyableCode code="valid_till" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the long running operation. |
| <CopyableCode code="name" /> | `string` | The name of the long running operation. |
| <CopyableCode code="endTime" /> | `string` | The endTime of the operation. |
| <CopyableCode code="error" /> | `object` | The details of the error. |
| <CopyableCode code="properties" /> | `object` | The URL to download the generated report. |
| <CopyableCode code="startTime" /> | `string` | The startTime of the operation. |
| <CopyableCode code="status" /> | `object` | The status of the long running operation. |
| <CopyableCode code="type" /> | `string` | The type of the long running operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, scope" /> | Get the status of the specified operation. This link is provided in the GenerateDetailedCostReport creation request response header. |

## `SELECT` examples

Get the status of the specified operation. This link is provided in the GenerateDetailedCostReport creation request response header.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_detailed_cost_report_operation_status', value: 'view', },
        { label: 'detailed_cost_report_operation_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
download_url,
end_time,
error,
expiry_time,
operationId,
scope,
start_time,
status,
type,
valid_till
FROM azure.cost_management.vw_detailed_cost_report_operation_status
WHERE operationId = '{{ operationId }}'
AND scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
endTime,
error,
properties,
startTime,
status,
type
FROM azure.cost_management.detailed_cost_report_operation_status
WHERE operationId = '{{ operationId }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>

