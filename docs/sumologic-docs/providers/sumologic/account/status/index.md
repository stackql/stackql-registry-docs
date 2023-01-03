---
title: status
hide_title: false
hide_table_of_contents: false
keywords:
  - status
  - account
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.account.status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `planType` | `string` | Whether the account is `Free`/`Trial`/`Paid` |
| `pricingModel` | `string` | Whether the account is `cloudflex` or `credits` |
| `accountActivated` | `boolean` | If the account is activated or not |
| `applicationUse` | `string` | The current usage of the application. |
| `canUpdatePlan` | `boolean` | If the plan can be updated by the given user |
| `planExpirationDays` | `integer` | The number of days in which the plan will expire |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getStatus` | `SELECT` |  |
