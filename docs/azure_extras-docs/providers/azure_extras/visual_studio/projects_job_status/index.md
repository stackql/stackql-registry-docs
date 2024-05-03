---
title: projects_job_status
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_job_status
  - visual_studio
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
<tr><td><b>Name</b></td><td><code>projects_job_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.visual_studio.projects_job_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Key/value pair of resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operation, resourceGroupName, resourceName, rootResourceName, subContainerName, subscriptionId" /> |
