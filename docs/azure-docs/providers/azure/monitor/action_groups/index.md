---
title: action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups
  - monitor
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

Creates, updates, deletes, gets or lists a <code>action_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_groups', value: 'view', },
        { label: 'action_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource Id. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="actionGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="action_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="webhook_properties" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="properties" /> | `object` | A pointer to an Azure Action Group. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Get an action group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of all action groups in a resource group. |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all action groups in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Create a new action group or update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Delete an action group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Updates an existing action group's tags. To update other fields use the CreateOrUpdate method. |
| <CopyableCode code="enable_receiver" /> | `EXEC` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId, data__receiverName" /> | Enable a receiver in an action group. This changes the receiver's status from Disabled to Enabled. This operation is only supported for Email or SMS receivers. |
| <CopyableCode code="reconcile_nsp" /> | `EXEC` | <CopyableCode code="actionGroupName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Reconciles a specified NSP configuration for specified action group. |

## `SELECT` examples

Get a list of all action groups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_groups', value: 'view', },
        { label: 'action_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
actionGroupName,
action_group_id,
location,
resourceGroupName,
subscriptionId,
tags,
type,
webhook_properties
FROM azure.monitor.vw_action_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.monitor.action_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>action_groups</code> resource.

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
INSERT INTO azure.monitor.action_groups (
actionGroupName,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ actionGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: actionGroupId
          value: string
        - name: webhookProperties
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>action_groups</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.action_groups
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
actionGroupName = '{{ actionGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>action_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.action_groups
WHERE actionGroupName = '{{ actionGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
