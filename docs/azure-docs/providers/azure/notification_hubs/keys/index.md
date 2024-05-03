---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - notification_hubs
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="keyName" /> | `string` | Gets or sets keyName of the created AuthorizationRule |
| <CopyableCode code="primaryConnectionString" /> | `string` | Gets or sets primaryConnectionString of the AuthorizationRule. |
| <CopyableCode code="primaryKey" /> | `string` | Gets or sets primaryKey of the created AuthorizationRule. |
| <CopyableCode code="secondaryConnectionString" /> | `string` | Gets or sets secondaryConnectionString of the created<br />AuthorizationRule |
| <CopyableCode code="secondaryKey" /> | `string` | Gets or sets secondaryKey of the created AuthorizationRule |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
