---
title: edge_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_modules
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>edge_modules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.edge_modules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_edge_modules', value: 'view', },
        { label: 'edge_modules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="edgeModuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="edge_module_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Application level properties for the edge module resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, edgeModuleName, resourceGroupName, subscriptionId" /> | Retrieves an existing edge module resource with the given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all existing edge module resources, along with their JSON representations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, edgeModuleName, resourceGroupName, subscriptionId" /> | Creates a new edge module or updates an existing one. An edge module resource enables a single instance of an Azure Video Analyzer IoT edge module to interact with the Video Analyzer Account. This is used for authorization and also to make sure that the particular edge module instance only has access to the data it requires from the Azure Video Analyzer service. A new edge module resource should be created for every new instance of an Azure Video Analyzer edge module deployed to you Azure IoT edge environment. Edge module resources can be deleted if the specific module is not in use anymore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, edgeModuleName, resourceGroupName, subscriptionId" /> | Deletes an existing edge module resource. Deleting the edge module resource will prevent an Azure Video Analyzer IoT edge module which was previously initiated with the module provisioning token from communicating with the cloud. |

## `SELECT` examples

List all existing edge module resources, along with their JSON representations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_edge_modules', value: 'view', },
        { label: 'edge_modules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
edgeModuleName,
edge_module_id,
resourceGroupName,
subscriptionId
FROM azure.video_analyzer.vw_edge_modules
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.video_analyzer.edge_modules
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>edge_modules</code> resource.

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
INSERT INTO azure.video_analyzer.edge_modules (
accountName,
edgeModuleName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ edgeModuleName }}',
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
        - name: edgeModuleId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>edge_modules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.video_analyzer.edge_modules
WHERE accountName = '{{ accountName }}'
AND edgeModuleName = '{{ edgeModuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
