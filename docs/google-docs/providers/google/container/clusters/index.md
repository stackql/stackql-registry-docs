---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - container
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. Unique id for the cluster. |
| `name` | `string` | The name of this cluster. The name must be unique within this project and location (e.g. zone or region), and can be up to 40 characters with the following restrictions: * Lowercase letters, numbers, and hyphens only. * Must start with a letter. * Must end with a number or a letter. |
| `description` | `string` | An optional description of this cluster. |
| `nodeConfig` | `object` | Parameters that describe the nodes in a cluster. GKE Autopilot clusters do not recognize parameters in `NodeConfig`. Use AutoprovisioningNodePoolDefaults instead. |
| `authenticatorGroupsConfig` | `object` | Configuration for returning group information from authenticators. |
| `autoscaling` | `object` | ClusterAutoscaling contains global, per-cluster information required by Cluster Autoscaler to automatically adjust the size of the cluster and create/delete node pools based on the current needs. |
| `labelFingerprint` | `string` | The fingerprint of the set of labels for this cluster. |
| `expireTime` | `string` | [Output only] The time the cluster will be automatically deleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `masterAuth` | `object` | The authentication information for accessing the master endpoint. Authentication can be done using HTTP basic auth or using client certificates. |
| `currentNodeCount` | `integer` | [Output only] The number of nodes currently in the cluster. Deprecated. Call Kubernetes API directly to retrieve node information. |
| `enableKubernetesAlpha` | `boolean` | Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes. The cluster has no SLA for uptime and master/node upgrades are disabled. Alpha enabled clusters are automatically deleted thirty days after creation. |
| `currentNodeVersion` | `string` | [Output only] Deprecated, use [NodePools.version](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) instead. The current version of the node software components. If they are currently at multiple versions because they're in the process of being upgraded, this reflects the minimum version of all nodes. |
| `autopilot` | `object` | Autopilot is the configuration for Autopilot settings on the cluster. |
| `currentMasterVersion` | `string` | [Output only] The current software version of the master endpoint. |
| `identityServiceConfig` | `object` | IdentityServiceConfig is configuration for Identity Service which allows customers to use external identity providers with the K8S API |
| `loggingConfig` | `object` | LoggingConfig is cluster logging configuration. |
| `nodePoolDefaults` | `object` | Subset of Nodepool message that has defaults. |
| `location` | `string` | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |
| `loggingService` | `string` | The logging service the cluster should use to write logs. Currently available options: * `logging.googleapis.com/kubernetes` - The Cloud Logging service with a Kubernetes-native resource model * `logging.googleapis.com` - The legacy Cloud Logging service (no longer available as of GKE 1.15). * `none` - no logs will be exported from the cluster. If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions. |
| `status` | `string` | [Output only] The current status of this cluster. |
| `servicesIpv4Cidr` | `string` | [Output only] The IP address range of the Kubernetes services in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last `/16` from the container CIDR. |
| `subnetwork` | `string` | The name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/subnetworks) to which the cluster is connected. |
| `locations` | `array` | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation. Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed. |
| `enableTpu` | `boolean` | Enable the ability to use Cloud TPUs in this cluster. |
| `clusterIpv4Cidr` | `string` | The IP address range of the container pods in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`). Leave blank to have one automatically chosen or specify a `/14` block in `10.0.0.0/8`. |
| `nodeIpv4CidrSize` | `integer` | [Output only] The size of the address space on each node for hosting containers. This is provisioned from within the `container_ipv4_cidr` range. This field will only be set when cluster is in route-based network mode. |
| `databaseEncryption` | `object` | Configuration of etcd encryption. |
| `verticalPodAutoscaling` | `object` | VerticalPodAutoscaling contains global, per-cluster information required by Vertical Pod Autoscaler to automatically adjust the resources of pods controlled by it. |
| `tpuIpv4CidrBlock` | `string` | [Output only] The IP address range of the Cloud TPUs in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). |
| `shieldedNodes` | `object` | Configuration of Shielded Nodes feature. |
| `resourceUsageExportConfig` | `object` | Configuration for exporting cluster resource usages. |
| `masterAuthorizedNetworksConfig` | `object` | Configuration options for the master authorized networks feature. Enabled master authorized networks will disallow all external traffic to access Kubernetes master through HTTPS except traffic from the given CIDR blocks, Google Compute Engine Public IPs and Google Prod IPs. |
| `defaultMaxPodsConstraint` | `object` | Constraints applied to pods. |
| `maintenancePolicy` | `object` | MaintenancePolicy defines the maintenance policy to be used for the cluster. |
| `instanceGroupUrls` | `array` | Deprecated. Use node_pools.instance_group_urls. |
| `conditions` | `array` | Which conditions caused the current cluster state. |
| `networkConfig` | `object` | NetworkConfig reports the relative names of network & subnetwork. |
| `nodePoolAutoConfig` | `object` | Node pool configs that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. |
| `privateClusterConfig` | `object` | Configuration options for private clusters. |
| `network` | `string` | The name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. If left unspecified, the `default` network will be used. |
| `nodePools` | `array` | The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified. |
| `addonsConfig` | `object` | Configuration for the addons that can be automatically spun up in the cluster, enabling additional functionality. |
| `notificationConfig` | `object` | NotificationConfig is the configuration of notifications. |
| `meshCertificates` | `object` | Configuration for issuance of mTLS keys and certificates to Kubernetes pods. |
| `selfLink` | `string` | [Output only] Server-defined URL for the resource. |
| `zone` | `string` | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field is deprecated, use location instead. |
| `initialNodeCount` | `integer` | The number of nodes to create in this cluster. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "node_config") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. This field is deprecated, use node_pool.initial_node_count instead. |
| `binaryAuthorization` | `object` | Configuration for Binary Authorization. |
| `createTime` | `string` | [Output only] The time the cluster was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| `legacyAbac` | `object` | Configuration for the legacy Attribute Based Access Control authorization mode. |
| `networkPolicy` | `object` | Configuration options for the NetworkPolicy feature. https://kubernetes.io/docs/concepts/services-networking/networkpolicies/ |
| `statusMessage` | `string` | [Output only] Deprecated. Use conditions instead. Additional information about the current status of this cluster, if available. |
| `endpoint` | `string` | [Output only] The IP address of this cluster's master endpoint. The endpoint can be accessed from the internet at `https://username:password@endpoint/`. See the `masterAuth` property of this resource for username and password information. |
| `confidentialNodes` | `object` | ConfidentialNodes is configuration for the confidential nodes feature, which makes nodes run on confidential VMs. |
| `ipAllocationPolicy` | `object` | Configuration for controlling how IPs are allocated in the cluster. |
| `initialClusterVersion` | `string` | The initial Kubernetes version for this cluster. Valid versions are those found in validMasterVersions returned by getServerConfig. The version can be upgraded over time; such upgrades are reflected in currentMasterVersion and currentNodeVersion. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "","-": picks the default Kubernetes version |
| `monitoringService` | `string` | The monitoring service the cluster should use to write metrics. Currently available options: * "monitoring.googleapis.com/kubernetes" - The Cloud Monitoring service with a Kubernetes-native resource model * `monitoring.googleapis.com` - The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * `none` - No metrics will be exported from the cluster. If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions. |
| `monitoringConfig` | `object` | MonitoringConfig is cluster monitoring configuration. |
| `workloadIdentityConfig` | `object` | Configuration for the use of Kubernetes Service Accounts in GCP IAM policies. |
| `releaseChannel` | `object` | ReleaseChannel indicates which release channel a cluster is subscribed to. Release channels are arranged in order of risk. When a cluster is subscribed to a release channel, Google maintains both the master version and the node version. Node auto-upgrade defaults to true and cannot be disabled. |
| `resourceLabels` | `object` | The resource labels for the cluster to use to annotate any related Google Compute Engine resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_clusters_get` | `SELECT` | `clustersId, locationsId, projectsId` | Gets the details of a specific cluster. |
| `projects_locations_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists all clusters owned by a project in either the specified zone or all zones. |
| `projects_zones_clusters_get` | `SELECT` | `clusterId, projectId, zone` | Gets the details of a specific cluster. |
| `projects_zones_clusters_list` | `SELECT` | `projectId, zone` | Lists all clusters owned by a project in either the specified zone or all zones. |
| `projects_locations_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| `projects_zones_clusters_create` | `INSERT` | `projectId, zone` | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| `projects_locations_clusters_delete` | `DELETE` | `clustersId, locationsId, projectsId` | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| `projects_zones_clusters_delete` | `DELETE` | `clusterId, projectId, zone` | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| `projects_locations_clusters_completeIpRotation` | `EXEC` | `clustersId, locationsId, projectsId` | Completes master IP rotation. |
| `projects_locations_clusters_setAddons` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the addons for a specific cluster. |
| `projects_locations_clusters_setLegacyAbac` | `EXEC` | `clustersId, locationsId, projectsId` | Enables or disables the ABAC authorization mechanism on a cluster. |
| `projects_locations_clusters_setLocations` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| `projects_locations_clusters_setLogging` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the logging service for a specific cluster. |
| `projects_locations_clusters_setMaintenancePolicy` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the maintenance policy for a cluster. |
| `projects_locations_clusters_setMasterAuth` | `EXEC` | `clustersId, locationsId, projectsId` | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| `projects_locations_clusters_setMonitoring` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the monitoring service for a specific cluster. |
| `projects_locations_clusters_setNetworkPolicy` | `EXEC` | `clustersId, locationsId, projectsId` | Enables or disables Network Policy for a cluster. |
| `projects_locations_clusters_setResourceLabels` | `EXEC` | `clustersId, locationsId, projectsId` | Sets labels on a cluster. |
| `projects_locations_clusters_startIpRotation` | `EXEC` | `clustersId, locationsId, projectsId` | Starts master IP rotation. |
| `projects_locations_clusters_update` | `EXEC` | `clustersId, locationsId, projectsId` | Updates the settings of a specific cluster. |
| `projects_locations_clusters_updateMaster` | `EXEC` | `clustersId, locationsId, projectsId` | Updates the master for a specific cluster. |
| `projects_zones_clusters_completeIpRotation` | `EXEC` | `clusterId, projectId, zone` | Completes master IP rotation. |
| `projects_zones_clusters_legacyAbac` | `EXEC` | `clusterId, projectId, zone` | Enables or disables the ABAC authorization mechanism on a cluster. |
| `projects_zones_clusters_locations` | `EXEC` | `clusterId, projectId, zone` | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| `projects_zones_clusters_logging` | `EXEC` | `clusterId, projectId, zone` | Sets the logging service for a specific cluster. |
| `projects_zones_clusters_master` | `EXEC` | `clusterId, projectId, zone` | Updates the master for a specific cluster. |
| `projects_zones_clusters_monitoring` | `EXEC` | `clusterId, projectId, zone` | Sets the monitoring service for a specific cluster. |
| `projects_zones_clusters_resourceLabels` | `EXEC` | `clusterId, projectId, zone` | Sets labels on a cluster. |
| `projects_zones_clusters_setMaintenancePolicy` | `EXEC` | `clusterId, projectId, zone` | Sets the maintenance policy for a cluster. |
| `projects_zones_clusters_setMasterAuth` | `EXEC` | `clusterId, projectId, zone` | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| `projects_zones_clusters_setNetworkPolicy` | `EXEC` | `clusterId, projectId, zone` | Enables or disables Network Policy for a cluster. |
| `projects_zones_clusters_startIpRotation` | `EXEC` | `clusterId, projectId, zone` | Starts master IP rotation. |
| `projects_zones_clusters_update` | `EXEC` | `clusterId, projectId, zone` | Updates the settings of a specific cluster. |
