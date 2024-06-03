---
title: callbacks
hide_title: false
hide_table_of_contents: false
keywords:
  - callbacks
  - workflowexecutions
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>callbacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workflowexecutions.callbacks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the callback. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/workflows/&#123;workflow&#125;/executions/&#123;execution&#125;/callback/&#123;callback&#125; |
| <CopyableCode code="availablePayloads" /> | `array` | Output only. The payloads received by the callback that have not been processed by a waiting execution step. |
| <CopyableCode code="method" /> | `string` | Output only. The method accepted by the callback. For example: GET, POST, PUT. |
| <CopyableCode code="waiters" /> | `string` | Output only. Number of execution steps waiting on this callback. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> |
