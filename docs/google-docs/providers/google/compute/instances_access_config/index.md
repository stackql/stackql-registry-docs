---
title: instances_access_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_access_config
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
<tr><td><b>Name</b></td><td><code>instances_access_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_access_config</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instances_addAccessConfig` | `INSERT` | `instance, networkInterface, project, zone` | Adds an access config to an instance's network interface. |
| `instances_deleteAccessConfig` | `DELETE` | `accessConfig, instance, networkInterface, project, zone` | Deletes an access config from an instance's network interface. |
