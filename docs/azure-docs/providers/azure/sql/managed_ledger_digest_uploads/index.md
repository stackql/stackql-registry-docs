---
title: managed_ledger_digest_uploads
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ledger_digest_uploads
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
<tr><td><b>Name</b></td><td><code>managed_ledger_digest_uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_ledger_digest_uploads</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, ledgerDigestUploads, managedInstanceName, resourceGroupName, subscriptionId` | Gets the current ledger digest upload configuration for a database. |
| `list_by_database` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets all ledger digest upload settings on a database. |
| `create_or_update` | `INSERT` | `databaseName, ledgerDigestUploads, managedInstanceName, resourceGroupName, subscriptionId` | Enables upload ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
| `_list_by_database` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets all ledger digest upload settings on a database. |
| `disable` | `EXEC` | `databaseName, ledgerDigestUploads, managedInstanceName, resourceGroupName, subscriptionId` | Disables uploading ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
