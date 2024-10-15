---
title: api_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - api_definitions
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

Creates, updates, deletes, gets or lists a <code>api_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.api_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_definitions', value: 'view', },
        { label: 'api_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiName" /> | `text` | field from the `properties` object |
| <CopyableCode code="definitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="specification" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="versionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API definition properties entity. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Returns details of the API definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Returns a collection of API definitions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Creates new or updates existing API definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Deletes specified API definition. |
| <CopyableCode code="export_specification" /> | `EXEC` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Exports the API specification. |
| <CopyableCode code="import_specification" /> | `EXEC` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Imports the API specification. |

## `SELECT` examples

Returns a collection of API definitions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_definitions', value: 'view', },
        { label: 'api_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiName,
definitionName,
resourceGroupName,
serviceName,
specification,
subscriptionId,
title,
versionName,
workspaceName
FROM azure.api_center.vw_api_definitions
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_center.api_definitions
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_definitions</code> resource.

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
INSERT INTO azure.api_center.api_definitions (
apiName,
definitionName,
resourceGroupName,
serviceName,
subscriptionId,
versionName,
workspaceName,
properties
)
SELECT 
'{{ apiName }}',
'{{ definitionName }}',
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
        - name: description
          value: string
        - name: specification
          value:
            - name: name
              value: string
            - name: version
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.api_definitions
WHERE apiName = '{{ apiName }}'
AND definitionName = '{{ definitionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND versionName = '{{ versionName }}'
AND workspaceName = '{{ workspaceName }}';
```
