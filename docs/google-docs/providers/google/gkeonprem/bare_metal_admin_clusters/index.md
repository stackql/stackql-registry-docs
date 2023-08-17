---
title: bare_metal_admin_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_admin_clusters
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
<tr><td><b>Name</b></td><td><code>bare_metal_admin_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.bare_metal_admin_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The bare metal admin cluster resource name. |
| `description` | `string` | A human readable description of this bare metal admin cluster. |
| `storage` | `object` | BareMetalAdminStorageConfig specifies the cluster storage configuration. |
| `networkConfig` | `object` | BareMetalAdminNetworkConfig specifies the cluster network configuration. |
| `reconciling` | `boolean` | Output only. If set, there are currently changes in flight to the bare metal Admin Cluster. |
| `validationCheck` | `object` | ValidationCheck represents the result of preflight check. |
| `nodeConfig` | `object` | BareMetalAdminWorkloadNodeConfig specifies the workload node configurations. |
| `localName` | `string` | Output only. The object name of the bare metal cluster custom resource. This field is used to support conflicting names when enrolling existing clusters to the API. When used as a part of cluster enrollment, this field will differ from the ID in the resource name. For new clusters, this field will match the user provided cluster name and be visible in the last component of the resource name. It is not modifiable. All users should use this name to access their cluster using gkectl or kubectl and should expect to see the local name when viewing admin cluster controller logs. |
| `endpoint` | `string` | Output only. The IP address name of bare metal admin cluster's API server. |
| `proxy` | `object` | BareMetalAdminProxyConfig specifies the cluster proxy configuration. |
| `controlPlane` | `object` | BareMetalAdminControlPlaneConfig specifies the control plane configuration. |
| `deleteTime` | `string` | Output only. The time at which this bare metal admin cluster was deleted. If the resource is not deleted, this must be empty |
| `uid` | `string` | Output only. The unique identifier of the bare metal admin cluster. |
| `annotations` | `object` | Annotations on the bare metal admin cluster. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `updateTime` | `string` | Output only. The time at which this bare metal admin cluster was last updated. |
| `fleet` | `object` | Fleet related configuration. Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems. See [Anthos Fleets](`https://cloud.google.com/anthos/multicluster-management/fleets`) for more details on Anthos multi-cluster capabilities using Fleets. ## |
| `securityConfig` | `object` | Specifies the security related settings for the bare metal admin cluster. |
| `nodeAccessConfig` | `object` | Specifies the node access related settings for the bare metal admin cluster. |
| `state` | `string` | Output only. The current state of the bare metal admin cluster. |
| `bareMetalVersion` | `string` | The Anthos clusters on bare metal version for the bare metal admin cluster. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| `maintenanceStatus` | `object` | BareMetalAdminMaintenanceStatus represents the maintenance status for bare metal Admin cluster CR's nodes. |
| `status` | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| `clusterOperations` | `object` | BareMetalAdminClusterOperationsConfig specifies the admin cluster's observability infrastructure. |
| `createTime` | `string` | Output only. The time at which this bare metal admin cluster was created. |
| `maintenanceConfig` | `object` | BareMetalAdminMaintenanceConfig specifies configurations to put bare metal Admin cluster CRs nodes in and out of maintenance. |
| `loadBalancer` | `object` | BareMetalAdminLoadBalancerConfig specifies the load balancer configuration. |
| `osEnvironmentConfig` | `object` | Specifies operating system operation settings for cluster provisioning. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bare_metal_admin_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists bare metal admin clusters in a given project and location. |
| `projects_locations_bare_metal_admin_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a new bare metal admin cluster in a given project and location. The API needs to be combined with creating a bootstrap cluster to work. See: https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-admin-cluster-api#prepare_bootstrap_environment |
| `_projects_locations_bare_metal_admin_clusters_list` | `EXEC` | `locationsId, projectsId` | Lists bare metal admin clusters in a given project and location. |
| `projects_locations_bare_metal_admin_clusters_enroll` | `EXEC` | `locationsId, projectsId` | Enrolls an existing bare metal admin cluster to the Anthos On-Prem API within a given project and location. Through enrollment, an existing admin cluster will become Anthos On-Prem API managed. The corresponding GCP resources will be created and all future modifications to the cluster will be expected to be performed through the API. |
| `projects_locations_bare_metal_admin_clusters_get` | `EXEC` | `bareMetalAdminClustersId, locationsId, projectsId` | Gets details of a single bare metal admin cluster. |
| `projects_locations_bare_metal_admin_clusters_patch` | `EXEC` | `bareMetalAdminClustersId, locationsId, projectsId` | Updates the parameters of a single bare metal admin cluster. |
| `projects_locations_bare_metal_admin_clusters_query_version_config` | `EXEC` | `locationsId, projectsId` | Queries the bare metal admin cluster version config. |
| `projects_locations_bare_metal_admin_clusters_unenroll` | `EXEC` | `bareMetalAdminClustersId, locationsId, projectsId` | Unenrolls an existing bare metal admin cluster from the Anthos On-Prem API within a given project and location. Unenrollment removes the Cloud reference to the cluster without modifying the underlying OnPrem Resources. Clusters will continue to run; however, they will no longer be accessible through the Anthos On-Prem API or its clients. |
