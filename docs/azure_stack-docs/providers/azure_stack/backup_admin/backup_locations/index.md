---
title: backup_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_locations
  - backup_admin
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
<tr><td><b>Name</b></td><td><code>backup_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.backup_admin.backup_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a backup location. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a specific backup location based on name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns the list of backup locations. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns the list of backup locations. |
| <CopyableCode code="prune_external_store" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Prune the external backup store. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Update a backup location. |
