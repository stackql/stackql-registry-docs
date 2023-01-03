---
title: balance
hide_title: false
hide_table_of_contents: false
keywords:
  - balance
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>balance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.balance</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_developers_balance_adjust` | `EXEC` | `developersId, organizationsId` | Adjust the prepaid balance for the developer. This API will be used in scenarios where the developer has been under-charged or over-charged. |
| `organizations_developers_balance_credit` | `EXEC` | `developersId, organizationsId` | Credits the account balance for the developer. |
