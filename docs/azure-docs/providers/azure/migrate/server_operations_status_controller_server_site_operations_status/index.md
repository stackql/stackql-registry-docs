---
title: server_operations_status_controller_server_site_operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - server_operations_status_controller_server_site_operations_status
  - migrate
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

Creates, updates, deletes, gets or lists a <code>server_operations_status_controller_server_site_operations_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_operations_status_controller_server_site_operations_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_operations_status_controller_server_site_operations_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_operations_status_controller_server_site_operations_status', value: 'view', },
        { label: 'server_operations_status_controller_server_site_operations_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the Id. |
| <CopyableCode code="name" /> | `text` | Gets the operation name. |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | Class for operation status errors. |
| <CopyableCode code="operationStatusName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="result" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | Gets the status of the operation. ARM expects the terminal status to be one
of
            Succeeded/ Failed/ Canceled. All other values imply that the
operation is still running. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the Id. |
| <CopyableCode code="name" /> | `string` | Gets the operation name. |
| <CopyableCode code="endTime" /> | `string` | Gets the start time. |
| <CopyableCode code="error" /> | `object` | Class for operation status errors. |
| <CopyableCode code="properties" /> | `object` | Class for operation result properties. |
| <CopyableCode code="startTime" /> | `string` | Gets the start time. |
| <CopyableCode code="status" /> | `string` | Gets the status of the operation. ARM expects the terminal status to be one
of
            Succeeded/ Failed/ Canceled. All other values imply that the
operation is still running. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationStatusName, resourceGroupName, siteName, subscriptionId" /> | A operation status resource belonging to a site resource. |

## `SELECT` examples

A operation status resource belonging to a site resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_operations_status_controller_server_site_operations_status', value: 'view', },
        { label: 'server_operations_status_controller_server_site_operations_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
end_time,
error,
operationStatusName,
resourceGroupName,
result,
siteName,
start_time,
status,
subscriptionId
FROM azure.migrate.vw_server_operations_status_controller_server_site_operations_status
WHERE operationStatusName = '{{ operationStatusName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
status
FROM azure.migrate.server_operations_status_controller_server_site_operations_status
WHERE operationStatusName = '{{ operationStatusName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

