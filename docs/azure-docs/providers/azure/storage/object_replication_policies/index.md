---
title: object_replication_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - object_replication_policies
  - storage
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

Creates, updates, deletes, gets or lists a <code>object_replication_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_replication_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.object_replication_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_object_replication_policies', value: 'view', },
        { label: 'object_replication_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="objectReplicationPolicyId" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The Storage Account ObjectReplicationPolicy properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId" /> | Get the object replication policy of the storage account by policy ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List the object replication policies associated with the storage account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId" /> | Create or update the object replication policy of the storage account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId" /> | Deletes the object replication policy associated with the specified storage account. |

## `SELECT` examples

List the object replication policies associated with the storage account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_object_replication_policies', value: 'view', },
        { label: 'object_replication_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
destination_account,
enabled_time,
objectReplicationPolicyId,
policy_id,
resourceGroupName,
rules,
source_account,
subscriptionId,
type
FROM azure.storage.vw_object_replication_policies
WHERE accountName = '{{ accountName }}'
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
type
FROM azure.storage.object_replication_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>object_replication_policies</code> resource.

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
INSERT INTO azure.storage.object_replication_policies (
accountName,
objectReplicationPolicyId,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ objectReplicationPolicyId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: policyId
          value: string
        - name: enabledTime
          value: string
        - name: sourceAccount
          value: string
        - name: destinationAccount
          value: string
        - name: rules
          value:
            - - name: ruleId
                value: string
              - name: sourceContainer
                value: string
              - name: destinationContainer
                value: string
              - name: filters
                value:
                  - name: prefixMatch
                    value:
                      - string
                  - name: minCreationTime
                    value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>object_replication_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.object_replication_policies
WHERE accountName = '{{ accountName }}'
AND objectReplicationPolicyId = '{{ objectReplicationPolicyId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
