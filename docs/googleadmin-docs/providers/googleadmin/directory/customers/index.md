---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.customers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for the customer's Google Workspace account. (Readonly) |
| `kind` | `string` | Identifies the resource as a customer. Value: `admin#directory#customer` |
| `etag` | `string` | ETag of the resource. |
| `customerCreationTime` | `string` | The customer's creation time (Readonly) |
| `customerDomain` | `string` | The customer's primary domain name string. Do not include the `www` prefix when creating a new customer. |
| `language` | `string` | The customer's ISO 639-2 language code. See the [Language Codes](/admin-sdk/directory/v1/languages) page for the list of supported codes. Valid language codes outside the supported set will be accepted by the API but may lead to unexpected behavior. The default value is `en`. |
| `phoneNumber` | `string` | The customer's contact phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. |
| `postalAddress` | `object` |  |
| `alternateEmail` | `string` | The customer's secondary contact email address. This email address cannot be on the same domain as the `customerDomain` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customerKey` | Retrieves a customer. |
| `patch` | `EXEC` | `customerKey` | Patches a customer. |
| `update` | `EXEC` | `customerKey` | Updates a customer. |
