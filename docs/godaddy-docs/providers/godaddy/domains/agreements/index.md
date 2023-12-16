---
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
  - domains
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.domains.agreements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `agreementKey` | `string` | Unique identifier for the legal agreement |
| `content` | `string` | Contents of the legal agreement, suitable for embedding |
| `title` | `string` | Title of the legal agreement |
| `url` | `string` | URL to a page containing the legal agreement |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_agreement` | `SELECT` | `privacy, tlds` |
