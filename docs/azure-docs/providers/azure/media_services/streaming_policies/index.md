---
title: streaming_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_policies
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
<tr><td><b>Name</b></td><td><code>streaming_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class to specify properties of Streaming Policy |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingPolicyName, subscriptionId" /> | Get the details of a Streaming Policy in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Streaming Policies in the account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingPolicyName, subscriptionId" /> | Create a Streaming Policy in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, streamingPolicyName, subscriptionId" /> | Deletes a Streaming Policy in the Media Services account |
