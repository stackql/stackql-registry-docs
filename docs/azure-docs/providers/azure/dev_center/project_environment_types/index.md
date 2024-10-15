---
title: project_environment_types
hide_title: false
hide_table_of_contents: false
keywords:
  - project_environment_types
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>project_environment_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_environment_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.project_environment_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_project_environment_types', value: 'view', },
        { label: 'project_environment_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="creator_role_assignment" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_target_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location for the environment type |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="user_role_assignments" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location for the environment type |
| <CopyableCode code="properties" /> | `object` | Properties of a project environment type. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Gets a project environment type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists environment types for a project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Creates or updates a project environment type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Deletes a project environment type. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Partially updates a project environment type. |

## `SELECT` examples

Lists environment types for a project.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_project_environment_types', value: 'view', },
        { label: 'project_environment_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
creator_role_assignment,
deployment_target_id,
display_name,
environmentTypeName,
environment_count,
identity,
location,
projectName,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
system_data,
tags,
type,
user_role_assignments
FROM azure.dev_center.vw_project_environment_types
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
systemData,
tags,
type
FROM azure.dev_center.project_environment_types
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project_environment_types</code> resource.

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
INSERT INTO azure.dev_center.project_environment_types (
environmentTypeName,
projectName,
resourceGroupName,
subscriptionId,
properties,
tags,
identity,
location
)
SELECT 
'{{ environmentTypeName }}',
'{{ projectName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ identity }}',
'{{ location }}'
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
        - name: deploymentTargetId
          value: string
        - name: displayName
          value: string
        - name: status
          value: []
        - name: creatorRoleAssignment
          value:
            - name: roles
              value: object
        - name: userRoleAssignments
          value: object
        - name: provisioningState
          value: []
        - name: environmentCount
          value: integer
    - name: tags
      value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>project_environment_types</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.project_environment_types
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
environmentTypeName = '{{ environmentTypeName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>project_environment_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.project_environment_types
WHERE environmentTypeName = '{{ environmentTypeName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
