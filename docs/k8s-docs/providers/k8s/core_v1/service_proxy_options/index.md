---
title: service_proxy_options
hide_title: false
hide_table_of_contents: false
keywords:
  - service_proxy_options
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
<tr><td><b>Name</b></td><td><code>service_proxy_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.service_proxy_options" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="connectCoreV1DeleteNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect DELETE requests to proxy of Service |
| <CopyableCode code="connectCoreV1DeleteNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect DELETE requests to proxy of Service |
| <CopyableCode code="connectCoreV1GetNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect GET requests to proxy of Service |
| <CopyableCode code="connectCoreV1GetNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect GET requests to proxy of Service |
| <CopyableCode code="connectCoreV1HeadNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect HEAD requests to proxy of Service |
| <CopyableCode code="connectCoreV1HeadNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect HEAD requests to proxy of Service |
| <CopyableCode code="connectCoreV1OptionsNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect OPTIONS requests to proxy of Service |
| <CopyableCode code="connectCoreV1OptionsNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect OPTIONS requests to proxy of Service |
| <CopyableCode code="connectCoreV1PatchNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect PATCH requests to proxy of Service |
| <CopyableCode code="connectCoreV1PatchNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect PATCH requests to proxy of Service |
| <CopyableCode code="connectCoreV1PostNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect POST requests to proxy of Service |
| <CopyableCode code="connectCoreV1PostNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect POST requests to proxy of Service |
| <CopyableCode code="connectCoreV1PutNamespacedServiceProxy" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect PUT requests to proxy of Service |
| <CopyableCode code="connectCoreV1PutNamespacedServiceProxyWithPath" /> | `EXEC` | <CopyableCode code="name, namespace, path, cluster_addr, protocol" /> | connect PUT requests to proxy of Service |
