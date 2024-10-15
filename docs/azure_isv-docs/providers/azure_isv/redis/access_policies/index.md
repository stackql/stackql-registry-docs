---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
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

Creates, updates, deletes, gets or lists a <code>access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.access_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policies', value: 'view', },
        { label: 'access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cacheName" /> | `text` | field from the `properties` object |
| <CopyableCode code="permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | All properties of an access policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyName, cacheName, resourceGroupName, subscriptionId" /> | Gets the detailed information about an access policy of a redis cache |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Gets the list of access policies associated with this redis cache |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accessPolicyName, cacheName, resourceGroupName, subscriptionId" /> | Adds an access policy to the redis cache |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyName, cacheName, resourceGroupName, subscriptionId" /> | Deletes the access policy from a redis cache |

## `SELECT` examples

Gets the list of access policies associated with this redis cache

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_access_policies', value: 'view', },
        { label: 'access_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accessPolicyName,
cacheName,
permissions,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure_isv.redis.vw_access_policies
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.redis.access_policies
WHERE cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_policies</code> resource.

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
INSERT INTO azure_isv.redis.access_policies (
accessPolicyName,
cacheName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accessPolicyName }}',
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
        - name: type
          value: string
        - name: permissions
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>access_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.redis.access_policies
WHERE accessPolicyName = '{{ accessPolicyName }}'
AND cacheName = '{{ cacheName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
