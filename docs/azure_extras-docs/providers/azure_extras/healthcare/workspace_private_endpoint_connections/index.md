---
title: workspace_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_private_endpoint_connections
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>workspace_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.workspace_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_private_endpoint_connections', value: 'view', },
        { label: 'workspace_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="privateEndpointConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the specified private endpoint connection associated with the workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all private endpoint connections for a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Update the state of the specified private endpoint connection associated with the workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a private endpoint connection. |

## `SELECT` examples

Lists all private endpoint connections for a workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_private_endpoint_connections', value: 'view', },
        { label: 'workspace_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
privateEndpointConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
workspaceName
FROM azure_extras.healthcare.vw_workspace_private_endpoint_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_extras.healthcare.workspace_private_endpoint_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_private_endpoint_connections</code> resource.

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
INSERT INTO azure_extras.healthcare.workspace_private_endpoint_connections (
privateEndpointConnectionName,
resourceGroupName,
subscriptionId,
workspaceName,
systemData,
properties
)
SELECT 
'{{ privateEndpointConnectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: privateEndpoint
          value:
            - name: id
              value: string
        - name: privateLinkServiceConnectionState
          value:
            - name: status
              value: []
            - name: description
              value: string
            - name: actionsRequired
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workspace_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.healthcare.workspace_private_endpoint_connections
WHERE privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
