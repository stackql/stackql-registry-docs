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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_proxy_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.node_proxy_options" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="connectCoreV1DeleteNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect DELETE requests to proxy of Node |
| <CopyableCode code="connectCoreV1DeleteNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect DELETE requests to proxy of Node |
| <CopyableCode code="connectCoreV1GetNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect GET requests to proxy of Node |
| <CopyableCode code="connectCoreV1GetNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect GET requests to proxy of Node |
| <CopyableCode code="connectCoreV1HeadNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect HEAD requests to proxy of Node |
| <CopyableCode code="connectCoreV1HeadNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect HEAD requests to proxy of Node |
| <CopyableCode code="connectCoreV1OptionsNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect OPTIONS requests to proxy of Node |
| <CopyableCode code="connectCoreV1OptionsNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect OPTIONS requests to proxy of Node |
| <CopyableCode code="connectCoreV1PatchNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect PATCH requests to proxy of Node |
| <CopyableCode code="connectCoreV1PatchNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect PATCH requests to proxy of Node |
| <CopyableCode code="connectCoreV1PostNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect POST requests to proxy of Node |
| <CopyableCode code="connectCoreV1PostNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect POST requests to proxy of Node |
| <CopyableCode code="connectCoreV1PutNodeProxy" /> | `EXEC` | <CopyableCode code="name, cluster_addr, protocol" /> | connect PUT requests to proxy of Node |
| <CopyableCode code="connectCoreV1PutNodeProxyWithPath" /> | `EXEC` | <CopyableCode code="name, path, cluster_addr, protocol" /> | connect PUT requests to proxy of Node |
