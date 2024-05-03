---
title: cloud_workload_policy_files
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_workload_policy_files
  - cloud_workload_security
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_workload_policy_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.cloud_workload_security.cloud_workload_policy_files" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="_download_cloud_workload_policy_file" /> | `EXEC` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="download_cloud_workload_policy_file" /> | `EXEC` | <CopyableCode code="dd_site" /> |
