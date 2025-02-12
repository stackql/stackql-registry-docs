---
title: protection_intents
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_intents
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>protection_intents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protection_intents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protection_intents', value: 'view', },
        { label: 'protection_intents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="backup_management_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="intentObjectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_intent_item_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Base class for backup ProtectionIntent. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName" /> | Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,
call the GetItemOperationResult API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName" /> | Create Intent for Enabling backup of an item. This is a synchronous operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName" /> | Used to remove intent from an item |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="azureRegion, subscriptionId" /> |  |

## `SELECT` examples

Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,
call the GetItemOperationResult API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protection_intents', value: 'view', },
        { label: 'protection_intents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_management_type,
fabricName,
intentObjectName,
item_id,
policy_id,
protection_intent_item_type,
protection_state,
resourceGroupName,
source_resource_id,
subscriptionId,
type,
vaultName
FROM azure.recovery_services_backup.vw_protection_intents
WHERE fabricName = '{{ fabricName }}'
AND intentObjectName = '{{ intentObjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.recovery_services_backup.protection_intents
WHERE fabricName = '{{ fabricName }}'
AND intentObjectName = '{{ intentObjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>protection_intents</code> resource.

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
INSERT INTO azure.recovery_services_backup.protection_intents (
fabricName,
intentObjectName,
resourceGroupName,
subscriptionId,
vaultName,
properties
)
SELECT 
'{{ fabricName }}',
'{{ intentObjectName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: protectionIntentItemType
          value: string
        - name: backupManagementType
          value: string
        - name: sourceResourceId
          value: string
        - name: itemId
          value: string
        - name: policyId
          value: string
        - name: protectionState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>protection_intents</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_backup.protection_intents
WHERE fabricName = '{{ fabricName }}'
AND intentObjectName = '{{ intentObjectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
