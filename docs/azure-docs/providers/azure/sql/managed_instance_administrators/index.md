---
title: managed_instance_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_administrators
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_administrators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_administrators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_administrators', value: 'view', },
        { label: 'managed_instance_administrators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administratorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="login" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a managed instance administrator. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="administratorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance administrator. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="administratorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates or updates a managed instance administrator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="administratorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a managed instance administrator. |

## `SELECT` examples

Gets a managed instance administrator.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_administrators', value: 'view', },
        { label: 'managed_instance_administrators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administratorName,
administrator_type,
login,
managedInstanceName,
resourceGroupName,
sid,
subscriptionId,
tenant_id
FROM azure.sql.vw_managed_instance_administrators
WHERE administratorName = '{{ administratorName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_instance_administrators
WHERE administratorName = '{{ administratorName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_administrators</code> resource.

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
INSERT INTO azure.sql.managed_instance_administrators (
administratorName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ administratorName }}',
'{{ managedInstanceName }}',
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
        - name: administratorType
          value: string
        - name: login
          value: string
        - name: sid
          value: string
        - name: tenantId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_instance_administrators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.managed_instance_administrators
WHERE administratorName = '{{ administratorName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
