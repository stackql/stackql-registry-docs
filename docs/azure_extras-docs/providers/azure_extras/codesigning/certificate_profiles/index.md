---
title: certificate_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_profiles
  - codesigning
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>certificate_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.codesigning.certificate_profiles" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId" /> | Get details of a certificate profile. |
| <CopyableCode code="list_by_code_signing_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List certificate profiles under a trusted signing account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId" /> | Create a certificate profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId" /> | Delete a certificate profile. |
| <CopyableCode code="revoke_certificate" /> | `EXEC` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId, data__effectiveAt, data__reason, data__serialNumber, data__thumbprint" /> | Revoke a certificate under a certificate profile. |
