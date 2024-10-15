---
title: logic_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - logic_apps
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>logic_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logic_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.logic_apps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_logic_apps', value: 'view', },
        { label: 'logic_apps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containerAppName" /> | `text` | field from the `properties` object |
| <CopyableCode code="logicAppName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of logic apps extension. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId" /> | Create or update a Logic App extension resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId" /> | Deletes a Logic App extension resource |
| <CopyableCode code="deploy_workflow_artifacts" /> | `EXEC` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId" /> | Creates or updates the artifacts for the logic app |
| <CopyableCode code="invoke" /> | `EXEC` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId, x-ms-logicApps-proxy-method, x-ms-logicApps-proxy-path" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_logic_apps', value: 'view', },
        { label: 'logic_apps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
containerAppName,
logicAppName,
resourceGroupName,
subscriptionId
FROM azure.container_apps.vw_logic_apps
WHERE containerAppName = '{{ containerAppName }}'
AND logicAppName = '{{ logicAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_apps.logic_apps
WHERE containerAppName = '{{ containerAppName }}'
AND logicAppName = '{{ logicAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logic_apps</code> resource.

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
INSERT INTO azure.container_apps.logic_apps (
containerAppName,
logicAppName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ containerAppName }}',
'{{ logicAppName }}',
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
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>logic_apps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.logic_apps
WHERE containerAppName = '{{ containerAppName }}'
AND logicAppName = '{{ logicAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
