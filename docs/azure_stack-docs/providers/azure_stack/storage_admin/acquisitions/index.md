---
title: acquisitions
hide_title: false
hide_table_of_contents: false
keywords:
  - acquisitions
  - storage_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>acquisitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.storage_admin.acquisitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `acquisitionid` | `string` | The ID of page BLOB acquisition. |
| `blob` | `string` | The name of the page BLOB. |
| `container` | `string` | The container associated with the page BLOB. |
| `filePath` | `string` | The file path of the page BLOB file on storage cluster. |
| `filePathUnc` | `string` | The file path unc of the page BLOB file on storage cluster. |
| `maximumblobsize` | `integer` | The maximum size of the page BLOB. |
| `status` | `string` | The status of page BLOB acquisition. |
| `storageaccount` | `string` | The storage account that holds the page BLOB. |
| `susbcriptionid` | `string` | ID of the subscription associated with the page BLOB. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, subscriptionId` |
| `_list` | `EXEC` | `location, subscriptionId` |
