---
title: region_instance_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_templates
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
<tr><td><b>Name</b></td><td><code>region_instance_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_instance_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this instance template. The server defines this identifier. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] The creation timestamp for this instance template in RFC3339 text format. |
| `kind` | `string` | [Output Only] The resource type, which is always compute#instanceTemplate for instance templates. |
| `sourceInstance` | `string` | The source instance used to create the template. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance  |
| `sourceInstanceParams` | `object` | A specification of the parameters to use when creating the instance template from a source instance. |
| `region` | `string` | [Output Only] URL of the region where the instance template resides. Only applicable for regional resources. |
| `properties` | `object` |  |
| `selfLink` | `string` | [Output Only] The URL for this instance template. The server defines this URL. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instanceTemplate, project, region` | Returns the specified instance template. |
| `list` | `SELECT` | `project, region` | Retrieves a list of instance templates that are contained within the specified project and region. |
| `insert` | `INSERT` | `project, region` | Creates an instance template in the specified project and region using the global instance template whose URL is included in the request. |
| `delete` | `DELETE` | `instanceTemplate, project, region` | Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. |
| `_list` | `EXEC` | `project, region` | Retrieves a list of instance templates that are contained within the specified project and region. |
