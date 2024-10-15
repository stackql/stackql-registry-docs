---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - postgresql_hsc
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

Creates, updates, deletes, gets or lists a <code>roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.roles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_roles', value: 'view', },
        { label: 'roles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a cluster role. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, roleName, subscriptionId" /> | Gets information about a cluster role. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all the roles in a given cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, roleName, subscriptionId, data__properties" /> | Creates a new role or updates an existing role. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, roleName, subscriptionId" /> | Deletes a cluster role. |

## `SELECT` examples

List all the roles in a given cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_roles', value: 'view', },
        { label: 'roles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
external_identity,
password,
provisioning_state,
resourceGroupName,
roleName,
role_type,
subscriptionId
FROM azure.postgresql_hsc.vw_roles
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql_hsc.roles
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>roles</code> resource.

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
INSERT INTO azure.postgresql_hsc.roles (
clusterName,
resourceGroupName,
roleName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ roleName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: roleType
          value: string
        - name: password
          value: string
        - name: externalIdentity
          value:
            - name: objectId
              value: string
            - name: principalType
              value: string
            - name: tenantId
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>roles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.postgresql_hsc.roles
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleName = '{{ roleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
