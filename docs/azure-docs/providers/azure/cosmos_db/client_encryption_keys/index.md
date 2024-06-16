---
title: client_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - client_encryption_keys
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>client_encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.client_encryption_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | The properties of a ClientEncryptionKey resource |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, clientEncryptionKeyName, databaseName, resourceGroupName, subscriptionId" /> | Gets the ClientEncryptionKey under an existing Azure Cosmos DB SQL database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Lists the ClientEncryptionKeys under an existing Azure Cosmos DB SQL database. |
| <CopyableCode code="create_update" /> | `EXEC` | <CopyableCode code="accountName, clientEncryptionKeyName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a ClientEncryptionKey. This API is meant to be invoked via tools such as the Azure Powershell (instead of directly). |
