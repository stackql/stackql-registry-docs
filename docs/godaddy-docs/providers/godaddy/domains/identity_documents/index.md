---
title: identity_documents
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_documents
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
<tr><td><b>Name</b></td><td><code>identity_documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.domains.identity_documents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contact` | `object` |  |
| `identificationCountry` | `string` | Two-letter ISO country code to be used as a hint for target region NOTE: These are sample values, there are many  more  |
| `identificationNumber` | `string` | Individual or business identification number written on the document. Must match image exactly |
| `identificationType` | `string` | Type of the identity document |
| `identityDocumentId` | `string` | The unique identifier of an identity document |
| `legalEntityName` | `string` | Individual or business name written on the document. Must match image exactly |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_identity_documents` | `SELECT` |  | Get a collection of identity documents the current shopper owns |
| `create_identity_document` | `INSERT` | `data__contact, data__identificationCountry, data__identificationNumber, data__identificationType, data__image, data__legalEntityName` | Create an Identity Document from uploaded image |
