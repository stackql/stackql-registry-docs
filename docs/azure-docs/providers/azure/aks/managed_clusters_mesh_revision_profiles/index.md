---
title: managed_clusters_mesh_revision_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_mesh_revision_profiles
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

Creates, updates, deletes, gets or lists a <code>managed_clusters_mesh_revision_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters_mesh_revision_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.managed_clusters_mesh_revision_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters_mesh_revision_profiles', value: 'view', },
        { label: 'managed_clusters_mesh_revision_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="mesh_revisions" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Mesh revision profile properties for a mesh |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, mode, subscriptionId" /> | Contains extra metadata on the revision, including supported revisions, cluster compatibility and available upgrades |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Contains extra metadata on each revision, including supported revisions, cluster compatibility and available upgrades |

## `SELECT` examples

Contains extra metadata on each revision, including supported revisions, cluster compatibility and available upgrades

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters_mesh_revision_profiles', value: 'view', },
        { label: 'managed_clusters_mesh_revision_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
mesh_revisions,
mode,
subscriptionId
FROM azure.aks.vw_managed_clusters_mesh_revision_profiles
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.aks.managed_clusters_mesh_revision_profiles
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

