---
title: monitors_sso_details
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_sso_details
  - dynatrace
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_sso_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.dynatrace.monitors_sso_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `aadDomains` | `array` | array of Aad(azure active directory) domains |
| `adminUsers` | `array` | Array of admin user emails. |
| `isSsoEnabled` | `string` | Indicates whether SSO is enabled or not |
| `metadataUrl` | `string` | URL for Azure AD metadata |
| `singleSignOnUrl` | `string` | The login URL specific to this Dynatrace Environment |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId, data__userPrincipal` |
