---
title: tenant_access_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access_secrets
  - api_management
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
<tr><td><b>Name</b></td><td><code>tenant_access_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_access_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Access Information type ('access' or 'gitAccess') |
| <CopyableCode code="enabled" /> | `boolean` | Determines whether direct access is enabled. |
| <CopyableCode code="primaryKey" /> | `string` | Primary access key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| <CopyableCode code="principalId" /> | `string` | Principal (User) Identifier. |
| <CopyableCode code="secondaryKey" /> | `string` | Secondary access key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accessName, resourceGroupName, serviceName, subscriptionId" /> |
