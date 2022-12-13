---
title: api_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - api_revision
  - api_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_revision</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Description of the API Revision. |
| `apiId` | `string` | Identifier of the API Revision. |
| `apiRevision` | `string` | Revision number of API. |
| `createdDateTime` | `string` | The time the API Revision was created. The date conforms to the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard. |
| `isCurrent` | `boolean` | Indicates if API revision is accessible via the gateway. |
| `isOnline` | `boolean` | Indicates if API revision is the current api revision. |
| `privateUrl` | `string` | Gateway URL for accessing the non-current API Revision. |
| `updatedDateTime` | `string` | The time the API Revision were updated. The date conforms to the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ApiRevision_ListByService` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` |
