---
title: registry_environment_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_environment_versions
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

Creates, updates, deletes, gets or lists a <code>registry_environment_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_environment_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.registry_environment_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registry_environment_versions', value: 'view', },
        { label: 'registry_environment_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_rebuild" /> | `text` | field from the `properties` object |
| <CopyableCode code="build" /> | `text` | field from the `properties` object |
| <CopyableCode code="conda_file" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="inference_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_anonymous" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archived" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stage" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Environment version details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId, version" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId, version, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId, version" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registry_environment_versions', value: 'view', },
        { label: 'registry_environment_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_rebuild,
build,
conda_file,
environmentName,
environment_type,
image,
inference_config,
is_anonymous,
is_archived,
os_type,
provisioning_state,
registryName,
resourceGroupName,
stage,
subscriptionId,
version
FROM azure.ml_services.vw_registry_environment_versions
WHERE environmentName = '{{ environmentName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.ml_services.registry_environment_versions
WHERE environmentName = '{{ environmentName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registry_environment_versions</code> resource.

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
INSERT INTO azure.ml_services.registry_environment_versions (
environmentName,
registryName,
resourceGroupName,
subscriptionId,
version,
data__properties,
properties
)
SELECT 
'{{ environmentName }}',
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
        - name: autoRebuild
          value: []
        - name: build
          value:
            - name: contextUri
              value: string
            - name: dockerfilePath
              value: string
        - name: condaFile
          value: string
        - name: environmentType
          value: []
        - name: image
          value: string
        - name: inferenceConfig
          value:
            - name: livenessRoute
              value:
                - name: path
                  value: string
                - name: port
                  value: integer
        - name: osType
          value: []
        - name: provisioningState
          value: []
        - name: stage
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registry_environment_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.registry_environment_versions
WHERE environmentName = '{{ environmentName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}';
```
