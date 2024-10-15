---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiName" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API deployment entity properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, deploymentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns details of the API deployment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of API deployments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiName, deploymentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Creates new or updates existing API deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, deploymentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Deletes API deployment. |

## `SELECT` examples

Returns a collection of API deployments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiName,
custom_properties,
definition_id,
deploymentName,
environment_id,
resourceGroupName,
server,
serviceName,
state,
subscriptionId,
title,
workspaceName
FROM azure.api_center.vw_deployments
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
FROM azure.api_center.deployments
WHERE apiName = '{{ apiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO azure.api_center.deployments (
apiName,
deploymentName,
resourceGroupName,
serviceName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ apiName }}',
'{{ deploymentName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
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
        - name: environmentId
          value: string
        - name: definitionId
          value: string
        - name: state
          value: []
        - name: server
          value:
            - name: runtimeUri
              value:
                - []
        - name: customProperties
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.deployments
WHERE apiName = '{{ apiName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
