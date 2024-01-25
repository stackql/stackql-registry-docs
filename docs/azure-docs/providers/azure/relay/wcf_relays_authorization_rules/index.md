---
title: wcf_relays_authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - wcf_relays_authorization_rules
  - relay
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
<tr><td><b>Name</b></td><td><code>wcf_relays_authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.relay.wcf_relays_authorization_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `` | Properties supplied to create or update AuthorizationRule |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `namespaceName, relayName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `namespaceName, relayName, resourceGroupName, subscriptionId` |
