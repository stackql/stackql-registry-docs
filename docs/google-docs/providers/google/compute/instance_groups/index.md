---
title: instance_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_groups
  - compute
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
<tr><td><b>Name</b></td><td><code>instance_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this instance group, generated by the server. |
| `name` | `string` | The name of the instance group. The name must be 1-63 characters long, and comply with RFC1035. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `size` | `integer` | [Output Only] The total number of instances in the instance group. |
| `network` | `string` | [Output Only] The URL of the network to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0). |
| `selfLink` | `string` | [Output Only] The URL for this instance group. The server generates this URL. |
| `kind` | `string` | [Output Only] The resource type, which is always compute#instanceGroup for instance groups. |
| `fingerprint` | `string` | [Output Only] The fingerprint of the named ports. The system uses this fingerprint to detect conflicts when multiple users change the named ports concurrently. |
| `namedPorts` | `array` |  Assigns a name to a port number. For example: &#123;name: "http", port: 80&#125; This allows the system to reference ports by the assigned name instead of a port number. Named ports can also contain multiple ports. For example: [&#123;name: "app1", port: 8080&#125;, &#123;name: "app1", port: 8081&#125;, &#123;name: "app2", port: 8082&#125;] Named ports apply to all instances in this instance group.  |
| `subnetwork` | `string` | [Output Only] The URL of the subnetwork to which all instances in the instance group belong. If your instance has multiple network interfaces, then the network and subnetwork fields only refer to the network and subnet used by your primary interface (nic0). |
| `zone` | `string` | [Output Only] The URL of the zone where the instance group is located (for zonal resources). |
| `region` | `string` | [Output Only] The URL of the region where the instance group is located (for regional resources). |
| `creationTimestamp` | `string` | [Output Only] The creation timestamp for this instance group in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregated_list` | `SELECT` | `project` | Retrieves the list of instance groups and sorts them by zone. |
| `get` | `SELECT` | `instanceGroup, project, zone` | Returns the specified zonal instance group. Get a list of available zonal instance groups by making a list() request. For managed instance groups, use the instanceGroupManagers or regionInstanceGroupManagers methods instead. |
| `list` | `SELECT` | `project, zone` | Retrieves the list of zonal instance group resources contained within the specified zone. For managed instance groups, use the instanceGroupManagers or regionInstanceGroupManagers methods instead. |
| `insert` | `INSERT` | `project, zone` | Creates an instance group in the specified project using the parameters that are included in the request. |
| `delete` | `DELETE` | `instanceGroup, project, zone` | Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information. |
| `_aggregated_list` | `EXEC` | `project` | Retrieves the list of instance groups and sorts them by zone. |
| `set_named_ports` | `EXEC` | `instanceGroup, project, zone` | Sets the named ports for the specified instance group. |
