---
title: accounts__ad_blocking_recovery_tag
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts__ad_blocking_recovery_tag
  - adsense
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts__ad_blocking_recovery_tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.accounts__ad_blocking_recovery_tag</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tag` | `string` | The ad blocking recovery tag. Note that the message generated by the tag can be blocked by an ad blocking extension. If this is not your desired outcome, then you'll need to use it in conjunction with the error protection code. |
| `errorProtectionCode` | `string` | Error protection code that can be used in conjunction with the tag. It'll display a message to users if an [ad blocking extension blocks their access to your site](https://support.google.com/adsense/answer/11575480). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_getAdBlockingRecoveryTag` | `SELECT` | `accountsId` |
