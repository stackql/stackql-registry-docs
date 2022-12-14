---
title: ledger_digest_uploads
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger_digest_uploads
  - sql
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
<tr><td><b>Name</b></td><td><code>ledger_digest_uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.ledger_digest_uploads</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LedgerDigestUploads_Get` | `SELECT` | `databaseName, ledgerDigestUploads, resourceGroupName, serverName, subscriptionId` | Gets the current ledger digest upload configuration for a database. |
| `LedgerDigestUploads_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets all ledger digest upload settings on a database. |
| `LedgerDigestUploads_CreateOrUpdate` | `INSERT` | `databaseName, ledgerDigestUploads, resourceGroupName, serverName, subscriptionId` | Enables upload ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
| `LedgerDigestUploads_Disable` | `EXEC` | `databaseName, ledgerDigestUploads, resourceGroupName, serverName, subscriptionId` | Disables uploading ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
