---
title: virtual_machine_image_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates
  - image_builder
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
<tr><td><b>Name</b></td><td><code>virtual_machine_image_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.image_builder.virtual_machine_image_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the image template. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an image template |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Get information about a virtual machine image template |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about the VM image templates associated with the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets information about the VM image templates associated with the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, data__identity" /> | Create or update a virtual machine image template |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Delete a virtual machine image template |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets information about the VM image templates associated with the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets information about the VM image templates associated with the specified resource group. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Cancel the long running image build based on the image template |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Create artifacts from a existing image template |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Update the tags for this Virtual Machine Image Template |
