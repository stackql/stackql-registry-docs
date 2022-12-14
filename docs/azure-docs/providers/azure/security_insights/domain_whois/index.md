---
title: domain_whois
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_whois
  - security_insights
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
<tr><td><b>Name</b></td><td><code>domain_whois</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.domain_whois</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `created` | `string` | The timestamp at which this record was created |
| `domain` | `string` | The domain for this whois record |
| `expires` | `string` | The timestamp at which this record will expire |
| `parsedWhois` | `object` | The whois record for a given domain |
| `server` | `string` | The hostname of this registrar's whois server |
| `updated` | `string` | The timestamp at which this record was last updated |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DomainWhois_Get` | `SELECT` | `domain, resourceGroupName, subscriptionId` |
