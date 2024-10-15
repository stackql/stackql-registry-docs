---
title: import_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - import_pipelines
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>import_pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.import_pipelines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_pipelines', value: 'view', },
        { label: 'import_pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `text` | Managed identity for the resource. |
| <CopyableCode code="importPipelineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the import pipeline. |
| <CopyableCode code="options" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the import pipeline. |
| <CopyableCode code="properties" /> | `object` | The properties of an import pipeline. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importPipelineName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the import pipeline. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all import pipelines for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="importPipelineName, registryName, resourceGroupName, subscriptionId" /> | Creates an import pipeline for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="importPipelineName, registryName, resourceGroupName, subscriptionId" /> | Deletes an import pipeline from a container registry. |

## `SELECT` examples

Lists all import pipelines for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_pipelines', value: 'view', },
        { label: 'import_pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
identity,
importPipelineName,
location,
options,
provisioning_state,
registryName,
resourceGroupName,
source,
subscriptionId,
trigger
FROM azure.container_registry.vw_import_pipelines
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties
FROM azure.container_registry.import_pipelines
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>import_pipelines</code> resource.

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
INSERT INTO azure.container_registry.import_pipelines (
importPipelineName,
registryName,
resourceGroupName,
subscriptionId,
location,
identity,
properties
)
SELECT 
'{{ importPipelineName }}',
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: source
          value:
            - name: type
              value: string
            - name: uri
              value: string
            - name: keyVaultUri
              value: string
        - name: trigger
          value:
            - name: sourceTrigger
              value:
                - name: status
                  value: string
        - name: options
          value:
            - string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>import_pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.import_pipelines
WHERE importPipelineName = '{{ importPipelineName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
