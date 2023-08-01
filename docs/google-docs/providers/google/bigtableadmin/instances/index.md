---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - bigtableadmin
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | DEPRECATED: This field is unused and ignored. |
| `failedLocations` | `array` | Locations from which Instance information could not be retrieved, due to an outage or some other transient condition. Instances whose Clusters are all in one of the failed locations may be missing from `instances`, and Instances with at least one Cluster in a failed location may only have partial information returned. Values are of the form `projects//locations/` |
| `instances` | `array` | The list of requested instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, projectsId` | Gets information about an instance. |
| `list` | `SELECT` | `projectsId` | Lists information about instances in a project. |
| `create` | `INSERT` | `projectsId` | Create an instance within a project. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled. |
| `delete` | `DELETE` | `instancesId, projectsId` | Delete an instance from a project. |
| `partial_update_instance` | `EXEC` | `instancesId, projectsId` | Partially updates an instance within a project. This method can modify all fields of an Instance and is the preferred way to update an Instance. |
| `update` | `EXEC` | `instancesId, projectsId` | Updates an instance within a project. This method updates only the display name and type for an Instance. To update other Instance properties, such as labels, use PartialUpdateInstance. |
