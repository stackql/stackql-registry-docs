---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
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

Creates, updates, deletes, gets or lists a <code>managed_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.managed_clusters" /></td></tr>
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
| <CopyableCode code="aad_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="addon_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_pool_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_server_access_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scaler_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_upgrade_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_monitor_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_portal_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_encryption_set_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_pod_security_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_rbac" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn_subdomain" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_proxy_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the managed cluster. |
| <CopyableCode code="identity_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="linux_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_agent_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="metrics_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="oidc_issuer_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="pod_identity_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uid" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_mesh_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_principal_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU of a Managed Cluster. |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="upgrade_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="windows_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_auto_scaler_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the managed cluster. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the managed cluster. |
| <CopyableCode code="sku" /> | `object` | The SKU of a Managed Cluster. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="abort_latest_operation" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Aborts the currently running operation on the managed cluster. The Managed Cluster will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned. |
| <CopyableCode code="reset_aad_profile" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | **WARNING**: This API will be deprecated. Please see [AKS-managed Azure Active Directory integration](https://aka.ms/aks-managed-aad) to update your cluster with AKS-managed Azure AD. |
| <CopyableCode code="reset_service_principal_profile" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__clientId" /> | This action cannot be performed on a cluster that is not using a service principal |
| <CopyableCode code="rotate_cluster_certificates" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | See [Certificate rotation](https://docs.microsoft.com/azure/aks/certificate-rotation) for more details about rotating managed cluster certificates. |
| <CopyableCode code="rotate_service_account_signing_keys" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="run_command" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId, data__command" /> | AKS will create a pod to run the command. This is primarily useful for private clusters. For more information see [AKS Run Command](https://docs.microsoft.com/azure/aks/private-clusters#aks-run-command-preview). |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | See [starting a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about starting a cluster. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | This can only be performed on Azure Virtual Machine Scale set backed clusters. Stopping a cluster stops the control plane and agent nodes entirely, while maintaining all object and cluster state. A cluster does not accrue charges while it is stopped. See [stopping a cluster](https://docs.microsoft.com/azure/aks/start-stop-cluster) for more details about stopping a cluster. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



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
aad_profile,
addon_profiles,
agent_pool_profiles,
api_server_access_profile,
auto_scaler_profile,
auto_upgrade_profile,
azure_monitor_profile,
azure_portal_fqdn,
current_kubernetes_version,
disable_local_accounts,
disk_encryption_set_id,
dns_prefix,
enable_pod_security_policy,
enable_rbac,
extended_location,
fqdn,
fqdn_subdomain,
http_proxy_config,
identity,
identity_profile,
ingress_profile,
kubernetes_version,
linux_profile,
location,
max_agent_pools,
metrics_profile,
network_profile,
node_resource_group,
oidc_issuer_profile,
pod_identity_profile,
power_state,
private_fqdn,
private_link_resources,
provisioning_state,
public_network_access,
resourceGroupName,
resourceName,
resource_uid,
security_profile,
service_mesh_profile,
service_principal_profile,
sku,
storage_profile,
subscriptionId,
support_plan,
tags,
upgrade_settings,
windows_profile,
workload_auto_scaler_profile
FROM azure.aks.vw_managed_clusters
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
sku,
tags
FROM azure.aks.managed_clusters
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
INSERT INTO azure.aks.managed_clusters (
resourceGroupName,
resourceName,
subscriptionId,
sku,
extendedLocation,
identity,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: delegatedResources
          value: []
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: powerState
          value:
            - name: code
              value: string
        - name: maxAgentPools
          value: integer
        - name: kubernetesVersion
          value: string
        - name: currentKubernetesVersion
          value: string
        - name: dnsPrefix
          value: string
        - name: fqdnSubdomain
          value: string
        - name: fqdn
          value: string
        - name: privateFQDN
          value: string
        - name: azurePortalFQDN
          value: string
        - name: agentPoolProfiles
          value:
            - - name: count
                value: integer
              - name: vmSize
                value: string
              - name: osDiskSizeGB
                value: []
              - name: osDiskType
                value: []
              - name: kubeletDiskType
                value: []
              - name: workloadRuntime
                value: []
              - name: vnetSubnetID
                value: string
              - name: podSubnetID
                value: string
              - name: maxPods
                value: integer
              - name: osType
                value: []
              - name: osSKU
                value: []
              - name: maxCount
                value: integer
              - name: minCount
                value: integer
              - name: enableAutoScaling
                value: boolean
              - name: scaleDownMode
                value: []
              - name: type
                value: []
              - name: mode
                value: []
              - name: orchestratorVersion
                value: string
              - name: currentOrchestratorVersion
                value: string
              - name: nodeImageVersion
                value: string
              - name: upgradeSettings
                value:
                  - name: maxSurge
                    value: string
                  - name: drainTimeoutInMinutes
                    value: integer
                  - name: nodeSoakDurationInMinutes
                    value: integer
              - name: provisioningState
                value: string
              - name: availabilityZones
                value:
                  - string
              - name: enableNodePublicIP
                value: boolean
              - name: nodePublicIPPrefixID
                value: string
              - name: scaleSetPriority
                value: []
              - name: scaleSetEvictionPolicy
                value: []
              - name: spotMaxPrice
                value: []
              - name: tags
                value: object
              - name: nodeLabels
                value: object
              - name: nodeTaints
                value:
                  - string
              - name: proximityPlacementGroupID
                value: []
              - name: kubeletConfig
                value:
                  - name: cpuManagerPolicy
                    value: string
                  - name: cpuCfsQuota
                    value: boolean
                  - name: cpuCfsQuotaPeriod
                    value: string
                  - name: imageGcHighThreshold
                    value: integer
                  - name: imageGcLowThreshold
                    value: integer
                  - name: topologyManagerPolicy
                    value: string
                  - name: allowedUnsafeSysctls
                    value:
                      - string
                  - name: failSwapOn
                    value: boolean
                  - name: containerLogMaxSizeMB
                    value: integer
                  - name: containerLogMaxFiles
                    value: integer
                  - name: podMaxPids
                    value: integer
              - name: linuxOSConfig
                value:
                  - name: sysctls
                    value:
                      - name: netCoreSomaxconn
                        value: integer
                      - name: netCoreNetdevMaxBacklog
                        value: integer
                      - name: netCoreRmemDefault
                        value: integer
                      - name: netCoreRmemMax
                        value: integer
                      - name: netCoreWmemDefault
                        value: integer
                      - name: netCoreWmemMax
                        value: integer
                      - name: netCoreOptmemMax
                        value: integer
                      - name: netIpv4TcpMaxSynBacklog
                        value: integer
                      - name: netIpv4TcpMaxTwBuckets
                        value: integer
                      - name: netIpv4TcpFinTimeout
                        value: integer
                      - name: netIpv4TcpKeepaliveTime
                        value: integer
                      - name: netIpv4TcpKeepaliveProbes
                        value: integer
                      - name: netIpv4TcpkeepaliveIntvl
                        value: integer
                      - name: netIpv4TcpTwReuse
                        value: boolean
                      - name: netIpv4IpLocalPortRange
                        value: string
                      - name: netIpv4NeighDefaultGcThresh1
                        value: integer
                      - name: netIpv4NeighDefaultGcThresh2
                        value: integer
                      - name: netIpv4NeighDefaultGcThresh3
                        value: integer
                      - name: netNetfilterNfConntrackMax
                        value: integer
                      - name: netNetfilterNfConntrackBuckets
                        value: integer
                      - name: fsInotifyMaxUserWatches
                        value: integer
                      - name: fsFileMax
                        value: integer
                      - name: fsAioMaxNr
                        value: integer
                      - name: fsNrOpen
                        value: integer
                      - name: kernelThreadsMax
                        value: integer
                      - name: vmMaxMapCount
                        value: integer
                      - name: vmSwappiness
                        value: integer
                      - name: vmVfsCachePressure
                        value: integer
                  - name: transparentHugePageEnabled
                    value: string
                  - name: transparentHugePageDefrag
                    value: string
                  - name: swapFileSizeMB
                    value: integer
              - name: enableEncryptionAtHost
                value: boolean
              - name: enableUltraSSD
                value: boolean
              - name: enableFIPS
                value: boolean
              - name: gpuInstanceProfile
                value: []
              - name: creationData
                value:
                  - name: sourceResourceId
                    value: string
              - name: capacityReservationGroupID
                value: []
              - name: hostGroupID
                value: string
              - name: networkProfile
                value:
                  - name: nodePublicIPTags
                    value: []
                  - name: allowedHostPorts
                    value:
                      - - name: portStart
                          value: integer
                        - name: portEnd
                          value: integer
                        - name: protocol
                          value: string
                  - name: applicationSecurityGroups
                    value:
                      - string
              - name: windowsProfile
                value:
                  - name: disableOutboundNat
                    value: boolean
              - name: securityProfile
                value:
                  - name: enableVTPM
                    value: boolean
                  - name: enableSecureBoot
                    value: boolean
              - name: name
                value: string
        - name: linuxProfile
          value:
            - name: adminUsername
              value: string
            - name: ssh
              value:
                - name: publicKeys
                  value:
                    - - name: keyData
                        value: string
        - name: windowsProfile
          value:
            - name: adminUsername
              value: string
            - name: adminPassword
              value: string
            - name: licenseType
              value: string
            - name: enableCSIProxy
              value: boolean
            - name: gmsaProfile
              value:
                - name: enabled
                  value: boolean
                - name: dnsServer
                  value: string
                - name: rootDomainName
                  value: string
        - name: servicePrincipalProfile
          value:
            - name: clientId
              value: string
            - name: secret
              value: string
        - name: addonProfiles
          value: object
        - name: podIdentityProfile
          value:
            - name: enabled
              value: boolean
            - name: allowNetworkPluginKubenet
              value: boolean
            - name: userAssignedIdentities
              value:
                - - name: name
                    value: string
                  - name: namespace
                    value: string
                  - name: bindingSelector
                    value: string
                  - name: identity
                    value:
                      - name: resourceId
                        value: string
                      - name: clientId
                        value: string
                      - name: objectId
                        value: string
                  - name: provisioningState
                    value: string
                  - name: provisioningInfo
                    value:
                      - name: error
                        value:
                          - name: error
                            value:
                              - name: code
                                value: string
                              - name: message
                                value: string
                              - name: target
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: message
                                      value: string
                                    - name: target
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: message
                                            value: string
                                          - name: target
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: target
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: target
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - []
            - name: userAssignedIdentityExceptions
              value:
                - - name: name
                    value: string
                  - name: namespace
                    value: string
                  - name: podLabels
                    value: object
        - name: oidcIssuerProfile
          value:
            - name: issuerURL
              value: string
            - name: enabled
              value: boolean
        - name: nodeResourceGroup
          value: string
        - name: enableRBAC
          value: boolean
        - name: supportPlan
          value: []
        - name: enablePodSecurityPolicy
          value: boolean
        - name: networkProfile
          value:
            - name: networkPlugin
              value: string
            - name: networkPluginMode
              value: string
            - name: networkPolicy
              value: string
            - name: networkMode
              value: string
            - name: networkDataplane
              value: string
            - name: podCidr
              value: string
            - name: serviceCidr
              value: string
            - name: dnsServiceIP
              value: string
            - name: outboundType
              value: string
            - name: loadBalancerSku
              value: string
            - name: loadBalancerProfile
              value:
                - name: managedOutboundIPs
                  value:
                    - name: count
                      value: integer
                    - name: countIPv6
                      value: integer
                - name: outboundIPPrefixes
                  value:
                    - name: publicIPPrefixes
                      value:
                        - - name: id
                            value: string
                - name: outboundIPs
                  value:
                    - name: publicIPs
                      value:
                        - - name: id
                            value: string
                - name: effectiveOutboundIPs
                  value:
                    - - name: id
                        value: string
                - name: allocatedOutboundPorts
                  value: integer
                - name: idleTimeoutInMinutes
                  value: integer
                - name: enableMultipleStandardLoadBalancers
                  value: boolean
                - name: backendPoolType
                  value: string
            - name: natGatewayProfile
              value:
                - name: managedOutboundIPProfile
                  value:
                    - name: count
                      value: integer
                - name: effectiveOutboundIPs
                  value:
                    - - name: id
                        value: string
                - name: idleTimeoutInMinutes
                  value: integer
            - name: podCidrs
              value:
                - string
            - name: serviceCidrs
              value:
                - string
            - name: ipFamilies
              value:
                - string
        - name: aadProfile
          value:
            - name: managed
              value: boolean
            - name: enableAzureRBAC
              value: boolean
            - name: adminGroupObjectIDs
              value:
                - string
            - name: clientAppID
              value: string
            - name: serverAppID
              value: string
            - name: serverAppSecret
              value: string
            - name: tenantID
              value: string
        - name: autoUpgradeProfile
          value:
            - name: upgradeChannel
              value: string
            - name: nodeOSUpgradeChannel
              value: string
        - name: upgradeSettings
          value:
            - name: overrideSettings
              value:
                - name: forceUpgrade
                  value: boolean
                - name: until
                  value: string
        - name: autoScalerProfile
          value:
            - name: balance-similar-node-groups
              value: string
            - name: daemonset-eviction-for-empty-nodes
              value: boolean
            - name: daemonset-eviction-for-occupied-nodes
              value: boolean
            - name: ignore-daemonsets-utilization
              value: boolean
            - name: expander
              value: string
            - name: max-empty-bulk-delete
              value: string
            - name: max-graceful-termination-sec
              value: string
            - name: max-node-provision-time
              value: string
            - name: max-total-unready-percentage
              value: string
            - name: new-pod-scale-up-delay
              value: string
            - name: ok-total-unready-count
              value: string
            - name: scan-interval
              value: string
            - name: scale-down-delay-after-add
              value: string
            - name: scale-down-delay-after-delete
              value: string
            - name: scale-down-delay-after-failure
              value: string
            - name: scale-down-unneeded-time
              value: string
            - name: scale-down-unready-time
              value: string
            - name: scale-down-utilization-threshold
              value: string
            - name: skip-nodes-with-local-storage
              value: string
            - name: skip-nodes-with-system-pods
              value: string
        - name: apiServerAccessProfile
          value:
            - name: authorizedIPRanges
              value:
                - string
            - name: enablePrivateCluster
              value: boolean
            - name: privateDNSZone
              value: string
            - name: enablePrivateClusterPublicFQDN
              value: boolean
            - name: disableRunCommand
              value: boolean
        - name: diskEncryptionSetID
          value: string
        - name: identityProfile
          value: object
        - name: privateLinkResources
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: groupId
                value: string
              - name: requiredMembers
                value:
                  - string
              - name: privateLinkServiceID
                value: string
        - name: disableLocalAccounts
          value: boolean
        - name: httpProxyConfig
          value:
            - name: httpProxy
              value: string
            - name: httpsProxy
              value: string
            - name: noProxy
              value:
                - string
            - name: trustedCa
              value: string
        - name: securityProfile
          value:
            - name: defender
              value:
                - name: logAnalyticsWorkspaceResourceId
                  value: string
                - name: securityMonitoring
                  value:
                    - name: enabled
                      value: boolean
            - name: azureKeyVaultKms
              value:
                - name: enabled
                  value: boolean
                - name: keyId
                  value: string
                - name: keyVaultNetworkAccess
                  value: string
                - name: keyVaultResourceId
                  value: string
            - name: workloadIdentity
              value:
                - name: enabled
                  value: boolean
            - name: imageCleaner
              value:
                - name: enabled
                  value: boolean
                - name: intervalHours
                  value: integer
        - name: storageProfile
          value:
            - name: diskCSIDriver
              value:
                - name: enabled
                  value: boolean
            - name: fileCSIDriver
              value:
                - name: enabled
                  value: boolean
            - name: snapshotController
              value:
                - name: enabled
                  value: boolean
            - name: blobCSIDriver
              value:
                - name: enabled
                  value: boolean
        - name: ingressProfile
          value:
            - name: webAppRouting
              value:
                - name: enabled
                  value: boolean
                - name: dnsZoneResourceIds
                  value:
                    - string
        - name: publicNetworkAccess
          value: string
        - name: workloadAutoScalerProfile
          value:
            - name: keda
              value:
                - name: enabled
                  value: boolean
            - name: verticalPodAutoscaler
              value:
                - name: enabled
                  value: boolean
        - name: azureMonitorProfile
          value:
            - name: metrics
              value:
                - name: enabled
                  value: boolean
                - name: kubeStateMetrics
                  value:
                    - name: metricLabelsAllowlist
                      value: string
                    - name: metricAnnotationsAllowList
                      value: string
        - name: serviceMeshProfile
          value:
            - name: mode
              value: string
            - name: istio
              value:
                - name: components
                  value:
                    - name: ingressGateways
                      value:
                        - - name: mode
                            value: string
                          - name: enabled
                            value: boolean
                    - name: egressGateways
                      value:
                        - - name: enabled
                            value: boolean
                - name: certificateAuthority
                  value:
                    - name: plugin
                      value:
                        - name: keyVaultId
                          value: string
                        - name: certObjectName
                          value: string
                        - name: keyObjectName
                          value: string
                        - name: rootCertObjectName
                          value: string
                        - name: certChainObjectName
                          value: string
                - name: revisions
                  value:
                    - string
        - name: resourceUID
          value: string
        - name: metricsProfile
          value:
            - name: costAnalysis
              value:
                - name: enabled
                  value: boolean
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aks.managed_clusters
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
