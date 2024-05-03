---
title: scope_access_review_instance_contacted_reviewers
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_instance_contacted_reviewers
  - authorization
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
<tr><td><b>Name</b></td><td><code>scope_access_review_instance_contacted_reviewers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.scope_access_review_instance_contacted_reviewers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review reviewer id. |
| <CopyableCode code="name" /> | `string` | The access review reviewer id. |
| <CopyableCode code="properties" /> | `object` | Properties of access review contacted reviewer. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="id, scheduleDefinitionId, scope" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, scope" /> |
