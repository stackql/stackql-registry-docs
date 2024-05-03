---
title: integration_runtime_connection_infos
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_connection_infos
  - synapse
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
<tr><td><b>Name</b></td><td><code>integration_runtime_connection_infos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtime_connection_infos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="hostServiceUri" /> | `string` | The on-premises integration runtime host URL. |
| <CopyableCode code="identityCertThumbprint" /> | `string` | The integration runtime SSL certificate thumbprint. Click-Once application uses it to do server validation. |
| <CopyableCode code="isIdentityCertExprired" /> | `boolean` | Whether the identity certificate is expired. |
| <CopyableCode code="publicKey" /> | `string` | The public key for encrypting a credential when transferring the credential to the integration runtime. |
| <CopyableCode code="serviceToken" /> | `string` | The token generated in service. Callers use this token to authenticate to integration runtime. |
| <CopyableCode code="version" /> | `string` | The integration runtime version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> |
