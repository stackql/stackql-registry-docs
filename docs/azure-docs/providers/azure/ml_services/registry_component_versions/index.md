---
title: registry_component_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_component_versions
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>registry_component_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_component_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.registry_component_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registry_component_versions', value: 'view', },
        { label: 'registry_component_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="componentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="component_spec" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_anonymous" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archived" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of a component version: defines resources that span component types. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, registryName, resourceGroupName, subscriptionId, version" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="componentName, registryName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="componentName, registryName, resourceGroupName, subscriptionId, version, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="componentName, registryName, resourceGroupName, subscriptionId, version" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registry_component_versions', value: 'view', },
        { label: 'registry_component_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
componentName,
component_spec,
is_anonymous,
is_archived,
provisioning_state,
registryName,
resourceGroupName,
subscriptionId,
version
FROM azure.ml_services.vw_registry_component_versions
WHERE componentName = '{{ componentName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.ml_services.registry_component_versions
WHERE componentName = '{{ componentName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registry_component_versions</code> resource.

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
INSERT INTO azure.ml_services.registry_component_versions (
componentName,
registryName,
resourceGroupName,
subscriptionId,
version,
data__properties,
properties
)
SELECT 
'{{ componentName }}',
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ version }}',
'{{ data__properties }}',
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
        - name: isAnonymous
          value: boolean
        - name: isArchived
          value: boolean
        - name: componentSpec
          value: object
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registry_component_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.registry_component_versions
WHERE componentName = '{{ componentName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}';
```
