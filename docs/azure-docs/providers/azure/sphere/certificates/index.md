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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sphere.certificates</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, resourceGroupName, serialNumber, subscriptionId` | Get a Certificate |
| `list_by_catalog` | `SELECT` | `catalogName, resourceGroupName, subscriptionId` | List Certificate resources by Catalog |
| `_list_by_catalog` | `EXEC` | `catalogName, resourceGroupName, subscriptionId` | List Certificate resources by Catalog |
| `retrieve_cert_chain` | `EXEC` | `catalogName, resourceGroupName, serialNumber, subscriptionId` | Retrieves cert chain. |
| `retrieve_proof_of_possession_nonce` | `EXEC` | `catalogName, resourceGroupName, serialNumber, subscriptionId, data__proofOfPossessionNonce` | Gets the proof of possession nonce. |
