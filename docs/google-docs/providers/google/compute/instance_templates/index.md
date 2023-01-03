---
title: instance_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_templates
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
<tr><td><b>Name</b></td><td><code>instance_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this instance template. The server defines this identifier. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `sourceInstanceParams` | `object` | A specification of the parameters to use when creating the instance template from a source instance. |
| `kind` | `string` | [Output Only] The resource type, which is always compute#instanceTemplate for instance templates. |
| `selfLink` | `string` | [Output Only] The URL for this instance template. The server defines this URL. |
| `properties` | `object` |  |
| `creationTimestamp` | `string` | [Output Only] The creation timestamp for this instance template in RFC3339 text format. |
| `sourceInstance` | `string` | The source instance used to create the template. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /instances/instance - projects/project/zones/zone/instances/instance  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instanceTemplates_get` | `SELECT` | `instanceTemplate, project` | Returns the specified instance template. Gets a list of available instance templates by making a list() request. |
| `instanceTemplates_list` | `SELECT` | `project` | Retrieves a list of instance templates that are contained within the specified project. |
| `instanceTemplates_insert` | `INSERT` | `project` | Creates an instance template in the specified project using the data that is included in the request. If you are creating a new template to update an existing instance group, your new instance template must use the same network or, if applicable, the same subnetwork as the original template. |
| `instanceTemplates_delete` | `DELETE` | `instanceTemplate, project` | Deletes the specified instance template. Deleting an instance template is permanent and cannot be undone. It is not possible to delete templates that are already in use by a managed instance group. |
