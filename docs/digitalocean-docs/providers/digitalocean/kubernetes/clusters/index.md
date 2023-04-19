---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - kubernetes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.kubernetes.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference a Kubernetes cluster. |
| `name` | `string` | A human-readable name for a Kubernetes cluster. |
| `version` | `string` | The slug identifier for the version of Kubernetes used for the cluster. If set to a minor version (e.g. "1.14"), the latest version within it will be used (e.g. "1.14.6-do.1"); if set to "latest", the latest published version will be used. See the `/v2/kubernetes/options` endpoint to find all currently available versions. |
| `ha` | `boolean` | A boolean value indicating whether the control plane is run in a highly available configuration in the cluster. Highly available control planes incur less downtime. The property cannot be disabled. |
| `registry_enabled` | `boolean` | A read-only boolean value indicating if a container registry is integrated with the cluster. |
| `ipv4` | `string` | The public IPv4 address of the Kubernetes master node. This will not be set if high availability is configured on the cluster (v1.21+) |
| `updated_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the Kubernetes cluster was last updated. |
| `status` | `object` | An object containing a `state` attribute whose value is set to a string indicating the current status of the cluster. |
| `service_subnet` | `string` | The range of assignable IP addresses for services running in the Kubernetes cluster in CIDR notation. |
| `tags` | `array` | An array of tags applied to the Kubernetes cluster. All clusters are automatically tagged `k8s` and `k8s:$K8S_CLUSTER_ID`. |
| `vpc_uuid` | `string` | A string specifying the UUID of the VPC to which the Kubernetes cluster is assigned. |
| `endpoint` | `string` | The base URL of the API server on the Kubernetes master node. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the Kubernetes cluster was created. |
| `node_pools` | `array` | An object specifying the details of the worker nodes available to the Kubernetes cluster. |
| `auto_upgrade` | `boolean` | A boolean value indicating whether the cluster will be automatically upgraded to new patch releases during its maintenance window. |
| `surge_upgrade` | `boolean` | A boolean value indicating whether surge upgrade is enabled/disabled for the cluster. Surge upgrade makes cluster upgrades fast and reliable by bringing up new nodes before destroying the outdated nodes. |
| `maintenance_policy` | `object` | An object specifying the maintenance window policy for the Kubernetes cluster. |
| `cluster_subnet` | `string` | The range of IP addresses in the overlay network of the Kubernetes cluster in CIDR notation. |
| `region` | `string` | The slug identifier for the region where the Kubernetes cluster is located. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_cluster` | `SELECT` | `cluster_id` | To show information about an existing Kubernetes cluster, send a GET request<br />to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`.<br /> |
| `list_clusters` | `SELECT` |  | To list all of the Kubernetes clusters on your account, send a GET request<br />to `/v2/kubernetes/clusters`.<br /> |
| `create_cluster` | `INSERT` | `data__name, data__node_pools, data__region, data__version` | To create a new Kubernetes cluster, send a POST request to<br />`/v2/kubernetes/clusters`. The request must contain at least one node pool<br />with at least one worker.<br /><br />The request may contain a maintenance window policy describing a time period<br />when disruptive maintenance tasks may be carried out. Omitting the policy<br />implies that a window will be chosen automatically. See<br />[here](https://www.digitalocean.com/docs/kubernetes/how-to/upgrade-cluster/)<br />for details.<br /> |
| `delete_cluster` | `DELETE` | `cluster_id` | To delete a Kubernetes cluster and all services deployed to it, send a DELETE<br />request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`.<br /><br />A 204 status code with no body will be returned in response to a successful<br />request.<br /> |
| `_get_cluster` | `EXEC` | `cluster_id` | To show information about an existing Kubernetes cluster, send a GET request<br />to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`.<br /> |
| `_list_clusters` | `EXEC` |  | To list all of the Kubernetes clusters on your account, send a GET request<br />to `/v2/kubernetes/clusters`.<br /> |
| `destroy_associatedResourcesDangerous` | `EXEC` | `cluster_id` | To delete a Kubernetes cluster with all of its associated resources, send a<br />DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources/dangerous`.<br />A 204 status code with no body will be returned in response to a successful request.<br /> |
| `destroy_associatedResourcesSelective` | `EXEC` | `cluster_id` | To delete a Kubernetes cluster along with a subset of its associated resources,<br />send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources/selective`.<br /><br />The JSON body of the request should include `load_balancers`, `volumes`, or<br />`volume_snapshots` keys each set to an array of IDs for the associated<br />resources to be destroyed.<br /><br />The IDs can be found by querying the cluster's associated resources endpoint.<br />Any associated resource not included in the request will remain and continue<br />to accrue changes on your account.<br /> |
| `get_kubeconfig` | `EXEC` | `cluster_id` | This endpoint returns a kubeconfig file in YAML format. It can be used to<br />connect to and administer the cluster using the Kubernetes command line tool,<br />`kubectl`, or other programs supporting kubeconfig files (e.g., client libraries).<br /><br />The resulting kubeconfig file uses token-based authentication for clusters<br />supporting it, and certificate-based authentication otherwise. For a list of<br />supported versions and more information, see "[How to Connect to a DigitalOcean<br />Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)".<br /><br />To retrieve a kubeconfig file for use with a Kubernetes cluster, send a GET<br />request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig`.<br /><br />Clusters supporting token-based authentication may define an expiration by<br />passing a duration in seconds as a query parameter to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`.<br />If not set or 0, then the token will have a 7 day expiry. The query parameter<br />has no impact in certificate-based authentication.<br /> |
| `list_associatedResources` | `EXEC` | `cluster_id` | To list the associated billable resources that can be destroyed along with a cluster, send a GET request to the `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources` endpoint. |
| `update_cluster` | `EXEC` | `cluster_id, data__name` | To update a Kubernetes cluster, send a PUT request to<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID` and specify one or more of the<br />attributes below.<br /> |
| `upgrade_cluster` | `EXEC` | `cluster_id` | To immediately upgrade a Kubernetes cluster to a newer patch release of<br />Kubernetes, send a POST request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrade`.<br />The body of the request must specify a version attribute.<br /><br />Available upgrade versions for a cluster can be fetched from<br />`/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`.<br /> |
