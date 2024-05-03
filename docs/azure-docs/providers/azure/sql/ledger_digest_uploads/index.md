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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ledger_digest_uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.ledger_digest_uploads" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, ledgerDigestUploads, resourceGroupName, serverName, subscriptionId" /> | Gets the current ledger digest upload configuration for a database. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets all ledger digest upload settings on a database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, ledgerDigestUploads, resourceGroupName, serverName, subscriptionId" /> | Enables upload ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
| <CopyableCode code="_list_by_database" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets all ledger digest upload settings on a database. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="databaseName, ledgerDigestUploads, resourceGroupName, serverName, subscriptionId" /> | Disables uploading ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
