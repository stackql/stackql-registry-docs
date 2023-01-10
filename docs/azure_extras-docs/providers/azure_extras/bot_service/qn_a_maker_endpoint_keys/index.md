---
title: qn_a_maker_endpoint_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - qn_a_maker_endpoint_keys
  - bot_service
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>qn_a_maker_endpoint_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.bot_service.qn_a_maker_endpoint_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `installedVersion` | `string` | Current version of runtime. |
| `lastStableVersion` | `string` | Latest version of runtime. |
| `primaryEndpointKey` | `string` | Primary Access Key. |
| `secondaryEndpointKey` | `string` | Secondary Access Key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `QnAMakerEndpointKeys_Get` | `SELECT` | `subscriptionId` |
