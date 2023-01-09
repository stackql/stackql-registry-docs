---
title: returncarrier
hide_title: false
hide_table_of_contents: false
keywords:
  - returncarrier
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>returncarrier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.returncarrier</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_returncarrier_list` | `SELECT` | `accountId` | Lists available return carriers in the merchant account. |
| `accounts_returncarrier_create` | `INSERT` | `accountId` | Links return carrier to a merchant account. |
| `accounts_returncarrier_delete` | `DELETE` | `accountId, carrierAccountId` | Delete a return carrier in the merchant account. |
| `accounts_returncarrier_patch` | `EXEC` | `accountId, carrierAccountId` | Updates a return carrier in the merchant account. |
