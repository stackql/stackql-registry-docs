---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - tagmanager
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Account display name. @mutable tagmanager.accounts.create @mutable tagmanager.accounts.update |
| `accountId` | `string` | The Account ID uniquely identifies the GTM Account. |
| `features` | `object` |  |
| `fingerprint` | `string` | The fingerprint of the GTM Account as computed at storage time. This value is recomputed whenever the account is modified. |
| `path` | `string` | GTM Account's API relative path. |
| `shareData` | `boolean` | Whether the account shares data anonymously with Google and others. This flag enables benchmarking by sharing your data in an anonymous form. Google will remove all identifiable information about your website, combine the data with hundreds of other anonymous sites and report aggregate trends in the benchmarking service. @mutable tagmanager.accounts.create @mutable tagmanager.accounts.update |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountsId` | Gets a GTM Account. |
| `list` | `SELECT` |  | Lists all GTM Accounts that a user has access to. |
| `update` | `EXEC` | `accountsId` | Updates a GTM Account. |
