---
title: disaster_recovery_configs_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs_keys
  - event_hubs
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
<tr><td><b>Name</b></td><td><code>disaster_recovery_configs_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.disaster_recovery_configs_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aliasPrimaryConnectionString" /> | `string` | Primary connection string of the alias if GEO DR is enabled |
| <CopyableCode code="aliasSecondaryConnectionString" /> | `string` | Secondary  connection string of the alias if GEO DR is enabled |
| <CopyableCode code="keyName" /> | `string` | A string that describes the AuthorizationRule. |
| <CopyableCode code="primaryConnectionString" /> | `string` | Primary connection string of the created namespace AuthorizationRule. |
| <CopyableCode code="primaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Secondary connection string of the created namespace AuthorizationRule. |
| <CopyableCode code="secondaryKey" /> | `string` | A base64-encoded 256-bit primary key for signing and validating the SAS token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="alias, authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> |
