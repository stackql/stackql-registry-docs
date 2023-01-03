---
title: service_proxy_options
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
<tr><td><b>Name</b></td><td><code>service_proxy_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.service_proxy_options</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `connectCoreV1DeleteNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect DELETE requests to proxy of Service |
| `connectCoreV1DeleteNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect DELETE requests to proxy of Service |
| `connectCoreV1GetNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect GET requests to proxy of Service |
| `connectCoreV1GetNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect GET requests to proxy of Service |
| `connectCoreV1HeadNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect HEAD requests to proxy of Service |
| `connectCoreV1HeadNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect HEAD requests to proxy of Service |
| `connectCoreV1OptionsNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect OPTIONS requests to proxy of Service |
| `connectCoreV1OptionsNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect OPTIONS requests to proxy of Service |
| `connectCoreV1PatchNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect PATCH requests to proxy of Service |
| `connectCoreV1PatchNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect PATCH requests to proxy of Service |
| `connectCoreV1PostNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect POST requests to proxy of Service |
| `connectCoreV1PostNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect POST requests to proxy of Service |
| `connectCoreV1PutNamespacedServiceProxy` | `EXEC` | `name, namespace` | connect PUT requests to proxy of Service |
| `connectCoreV1PutNamespacedServiceProxyWithPath` | `EXEC` | `name, namespace, path` | connect PUT requests to proxy of Service |
