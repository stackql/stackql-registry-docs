---
title: rp_unbilled_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - rp_unbilled_prefixes
  - peering
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
<tr><td><b>Name</b></td><td><code>rp_unbilled_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.rp_unbilled_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `azureRegion` | `string` | The Azure region. |
| `peerAsn` | `integer` | The peer ASN. |
| `prefix` | `string` | The prefix. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `peeringName, resourceGroupName, subscriptionId` |
