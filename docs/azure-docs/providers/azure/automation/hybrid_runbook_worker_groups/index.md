---
title: hybrid_runbook_worker_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_runbook_worker_groups
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

Creates, updates, deletes, gets or lists a <code>hybrid_runbook_worker_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_runbook_worker_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.hybrid_runbook_worker_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_runbook_worker_groups', value: 'view', },
        { label: 'hybrid_runbook_worker_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybridRunbookWorkerGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Definition of hybrid runbook worker group property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Retrieve a hybrid runbook worker group. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of hybrid runbook worker groups. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Create a hybrid runbook worker group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Delete a hybrid runbook worker group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, hybridRunbookWorkerGroupName, resourceGroupName, subscriptionId" /> | Update a hybrid runbook worker group. |

## `SELECT` examples

Retrieve a list of hybrid runbook worker groups.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_runbook_worker_groups', value: 'view', },
        { label: 'hybrid_runbook_worker_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
automationAccountName,
credential,
group_type,
hybridRunbookWorkerGroupName,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.automation.vw_hybrid_runbook_worker_groups
WHERE automationAccountName = '{{ automationAccountName }}'
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
FROM azure.automation.hybrid_runbook_worker_groups
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hybrid_runbook_worker_groups</code> resource.

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
INSERT INTO azure.automation.hybrid_runbook_worker_groups (
automationAccountName,
hybridRunbookWorkerGroupName,
resourceGroupName,
subscriptionId,
properties,
name
)
SELECT 
'{{ automationAccountName }}',
'{{ hybridRunbookWorkerGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: credential
          value:
            - name: name
              value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>hybrid_runbook_worker_groups</code> resource.

```sql
/*+ update */
UPDATE azure.automation.hybrid_runbook_worker_groups
SET 
properties = '{{ properties }}',
name = '{{ name }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND hybridRunbookWorkerGroupName = '{{ hybridRunbookWorkerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>hybrid_runbook_worker_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.hybrid_runbook_worker_groups
WHERE automationAccountName = '{{ automationAccountName }}'
AND hybridRunbookWorkerGroupName = '{{ hybridRunbookWorkerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
