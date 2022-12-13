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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_connection_infos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_connection_infos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hostServiceUri` | `string` | The on-premises integration runtime host URL. |
| `identityCertThumbprint` | `string` | The integration runtime SSL certificate thumbprint. Click-Once application uses it to do server validation. |
| `isIdentityCertExprired` | `boolean` | Whether the identity certificate is expired. |
| `publicKey` | `string` | The public key for encrypting a credential when transferring the credential to the integration runtime. |
| `serviceToken` | `string` | The token generated in service. Callers use this token to authenticate to integration runtime. |
| `version` | `string` | The integration runtime version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `IntegrationRuntimeConnectionInfos_Get` | `SELECT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` |
