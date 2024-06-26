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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. Unique id for the cluster. |
| <CopyableCode code="name" /> | `string` | The name of this cluster. The name must be unique within this project and location (e.g. zone or region), and can be up to 40 characters with the following restrictions: * Lowercase letters, numbers, and hyphens only. * Must start with a letter. * Must end with a number or a letter. |
| <CopyableCode code="description" /> | `string` | An optional description of this cluster. |
| <CopyableCode code="addonsConfig" /> | `object` | Configuration for the addons that can be automatically spun up in the cluster, enabling additional functionality. |
| <CopyableCode code="authenticatorGroupsConfig" /> | `object` | Configuration for returning group information from authenticators. |
| <CopyableCode code="autopilot" /> | `object` | Autopilot is the configuration for Autopilot settings on the cluster. |
| <CopyableCode code="autoscaling" /> | `object` | ClusterAutoscaling contains global, per-cluster information required by Cluster Autoscaler to automatically adjust the size of the cluster and create/delete node pools based on the current needs. |
| <CopyableCode code="binaryAuthorization" /> | `object` | Configuration for Binary Authorization. |
| <CopyableCode code="clusterIpv4Cidr" /> | `string` | The IP address range of the container pods in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`). Leave blank to have one automatically chosen or specify a `/14` block in `10.0.0.0/8`. |
| <CopyableCode code="conditions" /> | `array` | Which conditions caused the current cluster state. |
| <CopyableCode code="confidentialNodes" /> | `object` | ConfidentialNodes is configuration for the confidential nodes feature, which makes nodes run on confidential VMs. |
| <CopyableCode code="costManagementConfig" /> | `object` | Configuration for fine-grained cost management feature. |
| <CopyableCode code="createTime" /> | `string` | [Output only] The time the cluster was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="currentMasterVersion" /> | `string` | [Output only] The current software version of the master endpoint. |
| <CopyableCode code="currentNodeCount" /> | `integer` | [Output only] The number of nodes currently in the cluster. Deprecated. Call Kubernetes API directly to retrieve node information. |
| <CopyableCode code="currentNodeVersion" /> | `string` | [Output only] Deprecated, use [NodePools.version](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) instead. The current version of the node software components. If they are currently at multiple versions because they're in the process of being upgraded, this reflects the minimum version of all nodes. |
| <CopyableCode code="databaseEncryption" /> | `object` | Configuration of etcd encryption. |
| <CopyableCode code="defaultMaxPodsConstraint" /> | `object` | Constraints applied to pods. |
| <CopyableCode code="enableK8sBetaApis" /> | `object` | K8sBetaAPIConfig , configuration for beta APIs |
| <CopyableCode code="enableKubernetesAlpha" /> | `boolean` | Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes. The cluster has no SLA for uptime and master/node upgrades are disabled. Alpha enabled clusters are automatically deleted thirty days after creation. |
| <CopyableCode code="enableTpu" /> | `boolean` | Enable the ability to use Cloud TPUs in this cluster. |
| <CopyableCode code="endpoint" /> | `string` | [Output only] The IP address of this cluster's master endpoint. The endpoint can be accessed from the internet at `https://username:password@endpoint/`. See the `masterAuth` property of this resource for username and password information. |
| <CopyableCode code="enterpriseConfig" /> | `object` | EnterpriseConfig is the cluster enterprise configuration. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of cluster fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="expireTime" /> | `string` | [Output only] The time the cluster will be automatically deleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="fleet" /> | `object` | Fleet is the fleet configuration for the cluster. |
| <CopyableCode code="identityServiceConfig" /> | `object` | IdentityServiceConfig is configuration for Identity Service which allows customers to use external identity providers with the K8S API |
| <CopyableCode code="initialClusterVersion" /> | `string` | The initial Kubernetes version for this cluster. Valid versions are those found in validMasterVersions returned by getServerConfig. The version can be upgraded over time; such upgrades are reflected in currentMasterVersion and currentNodeVersion. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "","-": picks the default Kubernetes version |
| <CopyableCode code="initialNodeCount" /> | `integer` | The number of nodes to create in this cluster. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "node_config") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. This field is deprecated, use node_pool.initial_node_count instead. |
| <CopyableCode code="instanceGroupUrls" /> | `array` | Deprecated. Use node_pools.instance_group_urls. |
| <CopyableCode code="ipAllocationPolicy" /> | `object` | Configuration for controlling how IPs are allocated in the cluster. |
| <CopyableCode code="labelFingerprint" /> | `string` | The fingerprint of the set of labels for this cluster. |
| <CopyableCode code="legacyAbac" /> | `object` | Configuration for the legacy Attribute Based Access Control authorization mode. |
| <CopyableCode code="location" /> | `string` | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides. |
| <CopyableCode code="locations" /> | `array` | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation. Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed. |
| <CopyableCode code="loggingConfig" /> | `object` | LoggingConfig is cluster logging configuration. |
| <CopyableCode code="loggingService" /> | `string` | The logging service the cluster should use to write logs. Currently available options: * `logging.googleapis.com/kubernetes` - The Cloud Logging service with a Kubernetes-native resource model * `logging.googleapis.com` - The legacy Cloud Logging service (no longer available as of GKE 1.15). * `none` - no logs will be exported from the cluster. If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions. |
| <CopyableCode code="maintenancePolicy" /> | `object` | MaintenancePolicy defines the maintenance policy to be used for the cluster. |
| <CopyableCode code="masterAuth" /> | `object` | The authentication information for accessing the master endpoint. Authentication can be done using HTTP basic auth or using client certificates. |
| <CopyableCode code="masterAuthorizedNetworksConfig" /> | `object` | Configuration options for the master authorized networks feature. Enabled master authorized networks will disallow all external traffic to access Kubernetes master through HTTPS except traffic from the given CIDR blocks, Google Compute Engine Public IPs and Google Prod IPs. |
| <CopyableCode code="meshCertificates" /> | `object` | Configuration for issuance of mTLS keys and certificates to Kubernetes pods. |
| <CopyableCode code="monitoringConfig" /> | `object` | MonitoringConfig is cluster monitoring configuration. |
| <CopyableCode code="monitoringService" /> | `string` | The monitoring service the cluster should use to write metrics. Currently available options: * "monitoring.googleapis.com/kubernetes" - The Cloud Monitoring service with a Kubernetes-native resource model * `monitoring.googleapis.com` - The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * `none` - No metrics will be exported from the cluster. If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions. |
| <CopyableCode code="network" /> | `string` | The name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. If left unspecified, the `default` network will be used. |
| <CopyableCode code="networkConfig" /> | `object` | NetworkConfig reports the relative names of network & subnetwork. |
| <CopyableCode code="networkPolicy" /> | `object` | Configuration options for the NetworkPolicy feature. https://kubernetes.io/docs/concepts/services-networking/networkpolicies/ |
| <CopyableCode code="nodeConfig" /> | `object` | Parameters that describe the nodes in a cluster. GKE Autopilot clusters do not recognize parameters in `NodeConfig`. Use AutoprovisioningNodePoolDefaults instead. |
| <CopyableCode code="nodeIpv4CidrSize" /> | `integer` | [Output only] The size of the address space on each node for hosting containers. This is provisioned from within the `container_ipv4_cidr` range. This field will only be set when cluster is in route-based network mode. |
| <CopyableCode code="nodePoolAutoConfig" /> | `object` | Node pool configs that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. |
| <CopyableCode code="nodePoolDefaults" /> | `object` | Subset of Nodepool message that has defaults. |
| <CopyableCode code="nodePools" /> | `array` | The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified. |
| <CopyableCode code="notificationConfig" /> | `object` | NotificationConfig is the configuration of notifications. |
| <CopyableCode code="parentProductConfig" /> | `object` | ParentProductConfig is the configuration of the parent product of the cluster. This field is used by Google internal products that are built on top of a GKE cluster and take the ownership of the cluster. |
| <CopyableCode code="privateClusterConfig" /> | `object` | Configuration options for private clusters. |
| <CopyableCode code="releaseChannel" /> | `object` | ReleaseChannel indicates which release channel a cluster is subscribed to. Release channels are arranged in order of risk. When a cluster is subscribed to a release channel, Google maintains both the master version and the node version. Node auto-upgrade defaults to true and cannot be disabled. |
| <CopyableCode code="resourceLabels" /> | `object` | The resource labels for the cluster to use to annotate any related Google Compute Engine resources. |
| <CopyableCode code="resourceUsageExportConfig" /> | `object` | Configuration for exporting cluster resource usages. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="securityPostureConfig" /> | `object` | SecurityPostureConfig defines the flags needed to enable/disable features for the Security Posture API. |
| <CopyableCode code="selfLink" /> | `string` | [Output only] Server-defined URL for the resource. |
| <CopyableCode code="servicesIpv4Cidr" /> | `string` | [Output only] The IP address range of the Kubernetes services in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last `/16` from the container CIDR. |
| <CopyableCode code="shieldedNodes" /> | `object` | Configuration of Shielded Nodes feature. |
| <CopyableCode code="status" /> | `string` | [Output only] The current status of this cluster. |
| <CopyableCode code="statusMessage" /> | `string` | [Output only] Deprecated. Use conditions instead. Additional information about the current status of this cluster, if available. |
| <CopyableCode code="subnetwork" /> | `string` | The name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/subnetworks) to which the cluster is connected. |
| <CopyableCode code="tpuIpv4CidrBlock" /> | `string` | [Output only] The IP address range of the Cloud TPUs in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). |
| <CopyableCode code="verticalPodAutoscaling" /> | `object` | VerticalPodAutoscaling contains global, per-cluster information required by Vertical Pod Autoscaler to automatically adjust the resources of pods controlled by it. |
| <CopyableCode code="workloadIdentityConfig" /> | `object` | Configuration for the use of Kubernetes Service Accounts in GCP IAM policies. |
| <CopyableCode code="zone" /> | `string` | [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field is deprecated, use location instead. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_clusters_get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Gets the details of a specific cluster. |
| <CopyableCode code="projects_locations_clusters_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all clusters owned by a project in either the specified zone or all zones. |
| <CopyableCode code="projects_zones_clusters_get" /> | `SELECT` | <CopyableCode code="clusterId, projectId, zone" /> | Gets the details of a specific cluster. |
| <CopyableCode code="projects_zones_clusters_list" /> | `SELECT` | <CopyableCode code="projectId, zone" /> | Lists all clusters owned by a project in either the specified zone or all zones. |
| <CopyableCode code="projects_locations_clusters_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| <CopyableCode code="projects_zones_clusters_create" /> | `INSERT` | <CopyableCode code="projectId, zone" /> | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| <CopyableCode code="projects_locations_clusters_delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| <CopyableCode code="projects_zones_clusters_delete" /> | `DELETE` | <CopyableCode code="clusterId, projectId, zone" /> | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| <CopyableCode code="projects_locations_clusters_update" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Updates the settings of a specific cluster. |
| <CopyableCode code="projects_zones_clusters_update" /> | `UPDATE` | <CopyableCode code="clusterId, projectId, zone" /> | Updates the settings of a specific cluster. |
| <CopyableCode code="_projects_locations_clusters_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all clusters owned by a project in either the specified zone or all zones. |
| <CopyableCode code="projects_locations_clusters_check_autopilot_compatibility" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues. |
| <CopyableCode code="projects_locations_clusters_complete_ip_rotation" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Completes master IP rotation. |
| <CopyableCode code="projects_locations_clusters_set_addons" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets the addons for a specific cluster. |
| <CopyableCode code="projects_locations_clusters_set_legacy_abac" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Enables or disables the ABAC authorization mechanism on a cluster. |
| <CopyableCode code="projects_locations_clusters_set_locations" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| <CopyableCode code="projects_locations_clusters_set_logging" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets the logging service for a specific cluster. |
| <CopyableCode code="projects_locations_clusters_set_maintenance_policy" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets the maintenance policy for a cluster. |
| <CopyableCode code="projects_locations_clusters_set_master_auth" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| <CopyableCode code="projects_locations_clusters_set_monitoring" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets the monitoring service for a specific cluster. |
| <CopyableCode code="projects_locations_clusters_set_network_policy" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Enables or disables Network Policy for a cluster. |
| <CopyableCode code="projects_locations_clusters_set_resource_labels" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Sets labels on a cluster. |
| <CopyableCode code="projects_locations_clusters_start_ip_rotation" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Starts master IP rotation. |
| <CopyableCode code="projects_zones_clusters_complete_ip_rotation" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Completes master IP rotation. |
| <CopyableCode code="projects_zones_clusters_legacy_abac" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Enables or disables the ABAC authorization mechanism on a cluster. |
| <CopyableCode code="projects_zones_clusters_locations" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| <CopyableCode code="projects_zones_clusters_logging" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Sets the logging service for a specific cluster. |
| <CopyableCode code="projects_zones_clusters_master" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Updates the master for a specific cluster. |
| <CopyableCode code="projects_zones_clusters_monitoring" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Sets the monitoring service for a specific cluster. |
| <CopyableCode code="projects_zones_clusters_resource_labels" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Sets labels on a cluster. |
| <CopyableCode code="projects_zones_clusters_set_maintenance_policy" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Sets the maintenance policy for a cluster. |
| <CopyableCode code="projects_zones_clusters_set_master_auth" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| <CopyableCode code="projects_zones_clusters_set_network_policy" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Enables or disables Network Policy for a cluster. |
| <CopyableCode code="projects_zones_clusters_start_ip_rotation" /> | `EXEC` | <CopyableCode code="clusterId, projectId, zone" /> | Starts master IP rotation. |
