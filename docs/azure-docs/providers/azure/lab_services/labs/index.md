---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
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
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.labs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a lab resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Returns the properties of a lab resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` |  | Returns a list of all labs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` |  | Returns a list of all labs for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__properties" /> | Operation to create or update a lab resource. |
| <CopyableCode code="delete" /> | `DELETE` |  | Operation to delete a lab resource. |
| <CopyableCode code="publish" /> | `EXEC` |  | Publish or re-publish a lab. This will create or update all lab resources, such as virtual machines. |
| <CopyableCode code="sync_group" /> | `EXEC` |  | Action used to manually kick off an AAD group sync job. |
| <CopyableCode code="update" /> | `EXEC` |  | Operation to update a lab resource. |
