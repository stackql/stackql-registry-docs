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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bare_metal_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.bare_metal_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The bare metal user cluster resource name. |
| `description` | `string` | A human readable description of this bare metal user cluster. |
| `upgradePolicy` | `object` | BareMetalClusterUpgradePolicy defines the cluster upgrade policy. |
| `uid` | `string` | Output only. The unique identifier of the bare metal user cluster. |
| `controlPlane` | `object` | Specifies the control plane configuration. |
| `nodeConfig` | `object` | Specifies the workload node configurations. |
| `state` | `string` | Output only. The current state of the bare metal user cluster. |
| `reconciling` | `boolean` | Output only. If set, there are currently changes in flight to the bare metal user cluster. |
| `storage` | `object` | BareMetalStorageConfig specifies the cluster storage configuration. |
| `proxy` | `object` | Specifies the cluster proxy configuration. |
| `clusterOperations` | `object` | Specifies the bare metal user cluster's observability infrastructure. |
| `osEnvironmentConfig` | `object` | Specifies operating system settings for cluster provisioning. |
| `securityConfig` | `object` | Specifies the security related settings for the bare metal user cluster. |
| `maintenanceStatus` | `object` | Represents the maintenance status of the bare metal user cluster. |
| `status` | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| `binaryAuthorization` | `object` | Configuration for Binary Authorization. |
| `adminClusterName` | `string` | Output only. The resource name of the bare metal admin cluster managing this user cluster. |
| `createTime` | `string` | Output only. The time when the bare metal user cluster was created. |
| `maintenanceConfig` | `object` | Specifies configurations to put bare metal nodes in and out of maintenance. |
| `localName` | `string` | Output only. The object name of the bare metal user cluster custom resource on the associated admin cluster. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the name in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. When the local name and cluster name differ, the local name is used in the admin cluster controller logs. You use the cluster name when accessing the cluster using bmctl and kubectl. |
| `loadBalancer` | `object` | Specifies the load balancer configuration. |
| `annotations` | `object` | Annotations on the bare metal user cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `adminClusterMembership` | `string` | Required. The admin cluster this bare metal user cluster belongs to. This is the full resource name of the admin cluster's fleet membership. |
| `updateTime` | `string` | Output only. The time when the bare metal user cluster was last updated. |
| `validationCheck` | `object` | ValidationCheck represents the result of preflight check. |
| `fleet` | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| `nodeAccessConfig` | `object` | Specifies the node access related settings for the bare metal user cluster. |
| `bareMetalVersion` | `string` | Required. The Anthos clusters on bare metal version for your user cluster. |
| `endpoint` | `string` | Output only. The IP address of the bare metal user cluster's API server. |
| `deleteTime` | `string` | Output only. The time when the bare metal user cluster was deleted. If the resource is not deleted, this must be empty |
| `etag` | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| `networkConfig` | `object` | Specifies the cluster network configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bare_metal_clusters_get` | `SELECT` | `bareMetalClustersId, locationsId, projectsId` | Gets details of a single bare metal Cluster. |
| `projects_locations_bare_metal_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists bare metal clusters in a given project and location. |
| `projects_locations_bare_metal_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a new bare metal cluster in a given project and location. |
| `projects_locations_bare_metal_clusters_delete` | `DELETE` | `bareMetalClustersId, locationsId, projectsId` | Deletes a single bare metal Cluster. |
| `_projects_locations_bare_metal_clusters_list` | `EXEC` | `locationsId, projectsId` | Lists bare metal clusters in a given project and location. |
| `projects_locations_bare_metal_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing bare metal user cluster and its node pools to the Anthos On-Prem API within a given project and location. Through enrollment, an existing cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster and/or its node pools will be expected to be performed through the API. |
| `projects_locations_bare_metal_clusters_patch` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Updates the parameters of a single bare metal Cluster. |
| `projects_locations_bare_metal_clusters_query_version_config` | `EXEC` | `locationsId, projectsId` | Queries the bare metal user cluster version config. |
| `projects_locations_bare_metal_clusters_unenroll` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Unenrolls an existing bare metal user cluster and its node pools from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters and node pools will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |
