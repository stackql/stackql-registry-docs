---
title: vm_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_extensions
  - compute_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>vm_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.vm_extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a Virtual Machine Extension Image. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, publisher, subscriptionId, type, version" /> | Returns requested Virtual Machine Extension Image matching publisher, type, version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List of all Virtual Machine Extension Images for the current location are returned. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, publisher, subscriptionId, type, version" /> | Create a Virtual Machine Extension Image with publisher, version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, publisher, subscriptionId, type, version" /> | Deletes specified Virtual Machine Extension Image. |
