---
title: metric_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_namespaces
  - monitor
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metric_namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the metric namespace. |
| <CopyableCode code="name" /> | `string` | The escaped name of the namespace. |
| <CopyableCode code="classification" /> | `string` | Kind of namespace |
| <CopyableCode code="properties" /> | `object` | The fully qualified metric namespace name. |
| <CopyableCode code="type" /> | `string` | The type of the namespace. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> |
