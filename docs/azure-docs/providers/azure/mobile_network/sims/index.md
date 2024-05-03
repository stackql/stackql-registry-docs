---
title: sims
hide_title: false
hide_table_of_contents: false
keywords:
  - sims
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>sims</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.sims" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, simGroupName, simName, subscriptionId" /> | Gets information about the specified SIM. |
| <CopyableCode code="list_by_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Gets all the SIMs in a SIM group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, simGroupName, simName, subscriptionId, data__properties" /> | Creates or updates a SIM. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, simGroupName, simName, subscriptionId" /> | Deletes the specified SIM. |
| <CopyableCode code="_list_by_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Gets all the SIMs in a SIM group. |
| <CopyableCode code="bulk_delete" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__sims" /> | Bulk delete SIMs from a SIM group. |
| <CopyableCode code="bulk_upload" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__sims" /> | Bulk upload SIMs to a SIM group. |
| <CopyableCode code="bulk_upload_encrypted" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__azureKeyIdentifier, data__encryptedTransportKey, data__signedTransportKey, data__sims, data__vendorKeyFingerprint, data__version" /> | Bulk upload SIMs in encrypted form to a SIM group. The SIM credentials must be encrypted. |
