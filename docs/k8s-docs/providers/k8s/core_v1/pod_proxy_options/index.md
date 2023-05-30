---
title: pod_proxy_options
hide_title: false
hide_table_of_contents: false
keywords:
  - pod_proxy_options
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
<tr><td><b>Name</b></td><td><code>pod_proxy_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>k8s.core_v1.pod_proxy_options</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `connectCoreV1DeleteNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect DELETE requests to proxy of Pod |
| `connectCoreV1DeleteNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect DELETE requests to proxy of Pod |
| `connectCoreV1GetNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect GET requests to proxy of Pod |
| `connectCoreV1GetNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect GET requests to proxy of Pod |
| `connectCoreV1HeadNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect HEAD requests to proxy of Pod |
| `connectCoreV1HeadNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect HEAD requests to proxy of Pod |
| `connectCoreV1OptionsNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect OPTIONS requests to proxy of Pod |
| `connectCoreV1OptionsNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect OPTIONS requests to proxy of Pod |
| `connectCoreV1PatchNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect PATCH requests to proxy of Pod |
| `connectCoreV1PatchNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect PATCH requests to proxy of Pod |
| `connectCoreV1PostNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect POST requests to proxy of Pod |
| `connectCoreV1PostNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect POST requests to proxy of Pod |
| `connectCoreV1PutNamespacedPodProxy` | `EXEC` | `name, namespace, cluster_addr, protocol` | connect PUT requests to proxy of Pod |
| `connectCoreV1PutNamespacedPodProxyWithPath` | `EXEC` | `name, namespace, path, cluster_addr, protocol` | connect PUT requests to proxy of Pod |
