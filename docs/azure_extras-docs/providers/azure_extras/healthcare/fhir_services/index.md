---
title: fhir_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_services
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
<tr><td><b>Name</b></td><td><code>fhir_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.fhir_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="kind" /> | `string` | The kind of the service. |
| <CopyableCode code="properties" /> | `object` | Fhir Service properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified FHIR Service. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all FHIR Services for the given workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a FHIR Service resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a FHIR Service. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all FHIR Services for the given workspace |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="fhirServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Patch FHIR Service details. |
