---
title: infra_role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - infra_role_instances
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>infra_role_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infra_role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.infra_role_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_infra_role_instances', value: 'view', },
        { label: 'infra_role_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="infraRoleInstance" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit_node" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | All properties of an infrastructure role instance. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Return the requested infrastructure role instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all infrastructure role instances at a location. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Power off an infrastructure role instance. |
| <CopyableCode code="power_on" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Power on an infrastructure role instance. |
| <CopyableCode code="reboot" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Reboot an infrastructure role instance. |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="infraRoleInstance, location, resourceGroupName, subscriptionId" /> | Shut down an infrastructure role instance. |

## `SELECT` examples

Returns a list of all infrastructure role instances at a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_infra_role_instances', value: 'view', },
        { label: 'infra_role_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
infraRoleInstance,
location,
resourceGroupName,
scale_unit,
scale_unit_node,
size,
state,
subscriptionId,
tags,
type
FROM azure_stack.fabric_admin.vw_infra_role_instances
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure_stack.fabric_admin.infra_role_instances
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

