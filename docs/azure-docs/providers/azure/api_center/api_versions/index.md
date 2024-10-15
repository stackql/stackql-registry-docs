---
title: api_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - api_versions
  - api_center
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

Creates, updates, deletes, gets or lists a <code>api_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.api_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_versions', value: 'view', },
        { label: 'api_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiName" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_stage" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="versionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API version properties entity. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Returns details of the API version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of API versions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Creates new or updates existing API version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Deletes specified API version |

## `SELECT` examples

Returns a collection of API versions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_versions', value: 'view', },
        { label: 'api_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiName,
lifecycle_stage,
resourceGroupName,
serviceName,
subscriptionId,
title,
versionName,
workspaceName
FROM azure.api_center.vw_api_versions
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_center.api_versions
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_versions</code> resource.

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
INSERT INTO azure.api_center.api_versions (
apiName,
resourceGroupName,
serviceName,
subscriptionId,
versionName,
workspaceName,
properties
)
SELECT 
'{{ apiName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ versionName }}',
'{{ workspaceName }}',
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
        - name: title
          value: string
        - name: lifecycleStage
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.api_versions
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}'
AND workspaceName = '{{ workspaceName }}';
```
