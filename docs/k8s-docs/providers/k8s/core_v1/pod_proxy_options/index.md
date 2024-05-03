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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pod_proxy_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.pod_proxy_options" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="connectCoreV1DeleteNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect DELETE requests to proxy of Pod |
| <CopyableCode code="connectCoreV1DeleteNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect DELETE requests to proxy of Pod |
| <CopyableCode code="connectCoreV1GetNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect GET requests to proxy of Pod |
| <CopyableCode code="connectCoreV1GetNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect GET requests to proxy of Pod |
| <CopyableCode code="connectCoreV1HeadNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect HEAD requests to proxy of Pod |
| <CopyableCode code="connectCoreV1HeadNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect HEAD requests to proxy of Pod |
| <CopyableCode code="connectCoreV1OptionsNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect OPTIONS requests to proxy of Pod |
| <CopyableCode code="connectCoreV1OptionsNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect OPTIONS requests to proxy of Pod |
| <CopyableCode code="connectCoreV1PatchNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect PATCH requests to proxy of Pod |
| <CopyableCode code="connectCoreV1PatchNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect PATCH requests to proxy of Pod |
| <CopyableCode code="connectCoreV1PostNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect POST requests to proxy of Pod |
| <CopyableCode code="connectCoreV1PostNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect POST requests to proxy of Pod |
| <CopyableCode code="connectCoreV1PutNamespacedPodProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect PUT requests to proxy of Pod |
| <CopyableCode code="connectCoreV1PutNamespacedPodProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect PUT requests to proxy of Pod |
