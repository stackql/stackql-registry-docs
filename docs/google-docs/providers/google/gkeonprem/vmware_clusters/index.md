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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vmware_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.vmware_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The VMware user cluster resource name. |
| `description` | `string` | A human readable description of this VMware user cluster. |
| `endpoint` | `string` | Output only. The DNS name of VMware user cluster's API server. |
| `upgradePolicy` | `object` | VmwareClusterUpgradePolicy defines the cluster upgrade policy. |
| `status` | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| `deleteTime` | `string` | Output only. The time at which VMware user cluster was deleted. |
| `storage` | `object` | Specifies vSphere CSI components deployment config in the VMware user cluster. |
| `updateTime` | `string` | Output only. The time at which VMware user cluster was last updated. |
| `autoRepairConfig` | `object` | Specifies config to enable/disable auto repair. The cluster-health-controller is deployed only if Enabled is true. |
| `enableControlPlaneV2` | `boolean` | Enable control plane V2. Default to false. |
| `onPremVersion` | `string` | Required. The Anthos clusters on the VMware version for your user cluster. |
| `annotations` | `object` | Annotations on the VMware user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `validationCheck` | `object` | ValidationCheck represents the result of preflight check. |
| `uid` | `string` | Output only. The unique identifier of the VMware user cluster. |
| `adminClusterMembership` | `string` | Required. The admin cluster this VMware user cluster belongs to. This is the full resource name of the admin cluster's fleet membership. In the future, references to other resource types might be allowed if admin clusters are modeled as their own resources. |
| `authorization` | `object` | Authorization defines the On-Prem cluster authorization configuration to bootstrap onto the admin cluster. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| `antiAffinityGroups` | `object` | Specifies anti affinity group config for the VMware user cluster. |
| `loadBalancer` | `object` | Specifies the locad balancer config for the VMware user cluster. |
| `dataplaneV2` | `object` | Contains configurations for Dataplane V2, which is optimized dataplane for Kubernetes networking. For more information, see: https://cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2 |
| `localName` | `string` | Output only. The object name of the VMware OnPremUserCluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |
| `networkConfig` | `object` | Specifies network config for the VMware user cluster. |
| `adminClusterName` | `string` | Output only. The resource name of the VMware admin cluster hosting this user cluster. |
| `disableBundledIngress` | `boolean` | Disable bundled ingress. |
| `controlPlaneNode` | `object` | Specifies control plane node config for the VMware user cluster. |
| `vmTrackingEnabled` | `boolean` | Enable VM tracking. |
| `fleet` | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| `createTime` | `string` | Output only. The time at which VMware user cluster was created. |
| `vcenter` | `object` | Represents configuration for the VMware VCenter for the user cluster. |
| `state` | `string` | Output only. The current state of VMware user cluster. |
| `reconciling` | `boolean` | Output only. If set, there are currently changes in flight to the VMware user cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_vmware_clusters_get` | `SELECT` | `locationsId, projectsId, vmwareClustersId` | Gets details of a single VMware Cluster. |
| `projects_locations_vmware_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists VMware Clusters in a given project and location. |
| `projects_locations_vmware_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a new VMware user cluster in a given project and location. |
| `projects_locations_vmware_clusters_delete` | `DELETE` | `locationsId, projectsId, vmwareClustersId` | Deletes a single VMware Cluster. |
| `_projects_locations_vmware_clusters_list` | `EXEC` | `locationsId, projectsId` | Lists VMware Clusters in a given project and location. |
| `projects_locations_vmware_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing VMware user cluster and its node pools to the Anthos On-Prem API within a given project and location. Through enrollment, an existing cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster and/or its node pools will be expected to be performed through the API. |
| `projects_locations_vmware_clusters_patch` | `EXEC` | `locationsId, projectsId, vmwareClustersId` | Updates the parameters of a single VMware cluster. |
| `projects_locations_vmware_clusters_query_version_config` | `EXEC` | `locationsId, projectsId` | Queries the VMware user cluster version config. |
| `projects_locations_vmware_clusters_unenroll` | `EXEC` | `locationsId, projectsId, vmwareClustersId` | Unenrolls an existing VMware user cluster and its node pools from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters and node pools will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or UI. |
