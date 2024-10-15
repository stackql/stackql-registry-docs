---
title: cluster_principal_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_principal_assignments
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

Creates, updates, deletes, gets or lists a <code>cluster_principal_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_principal_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.cluster_principal_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_principal_assignments', value: 'view', },
        { label: 'cluster_principal_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | A class representing cluster principal property. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Gets a Kusto cluster principalAssignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all Kusto cluster principalAssignments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Create a Kusto cluster principalAssignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, principalAssignmentName, resourceGroupName, subscriptionId" /> | Deletes a Kusto cluster principalAssignment. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the principal assignment name is valid and is not already in use. |

## `SELECT` examples

Lists all Kusto cluster principalAssignments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_principal_assignments', value: 'view', },
        { label: 'cluster_principal_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_object_id,
clusterName,
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
FROM azure.data_explorer.vw_cluster_principal_assignments
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.data_explorer.cluster_principal_assignments
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_principal_assignments</code> resource.

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
INSERT INTO azure.data_explorer.cluster_principal_assignments (
clusterName,
principalAssignmentName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
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

Deletes the specified <code>cluster_principal_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.cluster_principal_assignments
WHERE clusterName = '{{ clusterName }}'
AND principalAssignmentName = '{{ principalAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
