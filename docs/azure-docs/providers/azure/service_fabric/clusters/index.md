---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - service_fabric
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.clusters" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Azure resource identifier. |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="add_on_features" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type_versions_cleanup_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_cluster_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_active_directory" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate_common_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_certificate_common_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_certificate_thumbprints" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_code_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics_storage_account_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Azure resource etag. |
| <CopyableCode code="event_store_service_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_service_manager" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure resource location. |
| <CopyableCode code="management_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="notifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reliability_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="reverse_proxy_certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="reverse_proxy_certificate_common_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="sf_zonal_upgrade_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
| <CopyableCode code="upgrade_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_pause_end_timestamp_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_pause_start_timestamp_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_wave" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmss_zonal_upgrade_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="wave_upgrade_paused" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="location" /> | `string` | Azure resource location. |
| <CopyableCode code="properties" /> | `object` | Describes the cluster resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric cluster resource created or in the process of being created in the specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric cluster resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric cluster resource with the specified name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Update the configuration of a Service Fabric cluster resource with the specified name. |

## `SELECT` examples

Gets all Service Fabric cluster resources created or in the process of being created in the subscription.

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
id,
name,
add_on_features,
application_type_versions_cleanup_policy,
available_cluster_versions,
azure_active_directory,
certificate,
certificate_common_names,
client_certificate_common_names,
client_certificate_thumbprints,
clusterName,
cluster_code_version,
cluster_endpoint,
cluster_id,
cluster_state,
diagnostics_storage_account_config,
etag,
event_store_service_enabled,
fabric_settings,
infrastructure_service_manager,
location,
management_endpoint,
node_types,
notifications,
provisioning_state,
reliability_level,
resourceGroupName,
reverse_proxy_certificate,
reverse_proxy_certificate_common_names,
sf_zonal_upgrade_mode,
subscriptionId,
system_data,
tags,
type,
upgrade_description,
upgrade_mode,
upgrade_pause_end_timestamp_utc,
upgrade_pause_start_timestamp_utc,
upgrade_wave,
vm_image,
vmss_zonal_upgrade_mode,
wave_upgrade_paused
FROM azure.service_fabric.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.service_fabric.clusters
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
INSERT INTO azure.service_fabric.clusters (
clusterName,
resourceGroupName,
subscriptionId,
location,
tags,
systemData,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ systemData }}',
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
    - name: etag
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: addOnFeatures
          value:
            - []
        - name: availableClusterVersions
          value:
            - - name: codeVersion
                value: string
              - name: supportExpiryUtc
                value: string
              - name: environment
                value: []
        - name: azureActiveDirectory
          value:
            - name: tenantId
              value: string
            - name: clusterApplication
              value: string
            - name: clientApplication
              value: string
        - name: certificate
          value:
            - name: thumbprint
              value: string
            - name: thumbprintSecondary
              value: string
            - name: x509StoreName
              value: []
        - name: certificateCommonNames
          value:
            - name: commonNames
              value:
                - - name: certificateCommonName
                    value: string
                  - name: certificateIssuerThumbprint
                    value: string
        - name: clientCertificateCommonNames
          value:
            - - name: isAdmin
                value: boolean
              - name: certificateCommonName
                value: string
              - name: certificateIssuerThumbprint
                value: string
        - name: clientCertificateThumbprints
          value:
            - - name: isAdmin
                value: boolean
              - name: certificateThumbprint
                value: string
        - name: clusterCodeVersion
          value: string
        - name: clusterEndpoint
          value: string
        - name: clusterId
          value: string
        - name: clusterState
          value: []
        - name: diagnosticsStorageAccountConfig
          value:
            - name: storageAccountName
              value: string
            - name: protectedAccountKeyName
              value: string
            - name: protectedAccountKeyName2
              value: string
            - name: blobEndpoint
              value: string
            - name: queueEndpoint
              value: string
            - name: tableEndpoint
              value: string
        - name: eventStoreServiceEnabled
          value: boolean
        - name: fabricSettings
          value:
            - - name: name
                value: string
              - name: parameters
                value:
                  - - name: name
                      value: string
                    - name: value
                      value: string
        - name: managementEndpoint
          value: string
        - name: nodeTypes
          value:
            - - name: name
                value: string
              - name: placementProperties
                value: object
              - name: capacities
                value: object
              - name: clientConnectionEndpointPort
                value: integer
              - name: httpGatewayEndpointPort
                value: integer
              - name: durabilityLevel
                value: []
              - name: applicationPorts
                value:
                  - name: startPort
                    value: integer
                  - name: endPort
                    value: integer
              - name: isPrimary
                value: boolean
              - name: vmInstanceCount
                value: integer
              - name: reverseProxyEndpointPort
                value: integer
              - name: isStateless
                value: boolean
              - name: multipleAvailabilityZones
                value: boolean
        - name: provisioningState
          value: string
        - name: reliabilityLevel
          value: []
        - name: upgradeDescription
          value:
            - name: forceRestart
              value: boolean
            - name: upgradeReplicaSetCheckTimeout
              value: string
            - name: healthCheckWaitDuration
              value: string
            - name: healthCheckStableDuration
              value: string
            - name: healthCheckRetryTimeout
              value: string
            - name: upgradeTimeout
              value: string
            - name: upgradeDomainTimeout
              value: string
            - name: healthPolicy
              value:
                - name: maxPercentUnhealthyNodes
                  value: integer
                - name: maxPercentUnhealthyApplications
                  value: integer
                - name: applicationHealthPolicies
                  value: []
            - name: deltaHealthPolicy
              value:
                - name: maxPercentDeltaUnhealthyNodes
                  value: integer
                - name: maxPercentUpgradeDomainDeltaUnhealthyNodes
                  value: integer
                - name: maxPercentDeltaUnhealthyApplications
                  value: integer
                - name: applicationDeltaHealthPolicies
                  value: []
        - name: upgradeMode
          value: []
        - name: applicationTypeVersionsCleanupPolicy
          value:
            - name: maxUnusedVersionsToKeep
              value: integer
        - name: vmImage
          value: string
        - name: sfZonalUpgradeMode
          value: []
        - name: vmssZonalUpgradeMode
          value: []
        - name: infrastructureServiceManager
          value: boolean
        - name: upgradeWave
          value: []
        - name: upgradePauseStartTimestampUtc
          value: string
        - name: upgradePauseEndTimestampUtc
          value: string
        - name: waveUpgradePaused
          value: boolean
        - name: notifications
          value:
            - - name: isEnabled
                value: boolean
              - name: notificationCategory
                value: string
              - name: notificationLevel
                value: string
              - name: notificationTargets
                value:
                  - - name: notificationChannel
                      value: string
                    - name: receivers
                      value:
                        - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure.service_fabric.clusters
SET 
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
DELETE FROM azure.service_fabric.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
