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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `clusters` | `array` | A list of clusters in the project in the specified zone, or across all ones. |
| `missingZones` | `array` | If any zones are listed here, the list of clusters returned may be missing those zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_clusters_list` | `SELECT` | `locationsId, projectsId` | Lists all clusters owned by a project in either the specified zone or all zones. |
| `projects_zones_clusters_list` | `SELECT` | `projectId, zone` | Lists all clusters owned by a project in either the specified zone or all zones. |
| `projects_locations_clusters_create` | `INSERT` | `locationsId, projectsId` | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| `projects_zones_clusters_create` | `INSERT` | `projectId, zone` | Creates a cluster, consisting of the specified number and type of Google Compute Engine instances. By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). One firewall is added for the cluster. After cluster creation, the Kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster. Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using. |
| `projects_locations_clusters_delete` | `DELETE` | `clustersId, locationsId, projectsId` | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| `projects_zones_clusters_delete` | `DELETE` | `clusterId, projectId, zone` | Deletes the cluster, including the Kubernetes endpoint and all worker nodes. Firewalls and routes that were configured during cluster creation are also deleted. Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created. |
| `projects_locations_clusters_check_autopilot_compatibility` | `EXEC` | `clustersId, locationsId, projectsId` | Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues. |
| `projects_locations_clusters_complete_ip_rotation` | `EXEC` | `clustersId, locationsId, projectsId` | Completes master IP rotation. |
| `projects_locations_clusters_get` | `EXEC` | `clustersId, locationsId, projectsId` | Gets the details of a specific cluster. |
| `projects_locations_clusters_set_addons` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the addons for a specific cluster. |
| `projects_locations_clusters_set_legacy_abac` | `EXEC` | `clustersId, locationsId, projectsId` | Enables or disables the ABAC authorization mechanism on a cluster. |
| `projects_locations_clusters_set_locations` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| `projects_locations_clusters_set_logging` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the logging service for a specific cluster. |
| `projects_locations_clusters_set_maintenance_policy` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the maintenance policy for a cluster. |
| `projects_locations_clusters_set_master_auth` | `EXEC` | `clustersId, locationsId, projectsId` | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| `projects_locations_clusters_set_monitoring` | `EXEC` | `clustersId, locationsId, projectsId` | Sets the monitoring service for a specific cluster. |
| `projects_locations_clusters_set_network_policy` | `EXEC` | `clustersId, locationsId, projectsId` | Enables or disables Network Policy for a cluster. |
| `projects_locations_clusters_set_resource_labels` | `EXEC` | `clustersId, locationsId, projectsId` | Sets labels on a cluster. |
| `projects_locations_clusters_start_ip_rotation` | `EXEC` | `clustersId, locationsId, projectsId` | Starts master IP rotation. |
| `projects_locations_clusters_update` | `EXEC` | `clustersId, locationsId, projectsId` | Updates the settings of a specific cluster. |
| `projects_zones_clusters_complete_ip_rotation` | `EXEC` | `clusterId, projectId, zone` | Completes master IP rotation. |
| `projects_zones_clusters_get` | `EXEC` | `clusterId, projectId, zone` | Gets the details of a specific cluster. |
| `projects_zones_clusters_legacy_abac` | `EXEC` | `clusterId, projectId, zone` | Enables or disables the ABAC authorization mechanism on a cluster. |
| `projects_zones_clusters_locations` | `EXEC` | `clusterId, projectId, zone` | Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/update) instead. |
| `projects_zones_clusters_logging` | `EXEC` | `clusterId, projectId, zone` | Sets the logging service for a specific cluster. |
| `projects_zones_clusters_master` | `EXEC` | `clusterId, projectId, zone` | Updates the master for a specific cluster. |
| `projects_zones_clusters_monitoring` | `EXEC` | `clusterId, projectId, zone` | Sets the monitoring service for a specific cluster. |
| `projects_zones_clusters_resource_labels` | `EXEC` | `clusterId, projectId, zone` | Sets labels on a cluster. |
| `projects_zones_clusters_set_maintenance_policy` | `EXEC` | `clusterId, projectId, zone` | Sets the maintenance policy for a cluster. |
| `projects_zones_clusters_set_master_auth` | `EXEC` | `clusterId, projectId, zone` | Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password. |
| `projects_zones_clusters_set_network_policy` | `EXEC` | `clusterId, projectId, zone` | Enables or disables Network Policy for a cluster. |
| `projects_zones_clusters_start_ip_rotation` | `EXEC` | `clusterId, projectId, zone` | Starts master IP rotation. |
| `projects_zones_clusters_update` | `EXEC` | `clusterId, projectId, zone` | Updates the settings of a specific cluster. |
