---
title: bare_metal_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_clusters
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

Creates, updates, deletes, gets or lists a <code>bare_metal_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bare_metal_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.gkeonprem.bare_metal_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The bare metal user cluster resource name. |
| <CopyableCode code="description" /> | `string` | A human readable description of this bare metal user cluster. |
| <CopyableCode code="adminClusterMembership" /> | `string` | Required. The admin cluster this bare metal user cluster belongs to. This is the full resource name of the admin cluster's fleet membership. |
| <CopyableCode code="adminClusterName" /> | `string` | Output only. The resource name of the bare metal admin cluster managing this user cluster. |
| <CopyableCode code="annotations" /> | `object` | Annotations on the bare metal user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| <CopyableCode code="bareMetalVersion" /> | `string` | Required. The Anthos clusters on bare metal version for your user cluster. |
| <CopyableCode code="binaryAuthorization" /> | `object` | Configuration for Binary Authorization. |
| <CopyableCode code="clusterOperations" /> | `object` | Specifies the bare metal user cluster's observability infrastructure. |
| <CopyableCode code="controlPlane" /> | `object` | Specifies the control plane configuration. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the bare metal user cluster was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time when the bare metal user cluster was deleted. If the resource is not deleted, this must be empty |
| <CopyableCode code="endpoint" /> | `string` | Output only. The IP address of the bare metal user cluster's API server. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| <CopyableCode code="fleet" /> | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| <CopyableCode code="loadBalancer" /> | `object` | Specifies the load balancer configuration. |
| <CopyableCode code="localName" /> | `string` | Output only. The object name of the bare metal user cluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the name in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. When the local name and cluster name differ, the local name is used in the admin cluster controller logs. You use the cluster name when accessing the cluster using bmctl and kubectl. |
| <CopyableCode code="maintenanceConfig" /> | `object` | Specifies configurations to put bare metal nodes in and out of maintenance. |
| <CopyableCode code="maintenanceStatus" /> | `object` | Represents the maintenance status of the bare metal user cluster. |
| <CopyableCode code="networkConfig" /> | `object` | Specifies the cluster network configuration. |
| <CopyableCode code="nodeAccessConfig" /> | `object` | Specifies the node access related settings for the bare metal user cluster. |
| <CopyableCode code="nodeConfig" /> | `object` | Specifies the workload node configurations. |
| <CopyableCode code="osEnvironmentConfig" /> | `object` | Specifies operating system settings for cluster provisioning. |
| <CopyableCode code="proxy" /> | `object` | Specifies the cluster proxy configuration. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. If set, there are currently changes in flight to the bare metal user cluster. |
| <CopyableCode code="securityConfig" /> | `object` | Specifies the security related settings for the bare metal user cluster. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the bare metal user cluster. |
| <CopyableCode code="status" /> | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| <CopyableCode code="storage" /> | `object` | BareMetalStorageConfig specifies the cluster storage configuration. |
| <CopyableCode code="uid" /> | `string` | Output only. The unique identifier of the bare metal user cluster. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the bare metal user cluster was last updated. |
| <CopyableCode code="upgradePolicy" /> | `object` | BareMetalClusterUpgradePolicy defines the cluster upgrade policy. |
| <CopyableCode code="validationCheck" /> | `object` | ValidationCheck represents the result of preflight check. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_bare_metal_clusters_get" /> | `SELECT` | <CopyableCode code="bareMetalClustersId, locationsId, projectsId" /> | Gets details of a single bare metal Cluster. |
| <CopyableCode code="projects_locations_bare_metal_clusters_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists bare metal clusters in a given project and location. |
| <CopyableCode code="projects_locations_bare_metal_clusters_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new bare metal cluster in a given project and location. |
| <CopyableCode code="projects_locations_bare_metal_clusters_delete" /> | `DELETE` | <CopyableCode code="bareMetalClustersId, locationsId, projectsId" /> | Deletes a single bare metal Cluster. |
| <CopyableCode code="projects_locations_bare_metal_clusters_patch" /> | `UPDATE` | <CopyableCode code="bareMetalClustersId, locationsId, projectsId" /> | Updates the parameters of a single bare metal Cluster. |
| <CopyableCode code="projects_locations_bare_metal_clusters_enroll" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Enrolls an existing bare metal user cluster and its node pools to the Anthos On-Prem API within a given project and location. Through enrollment, an existing cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster and/or its node pools will be expected to be performed through the API. |
| <CopyableCode code="projects_locations_bare_metal_clusters_query_version_config" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Queries the bare metal user cluster version config. |
| <CopyableCode code="projects_locations_bare_metal_clusters_unenroll" /> | `EXEC` | <CopyableCode code="bareMetalClustersId, locationsId, projectsId" /> | Unenrolls an existing bare metal user cluster and its node pools from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters and node pools will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |

## `SELECT` examples

Lists bare metal clusters in a given project and location.

```sql
SELECT
name,
description,
adminClusterMembership,
adminClusterName,
annotations,
bareMetalVersion,
binaryAuthorization,
clusterOperations,
controlPlane,
createTime,
deleteTime,
endpoint,
etag,
fleet,
loadBalancer,
localName,
maintenanceConfig,
maintenanceStatus,
networkConfig,
nodeAccessConfig,
nodeConfig,
osEnvironmentConfig,
proxy,
reconciling,
securityConfig,
state,
status,
storage,
uid,
updateTime,
upgradePolicy,
validationCheck
FROM google.gkeonprem.bare_metal_clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bare_metal_clusters</code> resource.

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
INSERT INTO google.gkeonprem.bare_metal_clusters (
locationsId,
projectsId,
name,
adminClusterMembership,
description,
bareMetalVersion,
annotations,
networkConfig,
controlPlane,
loadBalancer,
storage,
proxy,
clusterOperations,
maintenanceConfig,
nodeConfig,
securityConfig,
nodeAccessConfig,
osEnvironmentConfig,
binaryAuthorization,
upgradePolicy
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ adminClusterMembership }}',
'{{ description }}',
'{{ bareMetalVersion }}',
'{{ annotations }}',
'{{ networkConfig }}',
'{{ controlPlane }}',
'{{ loadBalancer }}',
'{{ storage }}',
'{{ proxy }}',
'{{ clusterOperations }}',
'{{ maintenanceConfig }}',
'{{ nodeConfig }}',
'{{ securityConfig }}',
'{{ nodeAccessConfig }}',
'{{ osEnvironmentConfig }}',
'{{ binaryAuthorization }}',
'{{ upgradePolicy }}'
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
    - name: bareMetalVersion
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
    - name: deleteTime
      value: string
    - name: localName
      value: string
    - name: etag
      value: string
    - name: annotations
      value: object
    - name: networkConfig
      value:
        - name: islandModeCidr
          value:
            - name: serviceAddressCidrBlocks
              value:
                - string
            - name: podAddressCidrBlocks
              value:
                - string
        - name: advancedNetworking
          value: boolean
        - name: multipleNetworkInterfacesConfig
          value:
            - name: enabled
              value: boolean
        - name: srIovConfig
          value:
            - name: enabled
              value: boolean
    - name: controlPlane
      value:
        - name: controlPlaneNodePoolConfig
          value:
            - name: nodePoolConfig
              value:
                - name: nodeConfigs
                  value:
                    - - name: nodeIp
                        value: string
                      - name: labels
                        value: object
                - name: operatingSystem
                  value: string
                - name: taints
                  value:
                    - - name: key
                        value: string
                      - name: value
                        value: string
                      - name: effect
                        value: string
                - name: labels
                  value: object
                - name: kubeletConfig
                  value:
                    - name: registryPullQps
                      value: integer
                    - name: registryBurst
                      value: integer
                    - name: serializeImagePullsDisabled
                      value: boolean
        - name: apiServerArgs
          value:
            - - name: argument
                value: string
              - name: value
                value: string
    - name: loadBalancer
      value:
        - name: vipConfig
          value:
            - name: controlPlaneVip
              value: string
            - name: ingressVip
              value: string
        - name: portConfig
          value:
            - name: controlPlaneLoadBalancerPort
              value: integer
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
            - name: loadBalancerNodePoolConfig
              value: []
        - name: manualLbConfig
          value:
            - name: enabled
              value: boolean
        - name: bgpLbConfig
          value:
            - name: asn
              value: string
            - name: bgpPeerConfigs
              value:
                - - name: asn
                    value: string
                  - name: ipAddress
                    value: string
                  - name: controlPlaneNodes
                    value:
                      - string
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
    - name: storage
      value:
        - name: lvpShareConfig
          value:
            - name: lvpConfig
              value:
                - name: path
                  value: string
                - name: storageClass
                  value: string
            - name: sharedPathPvCount
              value: integer
    - name: proxy
      value:
        - name: uri
          value: string
        - name: noProxy
          value:
            - string
    - name: clusterOperations
      value:
        - name: enableApplicationLogs
          value: boolean
    - name: maintenanceConfig
      value:
        - name: maintenanceAddressCidrBlocks
          value:
            - string
    - name: nodeConfig
      value:
        - name: maxPodsPerNode
          value: string
        - name: containerRuntime
          value: string
    - name: fleet
      value:
        - name: membership
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
    - name: securityConfig
      value:
        - name: authorization
          value:
            - name: adminUsers
              value:
                - - name: username
                    value: string
    - name: maintenanceStatus
      value:
        - name: machineDrainStatus
          value:
            - name: drainingMachines
              value:
                - - name: nodeIp
                    value: string
                  - name: podCount
                    value: integer
            - name: drainedMachines
              value:
                - - name: nodeIp
                    value: string
    - name: adminClusterName
      value: string
    - name: nodeAccessConfig
      value:
        - name: loginUser
          value: string
    - name: osEnvironmentConfig
      value:
        - name: packageRepoExcluded
          value: boolean
    - name: binaryAuthorization
      value:
        - name: evaluationMode
          value: string
    - name: upgradePolicy
      value:
        - name: policy
          value: string
        - name: pause
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bare_metal_clusters</code> resource.

```sql
/*+ update */
UPDATE google.gkeonprem.bare_metal_clusters
SET 
name = '{{ name }}',
adminClusterMembership = '{{ adminClusterMembership }}',
description = '{{ description }}',
bareMetalVersion = '{{ bareMetalVersion }}',
annotations = '{{ annotations }}',
networkConfig = '{{ networkConfig }}',
controlPlane = '{{ controlPlane }}',
loadBalancer = '{{ loadBalancer }}',
storage = '{{ storage }}',
proxy = '{{ proxy }}',
clusterOperations = '{{ clusterOperations }}',
maintenanceConfig = '{{ maintenanceConfig }}',
nodeConfig = '{{ nodeConfig }}',
securityConfig = '{{ securityConfig }}',
nodeAccessConfig = '{{ nodeAccessConfig }}',
osEnvironmentConfig = '{{ osEnvironmentConfig }}',
binaryAuthorization = '{{ binaryAuthorization }}',
upgradePolicy = '{{ upgradePolicy }}'
WHERE 
bareMetalClustersId = '{{ bareMetalClustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>bare_metal_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM google.gkeonprem.bare_metal_clusters
WHERE bareMetalClustersId = '{{ bareMetalClustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
