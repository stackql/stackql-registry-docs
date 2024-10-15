---
title: managed_instance_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_operations
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_operations', value: 'view', },
        { label: 'managed_instance_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="estimated_completion_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_cancellable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_user_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_instance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a managed instance operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, operationId, resourceGroupName, subscriptionId" /> | Gets a management operation on a managed instance. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="managedInstanceName, operationId, resourceGroupName, subscriptionId" /> | Cancels the asynchronous operation on the managed instance. |

## `SELECT` examples

Gets a management operation on a managed instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_operations', value: 'view', },
        { label: 'managed_instance_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
error_code,
error_description,
error_severity,
estimated_completion_time,
is_cancellable,
is_user_error,
managedInstanceName,
managed_instance_name,
operation,
operationId,
operation_friendly_name,
operation_parameters,
operation_steps,
percent_complete,
resourceGroupName,
start_time,
state,
subscriptionId
FROM azure.sql.vw_managed_instance_operations
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_instance_operations
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

