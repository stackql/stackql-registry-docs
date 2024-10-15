---
title: access_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy_assignments
  - redis_enterprise
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

Creates, updates, deletes, gets or lists a <code>access_policy_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policy_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.access_policy_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policy_assignments', value: 'view', },
        { label: 'access_policy_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessPolicyAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="user" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of Redis Enterprise database access policy assignment. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyAssignmentName, clusterName, databaseName, resourceGroupName, subscriptionId" /> | Gets information about access policy assignment for database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Gets all access policy assignments.. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accessPolicyAssignmentName, clusterName, databaseName, resourceGroupName, subscriptionId" /> | Creates/Updates a particular access policy assignment for a database |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyAssignmentName, clusterName, databaseName, resourceGroupName, subscriptionId" /> | Deletes a single access policy assignment. |

## `SELECT` examples

Gets all access policy assignments..

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policy_assignments', value: 'view', },
        { label: 'access_policy_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accessPolicyAssignmentName,
access_policy_name,
clusterName,
databaseName,
provisioning_state,
resourceGroupName,
subscriptionId,
user
FROM azure_isv.redis_enterprise.vw_access_policy_assignments
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
FROM azure_isv.redis_enterprise.access_policy_assignments
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_policy_assignments</code> resource.

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
INSERT INTO azure_isv.redis_enterprise.access_policy_assignments (
accessPolicyAssignmentName,
clusterName,
databaseName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accessPolicyAssignmentName }}',
'{{ clusterName }}',
'{{ databaseName }}',
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
        - name: provisioningState
          value: []
        - name: accessPolicyName
          value: string
        - name: user
          value:
            - name: objectId
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>access_policy_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis_enterprise.access_policy_assignments
WHERE accessPolicyAssignmentName = '{{ accessPolicyAssignmentName }}'
AND clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
