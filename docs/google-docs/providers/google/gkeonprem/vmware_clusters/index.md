---
title: vmware_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_clusters
  - gkeonprem
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

Creates, updates, deletes, gets or lists a <code>vmware_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vmware_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkeonprem.vmware_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The VMware user cluster resource name. |
| <CopyableCode code="description" /> | `string` | A human readable description of this VMware user cluster. |
| <CopyableCode code="adminClusterMembership" /> | `string` | Required. The admin cluster this VMware user cluster belongs to. This is the full resource name of the admin cluster's fleet membership. In the future, references to other resource types might be allowed if admin clusters are modeled as their own resources. |
| <CopyableCode code="adminClusterName" /> | `string` | Output only. The resource name of the VMware admin cluster hosting this user cluster. |
| <CopyableCode code="annotations" /> | `object` | Annotations on the VMware user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="antiAffinityGroups" /> | `object` | Specifies anti affinity group config for the VMware user cluster. |
| <CopyableCode code="authorization" /> | `object` | Authorization defines the On-Prem cluster authorization configuration to bootstrap onto the admin cluster. |
| <CopyableCode code="autoRepairConfig" /> | `object` | Specifies config to enable/disable auto repair. The cluster-health-controller is deployed only if Enabled is true. |
| <CopyableCode code="binaryAuthorization" /> | `object` | Configuration for Binary Authorization. |
| <CopyableCode code="controlPlaneNode" /> | `object` | Specifies control plane node config for the VMware user cluster. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which VMware user cluster was created. |
| <CopyableCode code="dataplaneV2" /> | `object` | Contains configurations for Dataplane V2, which is optimized dataplane for Kubernetes networking. For more information, see: https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2 |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which VMware user cluster was deleted. |
| <CopyableCode code="disableBundledIngress" /> | `boolean` | Disable bundled ingress. |
| <CopyableCode code="enableControlPlaneV2" /> | `boolean` | Enable control plane V2. Default to false. |
| <CopyableCode code="endpoint" /> | `string` | Output only. The DNS name of VMware user cluster's API server. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| <CopyableCode code="fleet" /> | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| <CopyableCode code="loadBalancer" /> | `object` | Specifies the locad balancer config for the VMware user cluster. |
| <CopyableCode code="localName" /> | `string` | Output only. The object name of the VMware OnPremUserCluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |
| <CopyableCode code="networkConfig" /> | `object` | Specifies network config for the VMware user cluster. |
| <CopyableCode code="onPremVersion" /> | `string` | Required. The Anthos clusters on the VMware version for your user cluster. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. If set, there are currently changes in flight to the VMware user cluster. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of VMware user cluster. |
| <CopyableCode code="status" /> | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| <CopyableCode code="storage" /> | `object` | Specifies vSphere CSI components deployment config in the VMware user cluster. |
| <CopyableCode code="uid" /> | `string` | Output only. The unique identifier of the VMware user cluster. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which VMware user cluster was last updated. |
| <CopyableCode code="upgradePolicy" /> | `object` | VmwareClusterUpgradePolicy defines the cluster upgrade policy. |
| <CopyableCode code="validationCheck" /> | `object` | ValidationCheck represents the result of preflight check. |
| <CopyableCode code="vcenter" /> | `object` | Represents configuration for the VMware VCenter for the user cluster. |
| <CopyableCode code="vmTrackingEnabled" /> | `boolean` | Enable VM tracking. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_vmware_clusters_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Gets details of a single VMware Cluster. |
| <CopyableCode code="projects_locations_vmware_clusters_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists VMware Clusters in a given project and location. |
| <CopyableCode code="projects_locations_vmware_clusters_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new VMware user cluster in a given project and location. |
| <CopyableCode code="projects_locations_vmware_clusters_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Deletes a single VMware Cluster. |
| <CopyableCode code="projects_locations_vmware_clusters_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Updates the parameters of a single VMware cluster. |
| <CopyableCode code="projects_locations_vmware_clusters_enroll" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Enrolls an existing VMware user cluster and its node pools to the Anthos On-Prem API within a given project and location. Through enrollment, an existing cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster and/or its node pools will be expected to be performed through the API. |
| <CopyableCode code="projects_locations_vmware_clusters_query_version_config" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Queries the VMware user cluster version config. |
| <CopyableCode code="projects_locations_vmware_clusters_unenroll" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, vmwareClustersId" /> | Unenrolls an existing VMware user cluster and its node pools from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters and node pools will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or UI. |

## `SELECT` examples

Lists VMware Clusters in a given project and location.

```sql
SELECT
name,
description,
adminClusterMembership,
adminClusterName,
annotations,
antiAffinityGroups,
authorization,
autoRepairConfig,
binaryAuthorization,
controlPlaneNode,
createTime,
dataplaneV2,
deleteTime,
disableBundledIngress,
enableControlPlaneV2,
endpoint,
etag,
fleet,
loadBalancer,
localName,
networkConfig,
onPremVersion,
reconciling,
state,
status,
storage,
uid,
updateTime,
upgradePolicy,
validationCheck,
vcenter,
vmTrackingEnabled
FROM google.gkeonprem.vmware_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vmware_clusters</code> resource.

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
INSERT INTO google.gkeonprem.vmware_clusters (
locationsId,
projectsId,
name,
adminClusterMembership,
description,
onPremVersion,
etag,
annotations,
controlPlaneNode,
antiAffinityGroups,
storage,
networkConfig,
loadBalancer,
vcenter,
dataplaneV2,
vmTrackingEnabled,
autoRepairConfig,
authorization,
enableControlPlaneV2,
binaryAuthorization,
upgradePolicy,
disableBundledIngress
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ adminClusterMembership }}',
'{{ description }}',
'{{ onPremVersion }}',
'{{ etag }}',
'{{ annotations }}',
'{{ controlPlaneNode }}',
'{{ antiAffinityGroups }}',
'{{ storage }}',
'{{ networkConfig }}',
'{{ loadBalancer }}',
'{{ vcenter }}',
'{{ dataplaneV2 }}',
{{ vmTrackingEnabled }},
'{{ autoRepairConfig }}',
'{{ authorization }}',
{{ enableControlPlaneV2 }},
'{{ binaryAuthorization }}',
'{{ upgradePolicy }}',
{{ disableBundledIngress }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: adminClusterMembership
      value: string
    - name: description
      value: string
    - name: onPremVersion
      value: string
    - name: uid
      value: string
    - name: state
      value: string
    - name: endpoint
      value: string
    - name: reconciling
      value: boolean
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: localName
      value: string
    - name: etag
      value: string
    - name: annotations
      value: object
    - name: controlPlaneNode
      value:
        - name: cpus
          value: string
        - name: memory
          value: string
        - name: replicas
          value: string
        - name: autoResizeConfig
          value:
            - name: enabled
              value: boolean
        - name: vsphereConfig
          value:
            - name: datastore
              value: string
            - name: storagePolicyName
              value: string
    - name: antiAffinityGroups
      value:
        - name: aagConfigDisabled
          value: boolean
    - name: storage
      value:
        - name: vsphereCsiDisabled
          value: boolean
    - name: networkConfig
      value:
        - name: serviceAddressCidrBlocks
          value:
            - string
        - name: podAddressCidrBlocks
          value:
            - string
        - name: staticIpConfig
          value:
            - name: ipBlocks
              value:
                - - name: netmask
                    value: string
                  - name: gateway
                    value: string
                  - name: ips
                    value:
                      - - name: ip
                          value: string
                        - name: hostname
                          value: string
        - name: dhcpIpConfig
          value:
            - name: enabled
              value: boolean
        - name: vcenterNetwork
          value: string
        - name: hostConfig
          value:
            - name: dnsServers
              value:
                - string
            - name: ntpServers
              value:
                - string
            - name: dnsSearchDomains
              value:
                - string
        - name: controlPlaneV2Config
          value:
            - name: controlPlaneIpBlock
              value:
                - name: netmask
                  value: string
                - name: gateway
                  value: string
                - name: ips
                  value:
                    - - name: ip
                        value: string
                      - name: hostname
                        value: string
    - name: loadBalancer
      value:
        - name: vipConfig
          value:
            - name: controlPlaneVip
              value: string
            - name: ingressVip
              value: string
        - name: f5Config
          value:
            - name: address
              value: string
            - name: partition
              value: string
            - name: snatPool
              value: string
        - name: manualLbConfig
          value:
            - name: ingressHttpNodePort
              value: integer
            - name: ingressHttpsNodePort
              value: integer
            - name: controlPlaneNodePort
              value: integer
            - name: konnectivityServerNodePort
              value: integer
        - name: seesawConfig
          value:
            - name: group
              value: string
            - name: masterIp
              value: string
            - name: ipBlocks
              value:
                - - name: netmask
                    value: string
                  - name: gateway
                    value: string
                  - name: ips
                    value:
                      - - name: ip
                          value: string
                        - name: hostname
                          value: string
            - name: enableHa
              value: boolean
            - name: vms
              value:
                - string
            - name: stackdriverName
              value: string
        - name: metalLbConfig
          value:
            - name: addressPools
              value:
                - - name: pool
                    value: string
                  - name: addresses
                    value:
                      - string
                  - name: avoidBuggyIps
                    value: boolean
                  - name: manualAssign
                    value: boolean
    - name: vcenter
      value:
        - name: resourcePool
          value: string
        - name: datastore
          value: string
        - name: datacenter
          value: string
        - name: cluster
          value: string
        - name: folder
          value: string
        - name: caCertData
          value: string
        - name: address
          value: string
        - name: storagePolicyName
          value: string
    - name: status
      value:
        - name: errorMessage
          value: string
        - name: conditions
          value:
            - - name: type
                value: string
              - name: reason
                value: string
              - name: message
                value: string
              - name: lastTransitionTime
                value: string
              - name: state
                value: string
        - name: version
          value: string
        - name: versions
          value:
            - name: versions
              value:
                - - name: version
                    value: string
                  - name: count
                    value: string
    - name: dataplaneV2
      value:
        - name: dataplaneV2Enabled
          value: boolean
        - name: windowsDataplaneV2Enabled
          value: boolean
        - name: advancedNetworking
          value: boolean
        - name: forwardMode
          value: string
    - name: vmTrackingEnabled
      value: boolean
    - name: autoRepairConfig
      value:
        - name: enabled
          value: boolean
    - name: fleet
      value:
        - name: membership
          value: string
    - name: authorization
      value:
        - name: adminUsers
          value:
            - - name: username
                value: string
    - name: deleteTime
      value: string
    - name: validationCheck
      value:
        - name: option
          value: string
        - name: status
          value:
            - name: result
              value:
                - - name: state
                    value: string
                  - name: description
                    value: string
                  - name: category
                    value: string
                  - name: reason
                    value: string
                  - name: details
                    value: string
        - name: scenario
          value: string
    - name: adminClusterName
      value: string
    - name: enableControlPlaneV2
      value: boolean
    - name: binaryAuthorization
      value:
        - name: evaluationMode
          value: string
    - name: upgradePolicy
      value:
        - name: controlPlaneOnly
          value: boolean
    - name: disableBundledIngress
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vmware_clusters</code> resource.

```sql
/*+ update */
UPDATE google.gkeonprem.vmware_clusters
SET 
name = '{{ name }}',
adminClusterMembership = '{{ adminClusterMembership }}',
description = '{{ description }}',
onPremVersion = '{{ onPremVersion }}',
etag = '{{ etag }}',
annotations = '{{ annotations }}',
controlPlaneNode = '{{ controlPlaneNode }}',
antiAffinityGroups = '{{ antiAffinityGroups }}',
storage = '{{ storage }}',
networkConfig = '{{ networkConfig }}',
loadBalancer = '{{ loadBalancer }}',
vcenter = '{{ vcenter }}',
dataplaneV2 = '{{ dataplaneV2 }}',
vmTrackingEnabled = true|false,
autoRepairConfig = '{{ autoRepairConfig }}',
authorization = '{{ authorization }}',
enableControlPlaneV2 = true|false,
binaryAuthorization = '{{ binaryAuthorization }}',
upgradePolicy = '{{ upgradePolicy }}',
disableBundledIngress = true|false
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND vmwareClustersId = '{{ vmwareClustersId }}';
```

## `DELETE` example

Deletes the specified <code>vmware_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM google.gkeonprem.vmware_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND vmwareClustersId = '{{ vmwareClustersId }}';
```
