---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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

Creates, updates, deletes, gets or lists a <code>queues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.queues" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_queues', value: 'view', },
        { label: 'queues', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="approximate_message_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="queueName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Gets the queue with the specified queue name, under the specified account if it exists. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets a list of all the queues under the specified storage account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Creates a new queue with the specified queue name, under the specified account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Deletes the queue with the specified queue name, under the specified account if it exists. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, queueName, resourceGroupName, subscriptionId" /> | Creates a new queue with the specified queue name, under the specified account. |

## `SELECT` examples

Gets a list of all the queues under the specified storage account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_queues', value: 'view', },
        { label: 'queues', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
approximate_message_count,
metadata,
queueName,
resourceGroupName,
subscriptionId,
type
FROM azure.storage.vw_queues
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
FROM azure.storage.queues
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queues</code> resource.

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
INSERT INTO azure.storage.queues (
accountName,
queueName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ queueName }}',
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
        - name: metadata
          value: object
        - name: approximateMessageCount
          value: integer
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>queues</code> resource.

```sql
/*+ update */
UPDATE azure.storage.queues
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND queueName = '{{ queueName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>queues</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.queues
WHERE accountName = '{{ accountName }}'
AND queueName = '{{ queueName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
