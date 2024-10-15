---
title: container_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registries
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>container_registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.container_registries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_container_registries', value: 'view', },
        { label: 'container_registries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containerRegistryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Container registry resource payload. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId" /> | Get the container registries resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List container registries resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId" /> | Create or update container registry resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId" /> | Delete a container registry resource. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId, data__credentials" /> | Check if the container registry properties are valid. |

## `SELECT` examples

List container registries resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_container_registries', value: 'view', },
        { label: 'container_registries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
containerRegistryName,
credentials,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.spring_apps.vw_container_registries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.container_registries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>container_registries</code> resource.

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
INSERT INTO azure.spring_apps.container_registries (
containerRegistryName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ containerRegistryName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: credentials
          value:
            - name: type
              value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>container_registries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.container_registries
WHERE containerRegistryName = '{{ containerRegistryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
