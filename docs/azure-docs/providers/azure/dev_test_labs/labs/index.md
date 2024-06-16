---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - dev_test_labs
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.labs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a lab. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Get lab. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List labs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List labs in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Create or replace an existing lab. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Delete lab. This operation can take a while to complete. |
| <CopyableCode code="claim_any_vm" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Claim a random claimable virtual machine in the lab. This operation can take a while to complete. |
| <CopyableCode code="export_resource_usage" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Exports the lab resource usage into a storage account This operation can take a while to complete. |
| <CopyableCode code="generate_upload_uri" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Generate a URI for uploading custom disk images to a Lab. |
| <CopyableCode code="import_virtual_machine" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Import a virtual machine into a different lab. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of labs. All other properties will be ignored. |
