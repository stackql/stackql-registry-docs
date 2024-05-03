---
title: pod_exec_options
hide_title: false
hide_table_of_contents: false
keywords:
  - pod_exec_options
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
<tr><td><b>Name</b></td><td><code>pod_exec_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="k8s.core_v1.pod_exec_options" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="connectCoreV1GetNamespacedPodExec" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect GET requests to exec of Pod |
| <CopyableCode code="connectCoreV1PostNamespacedPodExec" /> | `EXEC` | <CopyableCode code="name, namespace, cluster_addr, protocol" /> | connect POST requests to exec of Pod |
