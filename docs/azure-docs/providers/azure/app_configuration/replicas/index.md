---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.replicas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replicas', value: 'view', },
        { label: 'replicas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the replica. |
| <CopyableCode code="configStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the replica. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the replica. |
| <CopyableCode code="location" /> | `string` | The location of the replica. |
| <CopyableCode code="properties" /> | `object` | All replica properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, replicaName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified replica. |
| <CopyableCode code="list_by_configuration_store" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Lists the replicas for a given configuration store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="configStoreName, replicaName, resourceGroupName, subscriptionId" /> | Creates a replica with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, replicaName, resourceGroupName, subscriptionId" /> | Deletes a replica. |

## `SELECT` examples

Lists the replicas for a given configuration store.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replicas', value: 'view', },
        { label: 'replicas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configStoreName,
endpoint,
location,
provisioning_state,
replicaName,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.app_configuration.vw_replicas
WHERE configStoreName = '{{ configStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
systemData,
type
FROM azure.app_configuration.replicas
WHERE configStoreName = '{{ configStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replicas</code> resource.

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
INSERT INTO azure.app_configuration.replicas (
configStoreName,
replicaName,
resourceGroupName,
subscriptionId,
location
)
SELECT 
'{{ configStoreName }}',
'{{ replicaName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}'
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
    - name: location
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: endpoint
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>replicas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_configuration.replicas
WHERE configStoreName = '{{ configStoreName }}'
AND replicaName = '{{ replicaName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
