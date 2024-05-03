---
title: sql_pool_transparent_data_encryptions
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_transparent_data_encryptions
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_transparent_data_encryptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_transparent_data_encryptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a database transparent data encryption. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, transparentDataEncryptionName, workspaceName" /> | Get a SQL pool's transparent data encryption configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get list of SQL pool's transparent data encryption configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, transparentDataEncryptionName, workspaceName" /> | Creates or updates a Sql pool's transparent data encryption configuration. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get list of SQL pool's transparent data encryption configurations. |
