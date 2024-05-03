---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
  - application_insights
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
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.api_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of the API key inside an Application Insights component. It is auto generated when the API key is created. |
| <CopyableCode code="name" /> | `string` | The name of the API key. |
| <CopyableCode code="apiKey" /> | `string` | The API key value. It will be only return once when the API Key was created. |
| <CopyableCode code="createdDate" /> | `string` | The create date of this API key. |
| <CopyableCode code="linkedReadProperties" /> | `array` | The read access rights of this API Key. |
| <CopyableCode code="linkedWriteProperties" /> | `array` | The write access rights of this API Key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyId, resourceGroupName, resourceName, subscriptionId" /> | Get the API Key for this key id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of API keys of an Application Insights component. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create an API Key of an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyId, resourceGroupName, resourceName, subscriptionId" /> | Delete an API Key of an Application Insights component. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of API keys of an Application Insights component. |
