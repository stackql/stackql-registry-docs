---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
  - batch
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
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.certificate</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Certificate properties. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificate_Get` | `SELECT` | `accountName, certificateName, resourceGroupName, subscriptionId` | Gets information about the specified certificate. |
| `Certificate_ListByBatchAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all of the certificates in the specified account. |
| `Certificate_Create` | `INSERT` | `accountName, certificateName, resourceGroupName, subscriptionId` | Creates a new certificate inside the specified account. |
| `Certificate_Delete` | `DELETE` | `accountName, certificateName, resourceGroupName, subscriptionId` | Deletes the specified certificate. |
| `Certificate_CancelDeletion` | `EXEC` | `accountName, certificateName, resourceGroupName, subscriptionId` | If you try to delete a certificate that is being used by a pool or compute node, the status of the certificate changes to deleteFailed. If you decide that you want to continue using the certificate, you can use this operation to set the status of the certificate back to active. If you intend to delete the certificate, you do not need to run this operation after the deletion failed. You must make sure that the certificate is not being used by any resources, and then you can try again to delete the certificate. |
| `Certificate_Update` | `EXEC` | `accountName, certificateName, resourceGroupName, subscriptionId` | Updates the properties of an existing certificate. |
