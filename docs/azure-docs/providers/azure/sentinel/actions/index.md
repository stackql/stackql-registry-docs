---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.actions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_actions', value: 'view', },
        { label: 'actions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="actionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the action. |
| <CopyableCode code="logic_app_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="workflow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | Etag of the action. |
| <CopyableCode code="properties" /> | `object` | Action property bag. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionId, resourceGroupName, ruleId, subscriptionId, workspaceName" /> | Gets the action of alert rule. |
| <CopyableCode code="list_by_alert_rule" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleId, subscriptionId, workspaceName" /> | Gets all actions of alert rule. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="actionId, resourceGroupName, ruleId, subscriptionId, workspaceName" /> | Creates or updates the action of alert rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionId, resourceGroupName, ruleId, subscriptionId, workspaceName" /> | Delete the action of alert rule. |

## `SELECT` examples

Gets all actions of alert rule.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_actions', value: 'view', },
        { label: 'actions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actionId,
etag,
logic_app_resource_id,
resourceGroupName,
ruleId,
subscriptionId,
system_data,
type,
workflow_id,
workspaceName
FROM azure.sentinel.vw_actions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND ruleId = '{{ ruleId }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.sentinel.actions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND ruleId = '{{ ruleId }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>actions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.sentinel.actions (
actionId,
resourceGroupName,
ruleId,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ actionId }}',
'{{ resourceGroupName }}',
'{{ ruleId }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: logicAppResourceId
          value: string
        - name: triggerUri
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>actions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.actions
WHERE actionId = '{{ actionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleId = '{{ ruleId }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
