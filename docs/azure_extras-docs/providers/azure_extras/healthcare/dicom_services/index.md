---
title: dicom_services
hide_title: false
hide_table_of_contents: false
keywords:
  - dicom_services
  - healthcare
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
<tr><td><b>Name</b></td><td><code>dicom_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.dicom_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="properties" /> | `object` | Dicom Service properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified DICOM Service. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all DICOM Services for the given workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a DICOM Service resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a DICOM Service. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all DICOM Services for the given workspace |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dicomServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Patch DICOM Service details. |
