---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - nexus
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aggregator_or_single_rack_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="analytics_workspace_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_upgrade_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_manager_connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_manager_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_service_principal" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="command_output_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_deployment_threshold" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_rack_definitions" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="manual_action_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtime_protection_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_archive" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_expiry_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="update_strategy" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_resource_ids" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get properties of the provided cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of clusters in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of clusters in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new cluster or update the properties of the cluster if it exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete the provided cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Patch the properties of the provided cluster, or update the tags associated with the cluster. Properties and tag updates can be done independently. |
| <CopyableCode code="continue_update_version" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Trigger the continuation of an update for a cluster with a matching update strategy that has paused after completing a segment of the update. |
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deploy the cluster using the rack configuration provided during creation. |
| <CopyableCode code="scan_runtime" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Triggers the execution of a runtime protection scan to detect and remediate detected issues, in accordance with the cluster configuration. |

## `SELECT` examples

Get a list of clusters in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aggregator_or_single_rack_definition,
analytics_workspace_id,
available_upgrade_versions,
clusterName,
cluster_capacity,
cluster_connection_status,
cluster_extended_location,
cluster_location,
cluster_manager_connection_status,
cluster_manager_id,
cluster_service_principal,
cluster_type,
cluster_version,
command_output_settings,
compute_deployment_threshold,
compute_rack_definitions,
detailed_status,
detailed_status_message,
extended_location,
hybrid_aks_extended_location,
identity,
location,
managed_resource_group_configuration,
manual_action_count,
network_fabric_id,
provisioning_state,
resourceGroupName,
runtime_protection_configuration,
secret_archive,
subscriptionId,
support_expiry_date,
tags,
update_strategy,
workload_resource_ids
FROM azure.nexus.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
identity,
location,
properties,
tags
FROM azure.nexus.clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO azure.nexus.clusters (
clusterName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
identity,
properties,
tags,
location
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
'{{ identity }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: aggregatorOrSingleRackDefinition
          value:
            - name: availabilityZone
              value: string
            - name: bareMetalMachineConfigurationData
              value:
                - - name: bmcConnectionString
                    value: string
                  - name: bmcCredentials
                    value:
                      - name: password
                        value: string
                      - name: username
                        value: string
                  - name: bmcMacAddress
                    value: string
                  - name: bootMacAddress
                    value: string
                  - name: machineDetails
                    value: string
                  - name: machineName
                    value: string
                  - name: rackSlot
                    value: integer
                  - name: serialNumber
                    value: string
            - name: networkRackId
              value: string
            - name: rackLocation
              value: string
            - name: rackSerialNumber
              value: string
            - name: rackSkuId
              value: string
            - name: storageApplianceConfigurationData
              value:
                - - name: rackSlot
                    value: integer
                  - name: serialNumber
                    value: string
                  - name: storageApplianceName
                    value: string
        - name: analyticsWorkspaceId
          value: string
        - name: availableUpgradeVersions
          value:
            - - name: controlImpact
                value: string
              - name: expectedDuration
                value: string
              - name: impactDescription
                value: string
              - name: supportExpiryDate
                value: string
              - name: targetClusterVersion
                value: string
              - name: workloadImpact
                value: string
        - name: clusterCapacity
          value:
            - name: availableApplianceStorageGB
              value: integer
            - name: availableCoreCount
              value: integer
            - name: availableHostStorageGB
              value: integer
            - name: availableMemoryGB
              value: integer
            - name: totalApplianceStorageGB
              value: integer
            - name: totalCoreCount
              value: integer
            - name: totalHostStorageGB
              value: integer
            - name: totalMemoryGB
              value: integer
        - name: clusterConnectionStatus
          value: string
        - name: clusterLocation
          value: string
        - name: clusterManagerConnectionStatus
          value: string
        - name: clusterManagerId
          value: string
        - name: clusterServicePrincipal
          value:
            - name: applicationId
              value: string
            - name: password
              value: string
            - name: principalId
              value: string
            - name: tenantId
              value: string
        - name: clusterType
          value: string
        - name: clusterVersion
          value: string
        - name: commandOutputSettings
          value:
            - name: associatedIdentity
              value:
                - name: identityType
                  value: string
                - name: userAssignedIdentityResourceId
                  value: string
            - name: containerUrl
              value: string
        - name: computeDeploymentThreshold
          value:
            - name: grouping
              value: string
            - name: type
              value: string
            - name: value
              value: integer
        - name: computeRackDefinitions
          value:
            - - name: availabilityZone
                value: string
              - name: bareMetalMachineConfigurationData
                value:
                  - - name: bmcConnectionString
                      value: string
                    - name: bmcMacAddress
                      value: string
                    - name: bootMacAddress
                      value: string
                    - name: machineDetails
                      value: string
                    - name: machineName
                      value: string
                    - name: rackSlot
                      value: integer
                    - name: serialNumber
                      value: string
              - name: networkRackId
                value: string
              - name: rackLocation
                value: string
              - name: rackSerialNumber
                value: string
              - name: rackSkuId
                value: string
              - name: storageApplianceConfigurationData
                value:
                  - - name: rackSlot
                      value: integer
                    - name: serialNumber
                      value: string
                    - name: storageApplianceName
                      value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: managedResourceGroupConfiguration
          value:
            - name: location
              value: string
            - name: name
              value: string
        - name: manualActionCount
          value: integer
        - name: networkFabricId
          value: string
        - name: provisioningState
          value: string
        - name: runtimeProtectionConfiguration
          value:
            - name: enforcementLevel
              value: string
        - name: secretArchive
          value:
            - name: keyVaultId
              value: string
            - name: useKeyVault
              value: string
        - name: supportExpiryDate
          value: string
        - name: updateStrategy
          value:
            - name: maxUnavailable
              value: integer
            - name: strategyType
              value: string
            - name: thresholdType
              value: string
            - name: thresholdValue
              value: integer
            - name: waitTimeMinutes
              value: integer
        - name: workloadResourceIds
          value:
            - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.clusters
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
