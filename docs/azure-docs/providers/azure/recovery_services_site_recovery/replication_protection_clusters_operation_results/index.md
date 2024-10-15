---
title: replication_protection_clusters_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_clusters_operation_results
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

Creates, updates, deletes, gets or lists a <code>replication_protection_clusters_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protection_clusters_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_clusters_operation_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_clusters_operation_results', value: 'view', },
        { label: 'replication_protection_clusters_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The protection cluster Id. |
| <CopyableCode code="name" /> | `text` | The name of the protection cluster. |
| <CopyableCode code="active_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="are_all_cluster_nodes_registered" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_node_fqdns" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_protected_item_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_registered_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_scenario" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobId" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_test_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_fabric_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_protection_container_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_cluster_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_protection_container_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicationProtectionClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_disk_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_failover_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_failover_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The protection cluster Id. |
| <CopyableCode code="name" /> | `string` | The name of the protection cluster. |
| <CopyableCode code="properties" /> | `object` | Replication protection cluster custom data details. |
| <CopyableCode code="type" /> | `string` | The Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, jobId, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | Track the results of an asynchronous operation on the replication protection cluster. |

## `SELECT` examples

Track the results of an asynchronous operation on the replication protection cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_clusters_operation_results', value: 'view', },
        { label: 'replication_protection_clusters_operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
active_location,
agent_cluster_id,
allowed_operations,
are_all_cluster_nodes_registered,
cluster_fqdn,
cluster_node_fqdns,
cluster_protected_item_ids,
cluster_registered_nodes,
current_scenario,
fabricName,
health_errors,
jobId,
last_successful_failover_time,
last_successful_test_failover_time,
policy_friendly_name,
policy_id,
primary_fabric_friendly_name,
primary_fabric_provider,
primary_protection_container_friendly_name,
protectionContainerName,
protection_cluster_type,
protection_state,
protection_state_description,
provider_specific_details,
provisioning_state,
recovery_container_id,
recovery_fabric_friendly_name,
recovery_fabric_id,
recovery_protection_container_friendly_name,
replicationProtectionClusterName,
replication_health,
resourceGroupName,
resourceName,
shared_disk_properties,
subscriptionId,
test_failover_state,
test_failover_state_description,
type
FROM azure.recovery_services_site_recovery.vw_replication_protection_clusters_operation_results
WHERE fabricName = '{{ fabricName }}'
AND jobId = '{{ jobId }}'
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
FROM azure.recovery_services_site_recovery.replication_protection_clusters_operation_results
WHERE fabricName = '{{ fabricName }}'
AND jobId = '{{ jobId }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicationProtectionClusterName = '{{ replicationProtectionClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

