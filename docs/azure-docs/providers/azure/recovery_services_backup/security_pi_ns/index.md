---
title: security_pi_ns
hide_title: false
hide_table_of_contents: false
keywords:
  - security_pi_ns
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>security_pi_ns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.security_pi_ns" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expiryTimeInUtcTicks" /> | `integer` | Expiry time of token. |
| <CopyableCode code="securityPIN" /> | `string` | Security PIN |
| <CopyableCode code="token" /> | `string` | Token value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, vaultName" /> |
