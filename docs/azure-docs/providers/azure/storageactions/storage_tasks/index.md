---
title: storage_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_tasks
  - storageactions
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

Creates, updates, deletes, gets or lists a <code>storage_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storageactions.storage_tasks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_tasks', value: 'view', },
        { label: 'storage_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time_in_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageTaskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="task_version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the storage task. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageTaskName, subscriptionId" /> | Get the storage task properties |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the storage tasks available under the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the storage tasks available under the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageTaskName, subscriptionId, data__identity, data__properties" /> | Asynchronously creates a new storage task resource with the specified parameters. If a storage task is already created and a subsequent create request is issued with different properties, the storage task properties will be updated. If a storage task is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageTaskName, subscriptionId" /> | Delete the storage task resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, storageTaskName, subscriptionId" /> | Update storage task properties |
| <CopyableCode code="preview_actions" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__properties" /> | Runs the input conditions against input object metadata properties and designates matched objects in response. |

## `SELECT` examples

Lists all the storage tasks available under the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_tasks', value: 'view', },
        { label: 'storage_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
action,
creation_time_in_utc,
enabled,
identity,
location,
provisioning_state,
resourceGroupName,
storageTaskName,
subscriptionId,
tags,
task_version
FROM azure.storageactions.vw_storage_tasks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.storageactions.storage_tasks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_tasks</code> resource.

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
INSERT INTO azure.storageactions.storage_tasks (
resourceGroupName,
storageTaskName,
subscriptionId,
data__identity,
data__properties,
identity,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ storageTaskName }}',
'{{ subscriptionId }}',
'{{ data__identity }}',
'{{ data__properties }}',
'{{ identity }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: taskVersion
          value: integer
        - name: enabled
          value: boolean
        - name: description
          value: string
        - name: action
          value:
            - name: if
              value:
                - name: condition
                  value: string
                - name: operations
                  value:
                    - - name: name
                        value: string
                      - name: parameters
                        value: object
                      - name: onSuccess
                        value: string
                      - name: onFailure
                        value: string
            - name: else
              value:
                - name: operations
                  value:
                    - - name: name
                        value: string
                      - name: parameters
                        value: object
                      - name: onSuccess
                        value: string
                      - name: onFailure
                        value: string
        - name: provisioningState
          value: string
        - name: creationTimeInUtc
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>storage_tasks</code> resource.

```sql
/*+ update */
UPDATE azure.storageactions.storage_tasks
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskName = '{{ storageTaskName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>storage_tasks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storageactions.storage_tasks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskName = '{{ storageTaskName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
