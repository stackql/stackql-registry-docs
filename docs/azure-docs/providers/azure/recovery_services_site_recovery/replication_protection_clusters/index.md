---
title: replication_protection_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_clusters
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

Creates, updates, deletes, gets or lists a <code>replication_protection_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_protection_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_clusters', value: 'view', },
        { label: 'replication_protection_clusters', value: 'resource', },
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR replication protection cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected clusters in the vault. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protected clusters in the protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an ASR replication protection cluster item. |
| <CopyableCode code="apply_recovery_point" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to apply a new cluster recovery point on the Protection cluster. |
| <CopyableCode code="failover_commit" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | Operation to initiate commit failover of the replication protection cluster. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge the replication protection cluster. This operation will force delete the replication protection cluster. Use the remove operation on replication protection cluster to perform a clean disable replication protection cluster. |
| <CopyableCode code="repair_replication" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId" /> | The operation to repair replication protection cluster. |
| <CopyableCode code="test_failover" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to initiate a failover of the replication protection cluster. |
| <CopyableCode code="test_failover_cleanup" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to clean up the test failover of a replication protected cluster. |
| <CopyableCode code="unplanned_failover" /> | `EXEC` | <CopyableCode code="fabricName, protectionContainerName, replicationProtectionClusterName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Operation to initiate a failover of the replication protection cluster. |

## `SELECT` examples

Gets the list of ASR replication protected clusters in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_protection_clusters', value: 'view', },
        { label: 'replication_protection_clusters', value: 'resource', },
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
FROM azure.recovery_services_site_recovery.vw_replication_protection_clusters
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
FROM azure.recovery_services_site_recovery.replication_protection_clusters
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_protection_clusters</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_protection_clusters (
fabricName,
protectionContainerName,
replicationProtectionClusterName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ fabricName }}',
'{{ protectionContainerName }}',
'{{ replicationProtectionClusterName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: protectionClusterType
          value: string
        - name: primaryFabricFriendlyName
          value: string
        - name: primaryFabricProvider
          value: string
        - name: recoveryFabricFriendlyName
          value: string
        - name: recoveryFabricId
          value: string
        - name: primaryProtectionContainerFriendlyName
          value: string
        - name: recoveryProtectionContainerFriendlyName
          value: string
        - name: protectionState
          value: string
        - name: protectionStateDescription
          value: string
        - name: activeLocation
          value: string
        - name: testFailoverState
          value: string
        - name: testFailoverStateDescription
          value: string
        - name: allowedOperations
          value:
            - string
        - name: replicationHealth
          value: string
        - name: healthErrors
          value:
            - - name: innerHealthErrors
                value:
                  - - name: errorSource
                      value: string
                    - name: errorType
                      value: string
                    - name: errorLevel
                      value: string
                    - name: errorCategory
                      value: string
                    - name: errorCode
                      value: string
                    - name: summaryMessage
                      value: string
                    - name: errorMessage
                      value: string
                    - name: possibleCauses
                      value: string
                    - name: recommendedAction
                      value: string
                    - name: creationTimeUtc
                      value: string
                    - name: recoveryProviderErrorMessage
                      value: string
                    - name: entityId
                      value: string
                    - name: errorId
                      value: string
                    - name: customerResolvability
                      value: string
              - name: errorSource
                value: string
              - name: errorType
                value: string
              - name: errorLevel
                value: string
              - name: errorCategory
                value: string
              - name: errorCode
                value: string
              - name: summaryMessage
                value: string
              - name: errorMessage
                value: string
              - name: possibleCauses
                value: string
              - name: recommendedAction
                value: string
              - name: creationTimeUtc
                value: string
              - name: recoveryProviderErrorMessage
                value: string
              - name: entityId
                value: string
              - name: errorId
                value: string
              - name: customerResolvability
                value: string
        - name: lastSuccessfulFailoverTime
          value: string
        - name: lastSuccessfulTestFailoverTime
          value: string
        - name: policyFriendlyName
          value: string
        - name: currentScenario
          value:
            - name: scenarioName
              value: string
            - name: jobId
              value: string
            - name: startTime
              value: string
        - name: recoveryContainerId
          value: string
        - name: agentClusterId
          value: string
        - name: clusterFqdn
          value: string
        - name: clusterNodeFqdns
          value:
            - string
        - name: clusterProtectedItemIds
          value:
            - string
        - name: provisioningState
          value: string
        - name: areAllClusterNodesRegistered
          value: boolean
        - name: clusterRegisteredNodes
          value:
            - - name: clusterNodeFqdn
                value: string
              - name: machineId
                value: string
              - name: biosId
                value: string
              - name: isSharedDiskVirtualNode
                value: boolean
        - name: providerSpecificDetails
          value:
            - name: instanceType
              value: string
        - name: sharedDiskProperties
          value:
            - name: protectionState
              value: string
            - name: testFailoverState
              value: string
            - name: activeLocation
              value: string
            - name: allowedOperations
              value:
                - string
            - name: replicationHealth
              value: string
            - name: healthErrors
              value:
                - - name: innerHealthErrors
                    value:
                      - - name: errorSource
                          value: string
                        - name: errorType
                          value: string
                        - name: errorLevel
                          value: string
                        - name: errorCategory
                          value: string
                        - name: errorCode
                          value: string
                        - name: summaryMessage
                          value: string
                        - name: errorMessage
                          value: string
                        - name: possibleCauses
                          value: string
                        - name: recommendedAction
                          value: string
                        - name: creationTimeUtc
                          value: string
                        - name: recoveryProviderErrorMessage
                          value: string
                        - name: entityId
                          value: string
                        - name: errorId
                          value: string
                        - name: customerResolvability
                          value: string
                  - name: errorSource
                    value: string
                  - name: errorType
                    value: string
                  - name: errorLevel
                    value: string
                  - name: errorCategory
                    value: string
                  - name: errorCode
                    value: string
                  - name: summaryMessage
                    value: string
                  - name: errorMessage
                    value: string
                  - name: possibleCauses
                    value: string
                  - name: recommendedAction
                    value: string
                  - name: creationTimeUtc
                    value: string
                  - name: recoveryProviderErrorMessage
                    value: string
                  - name: entityId
                    value: string
                  - name: errorId
                    value: string
                  - name: customerResolvability
                    value: string
            - name: sharedDiskProviderSpecificDetails
              value:
                - name: instanceType
                  value: string
        - name: policyId
          value: string

```
</TabItem>
</Tabs>
