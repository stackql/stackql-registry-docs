---
title: registries_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - registries_private_link_resources
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>registries_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.registries_private_link_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registries_private_link_resources', value: 'view', },
        { label: 'registries_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_members" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_zone_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type is private link resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a private link resource. |
| <CopyableCode code="type" /> | `string` | The resource type is private link resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, registryName, resourceGroupName, subscriptionId" /> | Gets a private link resource by a specified group name for a container registry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists the private link resources for a container registry. |

## `SELECT` examples

Lists the private link resources for a container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registries_private_link_resources', value: 'view', },
        { label: 'registries_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
groupName,
group_id,
registryName,
required_members,
required_zone_names,
resourceGroupName,
subscriptionId,
type
FROM azure.container_registry.vw_registries_private_link_resources
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.container_registry.registries_private_link_resources
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

