---
title: instance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_configs
  - spanner
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
<tr><td><b>Name</b></td><td><code>instance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.instance_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A unique identifier for the instance configuration. Values are of the form `projects//instanceConfigs/a-z*`. |
| `replicas` | `array` | The geographic placement of nodes in this instance configuration and their replication properties. |
| `displayName` | `string` | The name of this instance configuration as it appears in UIs. |
| `leaderOptions` | `array` | Allowed values of the "default_leader" schema option for databases in instances that use this instance configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instanceConfigs_get` | `SELECT` | `instanceConfigsId, projectsId` | Gets information about a particular instance configuration. |
| `projects_instanceConfigs_list` | `SELECT` | `projectsId` | Lists the supported instance configurations for a given project. |
