---
title: services_export_errors_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - services_export_errors_v2
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>services_export_errors_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.services_export_errors_v2</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The error Id. |
| `attributeName` | `string` | The attribute name. |
| `attributeValue` | `string` | The attribute value. |
| `createdDate` | `string` | The date and time, in UTC, when the error was created. |
| `csObjectId` | `string` |  the cs object Id. |
| `dn` | `string` | the DN of the object. |
| `existingObject` | `object` | Object that hold sync object details. |
| `exportErrorStatus` | `integer` | The export error status. |
| `incomingObject` | `object` | Object that hold sync object details. |
| `incomingObjectDisplayName` | `string` | The incoming object display name. |
| `incomingObjectType` | `string` | The incoming object type. |
| `mergedEntityId` | `string` | The merged entity Id. |
| `modifiedOrRemovedAttributeValue` | `string` | The modified or removed attribute value. |
| `runStepResultId` | `string` | The run step result Id. |
| `samAccountName` | `string` | The sam account name. |
| `serverErrorDetail` | `string` | The server error details. |
| `serviceId` | `string` | The service Id. |
| `serviceMemberId` | `string` | The server Id. |
| `timeFirstOccurred` | `string` | The time when the error first occurred. |
| `timeOccurred` | `string` | The date and time when the error occurred. |
| `type` | `string` | The type of the error. |
| `userPrincipalName` | `string` | The user principal name |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `errorBucket, serviceName` |
| `_list` | `EXEC` | `errorBucket, serviceName` |
