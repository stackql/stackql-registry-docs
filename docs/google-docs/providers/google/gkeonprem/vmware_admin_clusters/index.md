---
title: vmware_admin_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_admin_clusters
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vmware_admin_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.vmware_admin_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The VMware admin cluster resource name. |
| `description` | `string` | A human readable description of this VMware admin cluster. |
| `imageType` | `string` | The OS image type for the VMware admin cluster. |
| `updateTime` | `string` | Output only. The time at which VMware admin cluster was last updated. |
| `status` | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| `onPremVersion` | `string` | The Anthos clusters on the VMware version for the admin cluster. |
| `autoRepairConfig` | `object` | Specifies config to enable/disable auto repair. The cluster-health-controller is deployed only if Enabled is true. |
| `uid` | `string` | Output only. The unique identifier of the VMware admin cluster. |
| `addonNode` | `object` | VmwareAdminAddonNodeConfig contains add-on node configurations for VMware admin cluster. |
| `fleet` | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| `antiAffinityGroups` | `object` | Specifies anti affinity group config for the VMware user cluster. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| `annotations` | `object` | Annotations on the VMware admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `controlPlaneNode` | `object` | VmwareAdminControlPlaneNodeConfig contains control plane node configuration for VMware admin cluster. |
| `localName` | `string` | Output only. The object name of the VMware OnPremAdminCluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |
| `platformConfig` | `object` | VmwarePlatformConfig represents configuration for the VMware platform. |
| `vcenter` | `object` | VmwareAdminVCenterConfig contains VCenter configuration for VMware admin cluster. |
| `createTime` | `string` | Output only. The time at which VMware admin cluster was created. |
| `bootstrapClusterMembership` | `string` | The bootstrap cluster this VMware admin cluster belongs to. |
| `loadBalancer` | `object` | VmwareAdminLoadBalancerConfig contains load balancer configuration for VMware admin cluster. |
| `endpoint` | `string` | Output only. The DNS name of VMware admin cluster's API server. |
| `reconciling` | `boolean` | Output only. If set, there are currently changes in flight to the VMware admin cluster. |
| `state` | `string` | Output only. The current state of VMware admin cluster. |
| `networkConfig` | `object` | VmwareAdminNetworkConfig contains network configuration for VMware admin cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_vmware_admin_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists VMware admin clusters in a given project and location. |
| `_projects_locations_vmware_admin_clusters_list` | `EXEC` | `locationsId, projectsId` | Lists VMware admin clusters in a given project and location. |
| `projects_locations_vmware_admin_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing VMware admin cluster to the Anthos On-Prem API within a given project and location. Through enrollment, an existing admin cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster will be expected to be performed through the API. |
| `projects_locations_vmware_admin_clusters_get` | `EXEC` | `locationsId, projectsId, vmwareAdminClustersId` | Gets details of a single VMware admin cluster. |
| `projects_locations_vmware_admin_clusters_patch` | `EXEC` | `locationsId, projectsId, vmwareAdminClustersId` | Updates the parameters of a single VMware admin cluster. |
| `projects_locations_vmware_admin_clusters_unenroll` | `EXEC` | `locationsId, projectsId, vmwareAdminClustersId` | Unenrolls an existing VMware admin cluster from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |
