---
title: instance_group_managers_per_instance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers_per_instance_configs
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
<tr><td><b>Name</b></td><td><code>instance_group_managers_per_instance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instance_group_managers_per_instance_configs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `delete_per_instance_configs` | `EXEC` | `instanceGroupManager, project, zone` | Deletes selected per-instance configurations for the managed instance group. |
| `list_per_instance_configs` | `EXEC` | `instanceGroupManager, project, zone` | Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported. |
| `update_per_instance_configs` | `EXEC` | `instanceGroupManager, project, zone` | Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
