---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.backup_admin.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for a backup. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backup, location, resourceGroupName, subscriptionId" /> | Returns a backup from a location based on name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of backups from a location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Back up a specific location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of backups from a location. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="backup, location, resourceGroupName, subscriptionId" /> | Restore a backup. |
