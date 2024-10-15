---
title: workspace_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_connections
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

Creates, updates, deletes, gets or lists a <code>workspace_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.workspace_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_connections', value: 'view', },
        { label: 'workspace_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="auth_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_workspace_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="group" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_shared_to_all" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="pe_requirement" /> | `text` | field from the `properties` object |
| <CopyableCode code="pe_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_user_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="use_workspace_managed_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="test_connection" /> | `EXEC` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_connections', value: 'view', },
        { label: 'workspace_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auth_type,
category,
connectionName,
created_by_workspace_arm_id,
error,
expiry_time,
group,
is_shared_to_all,
metadata,
pe_requirement,
pe_status,
resourceGroupName,
shared_user_list,
subscriptionId,
system_data,
target,
type,
use_workspace_managed_identity,
workspaceName
FROM azure.ml_services.vw_workspace_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.ml_services.workspace_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_connections</code> resource.

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
INSERT INTO azure.ml_services.workspace_connections (
connectionName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ connectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
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
        - name: authType
          value: []
        - name: category
          value: []
        - name: createdByWorkspaceArmId
          value: string
        - name: error
          value: string
        - name: expiryTime
          value: string
        - name: group
          value: []
        - name: isSharedToAll
          value: boolean
        - name: metadata
          value: object
        - name: peRequirement
          value: []
        - name: peStatus
          value: []
        - name: sharedUserList
          value:
            - string
        - name: target
          value: string
        - name: useWorkspaceManagedIdentity
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_connections</code> resource.

```sql
/*+ update */
UPDATE azure.ml_services.workspace_connections
SET 
properties = '{{ properties }}'
WHERE 
connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>workspace_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.workspace_connections
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
