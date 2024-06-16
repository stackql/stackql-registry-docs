---
title: extended_server_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_server_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>extended_server_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.extended_server_blob_auditing_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, serverName, subscriptionId" /> | Gets an extended server's blob auditing policy. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists extended auditing settings of a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blobAuditingPolicyName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates an extended server's blob auditing policy. |
