---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>managed_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.managed_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters', value: 'view', },
        { label: 'managed_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource identifier. |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="addon_features" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin_user_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_rdp_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type_versions_cleanup_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_generated_domain_name_label_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="auxiliary_subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_active_directory" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_connection_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="clients" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_certificate_thumbprints" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_code_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_upgrade_cadence" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_upgrade_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="ddos_protection_plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_auto_os_upgrade" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_http_gateway_exclusive_auth_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ipv6" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_service_public_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Azure resource etag. |
| <CopyableCode code="fabric_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_gateway_connection_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_gateway_token_auth_connection_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv4_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure resource location. |
| <CopyableCode code="network_security_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_prefix_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ipv6_prefix_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Service Fabric managed cluster Sku definition |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
| <CopyableCode code="upgrade_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_custom_vnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="zonal_resiliency" /> | `text` | field from the `properties` object |
| <CopyableCode code="zonal_update_mode" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="location" /> | `string` | Azure resource location. |
| <CopyableCode code="properties" /> | `object` | Describes the managed cluster resource properties. |
| <CopyableCode code="sku" /> | `object` | Service Fabric managed cluster Sku definition |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric managed cluster resource created or in the process of being created in the specified resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__sku" /> | Create or update a Service Fabric managed cluster resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric managed cluster resource with the specified name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Update the tags of of a Service Fabric managed cluster resource with the specified name. |
| <CopyableCode code="apply_maintenance_window" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Action to Apply Maintenance window on the Service Fabric Managed Clusters, right now. Any pending update will be applied. |

## `SELECT` examples

Gets all Service Fabric cluster resources created or in the process of being created in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters', value: 'view', },
        { label: 'managed_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
addon_features,
admin_password,
admin_user_name,
allow_rdp_access,
application_type_versions_cleanup_policy,
auto_generated_domain_name_label_scope,
auxiliary_subnets,
azure_active_directory,
client_connection_port,
clients,
clusterName,
cluster_certificate_thumbprints,
cluster_code_version,
cluster_id,
cluster_state,
cluster_upgrade_cadence,
cluster_upgrade_mode,
custom_fqdn,
ddos_protection_plan_id,
dns_name,
enable_auto_os_upgrade,
enable_http_gateway_exclusive_auth_mode,
enable_ipv6,
enable_service_public_ip,
etag,
fabric_settings,
fqdn,
http_gateway_connection_port,
http_gateway_token_auth_connection_port,
ip_tags,
ipv4_address,
ipv6_address,
load_balancing_rules,
location,
network_security_rules,
provisioning_state,
public_ip_prefix_id,
public_ipv6_prefix_id,
resourceGroupName,
service_endpoints,
sku,
subnet_id,
subscriptionId,
system_data,
tags,
type,
upgrade_description,
use_custom_vnet,
zonal_resiliency,
zonal_update_mode
FROM azure.service_fabric_managed_clusters.vw_managed_clusters
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
sku,
systemData,
tags,
type
FROM azure.service_fabric_managed_clusters.managed_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_clusters</code> resource.

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
INSERT INTO azure.service_fabric_managed_clusters.managed_clusters (
clusterName,
resourceGroupName,
subscriptionId,
data__sku,
location,
tags,
systemData,
properties,
sku
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ location }}',
'{{ tags }}',
'{{ systemData }}',
'{{ properties }}',
'{{ sku }}'
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
        - name: dnsName
          value: string
        - name: fqdn
          value: string
        - name: ipv4Address
          value: string
        - name: clusterId
          value: string
        - name: clusterState
          value: []
        - name: clusterCertificateThumbprints
          value:
            - string
        - name: clientConnectionPort
          value: integer
        - name: httpGatewayConnectionPort
          value: integer
        - name: adminUserName
          value: string
        - name: adminPassword
          value: string
        - name: loadBalancingRules
          value:
            - - name: frontendPort
                value: integer
              - name: backendPort
                value: integer
              - name: protocol
                value: string
              - name: probePort
                value: integer
              - name: probeProtocol
                value: string
              - name: probeRequestPath
                value: string
              - name: loadDistribution
                value: string
        - name: allowRdpAccess
          value: boolean
        - name: networkSecurityRules
          value:
            - - name: name
                value: string
              - name: description
                value: string
              - name: protocol
                value: string
              - name: sourceAddressPrefixes
                value:
                  - string
              - name: destinationAddressPrefixes
                value:
                  - string
              - name: sourcePortRanges
                value:
                  - string
              - name: destinationPortRanges
                value:
                  - string
              - name: sourceAddressPrefix
                value: string
              - name: destinationAddressPrefix
                value: string
              - name: sourcePortRange
                value: string
              - name: destinationPortRange
                value: string
              - name: access
                value: string
              - name: priority
                value: integer
              - name: direction
                value: string
        - name: clients
          value:
            - - name: isAdmin
                value: boolean
              - name: thumbprint
                value: string
              - name: commonName
                value: string
              - name: issuerThumbprint
                value: string
        - name: azureActiveDirectory
          value:
            - name: tenantId
              value: string
            - name: clusterApplication
              value: string
            - name: clientApplication
              value: string
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
        - name: provisioningState
          value: []
        - name: clusterCodeVersion
          value: string
        - name: clusterUpgradeMode
          value: []
        - name: clusterUpgradeCadence
          value: []
        - name: addonFeatures
          value:
            - []
        - name: enableAutoOSUpgrade
          value: boolean
        - name: zonalResiliency
          value: boolean
        - name: applicationTypeVersionsCleanupPolicy
          value:
            - name: maxUnusedVersionsToKeep
              value: integer
        - name: enableIpv6
          value: boolean
        - name: subnetId
          value: string
        - name: ipTags
          value:
            - - name: ipTagType
                value: string
              - name: tag
                value: string
        - name: ipv6Address
          value: string
        - name: enableServicePublicIP
          value: boolean
        - name: auxiliarySubnets
          value:
            - - name: name
                value: string
              - name: enableIpv6
                value: boolean
              - name: privateEndpointNetworkPolicies
                value: string
              - name: privateLinkServiceNetworkPolicies
                value: string
              - name: networkSecurityGroupId
                value: string
        - name: serviceEndpoints
          value:
            - - name: service
                value: string
              - name: locations
                value:
                  - string
        - name: zonalUpdateMode
          value: []
        - name: useCustomVnet
          value: boolean
        - name: publicIPPrefixId
          value: string
        - name: publicIPv6PrefixId
          value: string
        - name: ddosProtectionPlanId
          value: string
        - name: upgradeDescription
          value:
            - name: forceRestart
              value: boolean
            - name: healthPolicy
              value:
                - name: maxPercentUnhealthyNodes
                  value: integer
                - name: maxPercentUnhealthyApplications
                  value: integer
            - name: deltaHealthPolicy
              value:
                - name: maxPercentDeltaUnhealthyNodes
                  value: integer
                - name: maxPercentUpgradeDomainDeltaUnhealthyNodes
                  value: integer
                - name: maxPercentDeltaUnhealthyApplications
                  value: integer
            - name: monitoringPolicy
              value:
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
            - name: upgradeReplicaSetCheckTimeout
              value: string
        - name: httpGatewayTokenAuthConnectionPort
          value: integer
        - name: enableHttpGatewayExclusiveAuthMode
          value: boolean
        - name: autoGeneratedDomainNameLabelScope
          value: []
        - name: customFqdn
          value: string
    - name: sku
      value:
        - name: name
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_clusters</code> resource.

```sql
/*+ update */
UPDATE azure.service_fabric_managed_clusters.managed_clusters
SET 
tags = '{{ tags }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_managed_clusters.managed_clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
