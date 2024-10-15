---
title: hybrid_runbook_workers
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_workers
  - automation
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

Creates, updates, deletes, gets or lists a <code>hybrid_runbook_workers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_runbook_workers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.hybrid_runbook_workers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_runbook_workers', value: 'view', },
        { label: 'hybrid_runbook_workers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybridRunbookWorkerGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybridRunbookWorkerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_seen_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="registered_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vm_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="worker_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="worker_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Definition of hybrid runbook worker property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId" /> | Retrieve a hybrid runbook worker. |
| <CopyableCode code="list_by_hybrid_runbook_worker_group" /> | `SELECT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Retrieve a list of hybrid runbook workers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId, data__properties" /> | Create a hybrid runbook worker. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId" /> | Delete a hybrid runbook worker. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, hybridRunbookWorkerId, resourceGroupName, subscriptionId" /> | Move a hybrid worker to a different group. |

## `SELECT` examples

Retrieve a list of hybrid runbook workers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_runbook_workers', value: 'view', },
        { label: 'hybrid_runbook_workers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
automationAccountName,
hybridRunbookWorkerGroupName,
hybridRunbookWorkerId,
ip,
last_seen_date_time,
registered_date_time,
resourceGroupName,
subscriptionId,
system_data,
type,
vm_resource_id,
worker_name,
worker_type
FROM azure.automation.vw_hybrid_runbook_workers
WHERE automationAccountName = '{{ automationAccountName }}'
AND hybridRunbookWorkerGroupName = '{{ hybridRunbookWorkerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.automation.hybrid_runbook_workers
WHERE automationAccountName = '{{ automationAccountName }}'
AND hybridRunbookWorkerGroupName = '{{ hybridRunbookWorkerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hybrid_runbook_workers</code> resource.

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
INSERT INTO azure.automation.hybrid_runbook_workers (
automationAccountName,
hybridRunbookWorkerGroupName,
hybridRunbookWorkerId,
resourceGroupName,
subscriptionId,
data__properties,
properties,
name
)
SELECT 
'{{ automationAccountName }}',
'{{ hybridRunbookWorkerGroupName }}',
'{{ hybridRunbookWorkerId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: vmResourceId
          value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hybrid_runbook_workers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.hybrid_runbook_workers
WHERE automationAccountName = '{{ automationAccountName }}'
AND hybridRunbookWorkerGroupName = '{{ hybridRunbookWorkerGroupName }}'
AND hybridRunbookWorkerId = '{{ hybridRunbookWorkerId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
