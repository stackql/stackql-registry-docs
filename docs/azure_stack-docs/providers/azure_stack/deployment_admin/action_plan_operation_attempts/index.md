---
title: action_plan_operation_attempts
hide_title: false
hide_table_of_contents: false
keywords:
  - action_plan_operation_attempts
  - deployment_admin
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

Creates, updates, deletes, gets or lists a <code>action_plan_operation_attempts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_plan_operation_attempts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.action_plan_operation_attempts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_plan_operation_attempts', value: 'view', },
        { label: 'action_plan_operation_attempts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="planId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Operation Attempt Properties. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, operationId, planId, subscriptionId" /> | Returns the information about action plan operation attempt. |

## `SELECT` examples

Returns the information about action plan operation attempt.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_plan_operation_attempts', value: 'view', },
        { label: 'action_plan_operation_attempts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
end_time,
location,
operationId,
planId,
provisioning_state,
start_time,
subscriptionId,
type
FROM azure_stack.deployment_admin.vw_action_plan_operation_attempts
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND planId = '{{ planId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.deployment_admin.action_plan_operation_attempts
WHERE location = '{{ location }}'
AND operationId = '{{ operationId }}'
AND planId = '{{ planId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

