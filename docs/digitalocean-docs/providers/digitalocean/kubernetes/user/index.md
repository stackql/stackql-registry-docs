---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - kubernetes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.kubernetes.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `username` | `string` | The username for the cluster admin user. |
| `groups` | `array` | A list of in-cluster groups that the user belongs to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_clusterUser` | `SELECT` | `cluster_id` |
| `_get_clusterUser` | `EXEC` | `cluster_id` |
