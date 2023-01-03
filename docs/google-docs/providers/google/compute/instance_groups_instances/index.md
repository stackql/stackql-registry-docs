---
title: instance_groups_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_groups_instances
  - compute
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
<tr><td><b>Name</b></td><td><code>instance_groups_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_groups_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `namedPorts` | `array` | [Output Only] The named ports that belong to this instance group. |
| `status` | `string` | [Output Only] The status of the instance. |
| `instance` | `string` | [Output Only] The URL of the instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instanceGroups_listInstances` | `SELECT` | `instanceGroup, project, zone` | Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators. |
| `instanceGroups_addInstances` | `INSERT` | `instanceGroup, project, zone` | Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information. |
| `instanceGroups_removeInstances` | `DELETE` | `instanceGroup, project, zone` | Removes one or more instances from the specified instance group, but does not delete those instances. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted. |
