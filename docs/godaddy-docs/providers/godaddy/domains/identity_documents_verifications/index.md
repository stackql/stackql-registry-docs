---
title: identity_documents_verifications
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_documents_verifications
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
<tr><td><b>Name</b></td><td><code>identity_documents_verifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.domains.identity_documents_verifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `createdAt` | `string` | Timestamp indicating when the user created the identity document verification job |
| `status` | `string` |  |
| `tld` | `string` | Top level domain the current identity document verification is for |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_identity_document_verification` | `SELECT` | `identity_document_id` | Retrieve a list of Verifications for the specified Identity Document |
| `create_verification` | `INSERT` | `identity_document_id, tlds` | Only one verification job is needed for one TLD, Top Level Domain, per identity document. Sending in request(s) with multiple domains for the same TLD, will not create multiple verification jobs. We accept domain names for the convenience of our customers so that they don't need to worry about parsing TLDs out of domain names |
