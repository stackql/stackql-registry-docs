---
title: target_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - target_instances
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
<tr><td><b>Name</b></td><td><code>target_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.target_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#targetInstance for target instances. |
| `network` | `string` | The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to the network that the default network interface belongs to. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `zone` | `string` | [Output Only] URL of the zone where the target instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `instance` | `string` | A URL to the virtual machine instance that handles traffic for this target instance. When creating a target instance, you can provide the fully-qualified URL or a valid partial URL to the desired virtual machine. For example, the following are all valid URLs: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance - zones/zone/instances/instance  |
| `natPolicy` | `string` | Must have a value of NO_NAT. Protocol forwarding delivers packets while preserving the destination IP address of the forwarding rule referencing the target instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregated_list` | `SELECT` | `project` | Retrieves an aggregated list of target instances. |
| `get` | `SELECT` | `project, targetInstance, zone` | Returns the specified TargetInstance resource. |
| `list` | `SELECT` | `project, zone` | Retrieves a list of TargetInstance resources available to the specified project and zone. |
| `insert` | `INSERT` | `project, zone` | Creates a TargetInstance resource in the specified project and zone using the data included in the request. |
| `delete` | `DELETE` | `project, targetInstance, zone` | Deletes the specified TargetInstance resource. |
| `_aggregated_list` | `EXEC` | `project` | Retrieves an aggregated list of target instances. |
