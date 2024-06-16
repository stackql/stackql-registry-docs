---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - sphere
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.certificates" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, serialNumber, subscriptionId" /> | Get a Certificate |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Certificate resources by Catalog |
| <CopyableCode code="retrieve_cert_chain" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, serialNumber, subscriptionId" /> | Retrieves cert chain. |
| <CopyableCode code="retrieve_proof_of_possession_nonce" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, serialNumber, subscriptionId, data__proofOfPossessionNonce" /> | Gets the proof of possession nonce. |
