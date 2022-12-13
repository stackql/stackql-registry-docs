---
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - datadog
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
<tr><td><b>Name</b></td><td><code>marketplace_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.datadog.marketplace_agreements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the resource. |
| `name` | `string` | Name of the agreement. |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | Terms properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MarketplaceAgreements_List` | `SELECT` | `subscriptionId` |
| `MarketplaceAgreements_CreateOrUpdate` | `INSERT` | `subscriptionId` |
