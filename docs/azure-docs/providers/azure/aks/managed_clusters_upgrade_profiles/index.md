---
title: managed_clusters_upgrade_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_upgrade_profiles
  - aks
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

Creates, updates, deletes, gets or lists a <code>managed_clusters_upgrade_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters_upgrade_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.managed_clusters_upgrade_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters_upgrade_profiles', value: 'view', },
        { label: 'managed_clusters_upgrade_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the upgrade profile. |
| <CopyableCode code="name" /> | `text` | The name of the upgrade profile. |
| <CopyableCode code="agent_pool_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="control_plane_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the upgrade profile. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the upgrade profile. |
| <CopyableCode code="name" /> | `string` | The name of the upgrade profile. |
| <CopyableCode code="properties" /> | `object` | Control plane and agent pool upgrade profiles. |
| <CopyableCode code="type" /> | `string` | The type of the upgrade profile. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters_upgrade_profiles', value: 'view', },
        { label: 'managed_clusters_upgrade_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agent_pool_profiles,
control_plane_profile,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.aks.vw_managed_clusters_upgrade_profiles
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
FROM azure.aks.managed_clusters_upgrade_profiles
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

