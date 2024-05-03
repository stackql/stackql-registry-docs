---
title: data_masking_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_policies
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
<tr><td><b>Name</b></td><td><code>data_masking_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.data_masking_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of data masking policy. Metadata, used for Azure portal. |
| <CopyableCode code="location" /> | `string` | The location of the data masking policy. |
| <CopyableCode code="properties" /> | `object` | The properties of a database data masking policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database data masking policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a database data masking policy |
