---
title: provider_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_registrations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>provider_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.provider_registrations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the provider registration details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of the provider registrations in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Creates or updates the provider registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, subscriptionId" /> | Deletes a provider registration. |
| <CopyableCode code="generate_operations" /> | `EXEC` | <CopyableCode code="providerNamespace, subscriptionId" /> | Generates the operations api for the given provider. |
