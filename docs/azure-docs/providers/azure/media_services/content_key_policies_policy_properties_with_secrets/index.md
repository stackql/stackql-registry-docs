---
title: content_key_policies_policy_properties_with_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies_policy_properties_with_secrets
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
<tr><td><b>Name</b></td><td><code>content_key_policies_policy_properties_with_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.content_key_policies_policy_properties_with_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description for the Policy. |
| <CopyableCode code="created" /> | `string` | The creation date of the Policy |
| <CopyableCode code="lastModified" /> | `string` | The last modified date of the Policy |
| <CopyableCode code="options" /> | `array` | The Key Policy options. |
| <CopyableCode code="policyId" /> | `string` | The legacy Policy ID. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId" /> |
