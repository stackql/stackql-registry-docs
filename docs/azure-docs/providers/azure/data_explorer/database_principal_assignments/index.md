---
title: database_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - database_principal_assignments
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>database_principal_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.database_principal_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_principal_assignments', value: 'view', },
        { label: 'database_principal_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="principalAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing database principal property. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Gets a Kusto cluster database principalAssignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Lists all Kusto cluster database principalAssignments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, databaseName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Creates a Kusto cluster database principalAssignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, databaseName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Deletes a Kusto principalAssignment. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the database principal assignment is valid and is not already in use. |

## `SELECT` examples

Lists all Kusto cluster database principalAssignments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_principal_assignments', value: 'view', },
        { label: 'database_principal_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_object_id,
clusterName,
databaseName,
principalAssignmentName,
principal_id,
principal_name,
principal_type,
provisioning_state,
resourceGroupName,
role,
subscriptionId,
tenant_id,
tenant_name
FROM azure.data_explorer.vw_database_principal_assignments
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.data_explorer.database_principal_assignments
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_principal_assignments</code> resource.

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
INSERT INTO azure.data_explorer.database_principal_assignments (
clusterName,
databaseName,
principalAssignmentName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ databaseName }}',
'{{ principalAssignmentName }}',
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
        - name: principalId
          value: string
        - name: role
          value: string
        - name: tenantId
          value: string
        - name: principalType
          value: string
        - name: tenantName
          value: string
        - name: principalName
          value: string
        - name: provisioningState
          value: []
        - name: aadObjectId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>database_principal_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.database_principal_assignments
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND principalAssignmentName = '{{ principalAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
