---
title: encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_protectors
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
<tr><td><b>Name</b></td><td><code>encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.encryption_protectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for an encryption protector execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="encryptionProtectorName, resourceGroupName, serverName, subscriptionId" /> | Gets a server encryption protector. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server encryption protectors |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="encryptionProtectorName, resourceGroupName, serverName, subscriptionId" /> | Updates an existing encryption protector. |
| <CopyableCode code="revalidate" /> | `EXEC` | <CopyableCode code="encryptionProtectorName, resourceGroupName, serverName, subscriptionId" /> | Revalidates an existing encryption protector. |
