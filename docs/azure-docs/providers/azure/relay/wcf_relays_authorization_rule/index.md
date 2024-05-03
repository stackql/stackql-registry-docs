---
title: wcf_relays_authorization_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - wcf_relays_authorization_rule
  - relay
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
<tr><td><b>Name</b></td><td><code>wcf_relays_authorization_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relay.wcf_relays_authorization_rule" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `` | Properties supplied to create or update AuthorizationRule |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Get authorizationRule for a WCF relay by name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Creates or updates an authorization rule for a WCF relay. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationRuleName, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Deletes a WCF relay authorization rule. |
