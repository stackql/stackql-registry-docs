---
title: node_proxy_options
hide_title: false
hide_table_of_contents: false
keywords:
  - node_proxy_options
  - core_v1
  - k8s    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: /img/providers/k8s/stackql-k8s-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_proxy_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.node_proxy_options</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `connectCoreV1DeleteNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect DELETE requests to proxy of Node |
| `connectCoreV1DeleteNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect DELETE requests to proxy of Node |
| `connectCoreV1GetNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect GET requests to proxy of Node |
| `connectCoreV1GetNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect GET requests to proxy of Node |
| `connectCoreV1HeadNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect HEAD requests to proxy of Node |
| `connectCoreV1HeadNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect HEAD requests to proxy of Node |
| `connectCoreV1OptionsNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect OPTIONS requests to proxy of Node |
| `connectCoreV1OptionsNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect OPTIONS requests to proxy of Node |
| `connectCoreV1PatchNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect PATCH requests to proxy of Node |
| `connectCoreV1PatchNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect PATCH requests to proxy of Node |
| `connectCoreV1PostNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect POST requests to proxy of Node |
| `connectCoreV1PostNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect POST requests to proxy of Node |
| `connectCoreV1PutNodeProxy` | `EXEC` | `name, cluster_addr, protocol` | connect PUT requests to proxy of Node |
| `connectCoreV1PutNodeProxyWithPath` | `EXEC` | `name, path, cluster_addr, protocol` | connect PUT requests to proxy of Node |
