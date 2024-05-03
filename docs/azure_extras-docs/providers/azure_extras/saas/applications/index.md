---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - saas
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.saas.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | the resource Id. |
| <CopyableCode code="name" /> | `string` | the resource name. |
| <CopyableCode code="location" /> | `string` | the resource location. |
| <CopyableCode code="properties" /> | `object` | Saas resource properties. |
| <CopyableCode code="tags" /> | `object` | the resource tags. |
| <CopyableCode code="type" /> | `string` | the resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
