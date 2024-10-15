---
title: workspace_global_schemata
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_global_schemata
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_global_schemata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_global_schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_global_schemata" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_global_schemata', value: 'view', },
        { label: 'workspace_global_schemata', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="document" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaId" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Schema create or update contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaId, serviceName, subscriptionId, workspaceId" /> | Gets the details of the Schema specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of schemas registered with workspace in a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, schemaId, serviceName, subscriptionId, workspaceId" /> | Creates new or updates existing specified Schema of the workspace in an API Management service instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, schemaId, serviceName, subscriptionId, workspaceId" /> | Deletes specific Schema. |

## `SELECT` examples

Lists a collection of schemas registered with workspace in a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_global_schemata', value: 'view', },
        { label: 'workspace_global_schemata', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
document,
provisioning_state,
resourceGroupName,
schemaId,
schema_type,
serviceName,
subscriptionId,
value,
workspaceId
FROM azure.api_management.vw_workspace_global_schemata
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_global_schemata
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_global_schemata</code> resource.

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
INSERT INTO azure.api_management.workspace_global_schemata (
resourceGroupName,
schemaId,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ schemaId }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
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
        - name: schemaType
          value: string
        - name: description
          value: string
        - name: value
          value: string
        - name: document
          value: []
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workspace_global_schemata</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_global_schemata
WHERE If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaId = '{{ schemaId }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
