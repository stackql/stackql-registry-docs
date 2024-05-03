---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - lab_services
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | User resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Returns the properties of a lab user. |
| <CopyableCode code="list_by_lab" /> | `SELECT` |  | Returns a list of all users for a lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__properties" /> | Operation to create or update a lab user. |
| <CopyableCode code="delete" /> | `DELETE` |  | Operation to delete a user resource. |
| <CopyableCode code="_list_by_lab" /> | `EXEC` |  | Returns a list of all users for a lab. |
| <CopyableCode code="invite" /> | `EXEC` |  | Operation to invite a user to a lab. |
| <CopyableCode code="update" /> | `EXEC` |  | Operation to update a lab user. |
