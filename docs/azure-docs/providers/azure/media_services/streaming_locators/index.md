---
title: streaming_locators
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators
  - media_services
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
<tr><td><b>Name</b></td><td><code>streaming_locators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_locators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Streaming Locator. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId" /> | Get the details of a Streaming Locator in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Streaming Locators in the account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId" /> | Create a Streaming Locator in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId" /> | Deletes a Streaming Locator in the Media Services account |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Streaming Locators in the account |
