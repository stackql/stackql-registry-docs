---
title: node_proxy_options
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes
  - k8s
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Kubernetes resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `connectCoreV1DeleteNodeProxy` | `EXEC` | `name` | connect DELETE requests to proxy of Node |
| `connectCoreV1DeleteNodeProxyWithPath` | `EXEC` | `name, path` | connect DELETE requests to proxy of Node |
| `connectCoreV1GetNodeProxy` | `EXEC` | `name` | connect GET requests to proxy of Node |
| `connectCoreV1GetNodeProxyWithPath` | `EXEC` | `name, path` | connect GET requests to proxy of Node |
| `connectCoreV1HeadNodeProxy` | `EXEC` | `name` | connect HEAD requests to proxy of Node |
| `connectCoreV1HeadNodeProxyWithPath` | `EXEC` | `name, path` | connect HEAD requests to proxy of Node |
| `connectCoreV1OptionsNodeProxy` | `EXEC` | `name` | connect OPTIONS requests to proxy of Node |
| `connectCoreV1OptionsNodeProxyWithPath` | `EXEC` | `name, path` | connect OPTIONS requests to proxy of Node |
| `connectCoreV1PatchNodeProxy` | `EXEC` | `name` | connect PATCH requests to proxy of Node |
| `connectCoreV1PatchNodeProxyWithPath` | `EXEC` | `name, path` | connect PATCH requests to proxy of Node |
| `connectCoreV1PostNodeProxy` | `EXEC` | `name` | connect POST requests to proxy of Node |
| `connectCoreV1PostNodeProxyWithPath` | `EXEC` | `name, path` | connect POST requests to proxy of Node |
| `connectCoreV1PutNodeProxy` | `EXEC` | `name` | connect PUT requests to proxy of Node |
| `connectCoreV1PutNodeProxyWithPath` | `EXEC` | `name, path` | connect PUT requests to proxy of Node |
