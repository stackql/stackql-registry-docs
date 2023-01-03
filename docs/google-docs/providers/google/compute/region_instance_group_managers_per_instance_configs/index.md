---
title: region_instance_group_managers_per_instance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_group_managers_per_instance_configs
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
<tr><td><b>Name</b></td><td><code>region_instance_group_managers_per_instance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_instance_group_managers_per_instance_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of a per-instance configuration and its corresponding instance. Serves as a merge key during UpdatePerInstanceConfigs operations, that is, if a per-instance configuration with the same name exists then it will be updated, otherwise a new one will be created for the VM instance with the same name. An attempt to create a per-instance configconfiguration for a VM instance that either doesn't exist or is not part of the group will result in an error. |
| `preservedState` | `object` | Preserved state for a given instance. |
| `status` | `string` | The status of applying this per-instance configuration on the corresponding managed instance. |
| `fingerprint` | `string` | Fingerprint of this per-instance config. This field can be used in optimistic locking. It is ignored when inserting a per-instance config. An up-to-date fingerprint must be provided in order to update an existing per-instance configuration or the field needs to be unset. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionInstanceGroupManagers_listPerInstanceConfigs` | `SELECT` | `instanceGroupManager, project, region` | Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported. |
| `regionInstanceGroupManagers_deletePerInstanceConfigs` | `DELETE` | `instanceGroupManager, project, region` | Deletes selected per-instance configurations for the managed instance group. |
