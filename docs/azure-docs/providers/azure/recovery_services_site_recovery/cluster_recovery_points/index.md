---
title: cluster_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_recovery_points
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>cluster_recovery_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.cluster_recovery_points" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_recovery_points', value: 'view', },
        { label: 'cluster_recovery_points', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The recovery point Id. |
| <CopyableCode code="name" /> | `text` | The name of the recovery point. |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoveryPointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_point_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_point_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicationProtectionClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The recovery point Id. |
| <CopyableCode code="name" /> | `string` | The name of the recovery point. |
| <CopyableCode code="properties" /> | `object` | Cluster recovery point properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, recoveryPointName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | Get the details of specified recovery point. |
| <CopyableCode code="list_by_replication_protection_cluster" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The list of cluster recovery points. |

## `SELECT` examples

The list of cluster recovery points.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_recovery_points', value: 'view', },
        { label: 'cluster_recovery_points', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
protectionContainerName,
provider_specific_details,
recoveryPointName,
recovery_point_time,
recovery_point_type,
replicationProtectionClusterName,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_cluster_recovery_points
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicationProtectionClusterName = '{{ replicationProtectionClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.recovery_services_site_recovery.cluster_recovery_points
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicationProtectionClusterName = '{{ replicationProtectionClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

