---
title: access_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy_assignments
  - redis
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.access_policy_assignments" /></td></tr>
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
| <CopyableCode code="cacheName" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id_alias" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties for an access policy assignment |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyAssignmentName, cacheName, resourceGroupName, subscriptionId" /> | Gets the list of assignments for an access policy of a redis cache |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Gets the list of access policy assignments associated with this redis cache |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accessPolicyAssignmentName, cacheName, resourceGroupName, subscriptionId" /> | Adds the access policy assignment to the specified users |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyAssignmentName, cacheName, resourceGroupName, subscriptionId" /> | Deletes the access policy assignment from a redis cache |

## `SELECT` examples

Gets the list of access policy assignments associated with this redis cache

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
cacheName,
object_id,
object_id_alias,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure_isv.redis.vw_access_policy_assignments
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.redis.access_policy_assignments
WHERE cacheName = '{{ cacheName }}'
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
INSERT INTO azure_isv.redis.access_policy_assignments (
accessPolicyAssignmentName,
cacheName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accessPolicyAssignmentName }}',
'{{ cacheName }}',
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
          value: string
        - name: objectId
          value: string
        - name: objectIdAlias
          value: string
        - name: accessPolicyName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>access_policy_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis.access_policy_assignments
WHERE accessPolicyAssignmentName = '{{ accessPolicyAssignmentName }}'
AND cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
