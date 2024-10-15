---
title: provisioned_cluster_instances_upgrade_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_cluster_instances_upgrade_profiles
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>provisioned_cluster_instances_upgrade_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioned_cluster_instances_upgrade_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.provisioned_cluster_instances_upgrade_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provisioned_cluster_instances_upgrade_profiles', value: 'view', },
        { label: 'provisioned_cluster_instances_upgrade_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectedClusterResourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="control_plane_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Control plane and agent pool upgrade profiles. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Gets the upgrade profile of a provisioned cluster |

## `SELECT` examples

Gets the upgrade profile of a provisioned cluster

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provisioned_cluster_instances_upgrade_profiles', value: 'view', },
        { label: 'provisioned_cluster_instances_upgrade_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connectedClusterResourceUri,
control_plane_profile,
provisioning_state
FROM azure.hybrid_aks.vw_provisioned_cluster_instances_upgrade_profiles
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.hybrid_aks.provisioned_cluster_instances_upgrade_profiles
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem></Tabs>

