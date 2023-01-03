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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`. |
| `state` | `string` | Output only. The current state of the instance. |
| `type` | `string` | Required. The type of the instance. Defaults to `PRODUCTION`. |
| `createTime` | `string` | Output only. A server-assigned timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`. |
| `displayName` | `string` | Required. The descriptive name for this instance as it appears in UIs. Can be changed at any time, but should be kept globally unique to avoid confusion. |
| `labels` | `object` | Required. Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `\p{Ll}\p{Lo}{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`. * No more than 64 labels can be associated with a given resource. * Keys and values must both be under 128 bytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instances_get` | `SELECT` | `instancesId, projectsId` | Gets information about an instance. |
| `projects_instances_list` | `SELECT` | `projectsId` | Lists information about instances in a project. |
| `projects_instances_create` | `INSERT` | `projectsId` | Create an instance within a project. Note that exactly one of Cluster.serve_nodes and Cluster.cluster_config.cluster_autoscaling_config can be set. If serve_nodes is set to non-zero, then the cluster is manually scaled. If cluster_config.cluster_autoscaling_config is non-empty, then autoscaling is enabled. |
| `projects_instances_delete` | `DELETE` | `instancesId, projectsId` | Delete an instance from a project. |
| `projects_instances_partialUpdateInstance` | `EXEC` | `instancesId, projectsId` | Partially updates an instance within a project. This method can modify all fields of an Instance and is the preferred way to update an Instance. |
| `projects_instances_update` | `EXEC` | `instancesId, projectsId` | Updates an instance within a project. This method updates only the display name and type for an Instance. To update other Instance properties, such as labels, use PartialUpdateInstance. |
