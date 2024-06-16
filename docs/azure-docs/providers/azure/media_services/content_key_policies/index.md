---
title: content_key_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies
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
<tr><td><b>Name</b></td><td><code>content_key_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.content_key_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the Content Key Policy. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Get the details of a Content Key Policy in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Content Key Policies in the account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Create or update a Content Key Policy in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Deletes a Content Key Policy in the Media Services account |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Updates an existing Content Key Policy in the Media Services account |
