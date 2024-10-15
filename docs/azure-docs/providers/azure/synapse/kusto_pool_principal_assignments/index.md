---
title: kusto_pool_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_principal_assignments
  - synapse
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

Creates, updates, deletes, gets or lists a <code>kusto_pool_principal_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pool_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_principal_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kusto_pool_principal_assignments', value: 'view', },
        { label: 'kusto_pool_principal_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="kustoPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="principalAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing cluster principal property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a Kusto pool principalAssignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Lists all Kusto pool principalAssignments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName" /> | Create a Kusto pool principalAssignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kustoPoolName, principalAssignmentName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a Kusto pool principalAssignment. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type" /> | Checks that the principal assignment name is valid and is not already in use. |

## `SELECT` examples

Lists all Kusto pool principalAssignments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kusto_pool_principal_assignments', value: 'view', },
        { label: 'kusto_pool_principal_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_object_id,
kustoPoolName,
principalAssignmentName,
principal_id,
principal_name,
principal_type,
provisioning_state,
resourceGroupName,
role,
subscriptionId,
system_data,
tenant_id,
tenant_name,
workspaceName
FROM azure.synapse.vw_kusto_pool_principal_assignments
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.synapse.kusto_pool_principal_assignments
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kusto_pool_principal_assignments</code> resource.

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
INSERT INTO azure.synapse.kusto_pool_principal_assignments (
kustoPoolName,
principalAssignmentName,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ kustoPoolName }}',
'{{ principalAssignmentName }}',
'{{ resourceGroupName }}',
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>kusto_pool_principal_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.kusto_pool_principal_assignments
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND principalAssignmentName = '{{ principalAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
