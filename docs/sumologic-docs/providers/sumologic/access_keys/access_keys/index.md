---
title: access_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - access_keys
  - access_keys
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
<tr><td><b>Name</b></td><td><code>access_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.access_keys.access_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the access key. |
| `label` | `string` | The name of the access key. |
| `lastUsed` | `string` | Last used timestamp in UTC.  &lt;br&gt; **Note:** Property not in use, it is part of an upcoming feature. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `corsHeaders` | `array` | An array of domains for which the access key is valid. Whether Sumo Logic accepts or rejects an API request depends on whether it contains an ORIGIN header and the entries in the allowlist. Sumo Logic will reject:<br />  1. Requests with an ORIGIN header but the allowlist is empty.<br />  2. Requests with an ORIGIN header that don't match any entry in the allowlist. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `createdBy` | `string` | Identifier of the user who created the access key. |
| `disabled` | `boolean` | Indicates whether the access key is disabled or not. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listAccessKeys` | `SELECT` |  | List all access keys in your account. |
| `createAccessKey` | `INSERT` | `data__label` | Creates a new access ID and key pair. The new access key can be used from the domains specified in corsHeaders field. Whether Sumo Logic accepts or rejects an API request depends on whether it contains an ORIGIN header and the entries in the allowlist. Sumo Logic will reject:<br />  1. Requests with an ORIGIN header but the allowlist is empty.<br />  2. Requests with an ORIGIN header that don't match any entry in the allowlist. |
| `deleteAccessKey` | `DELETE` | `id` | Deletes the access key with the given accessId. |
| `updateAccessKey` | `EXEC` | `id, data__disabled` | Updates the properties of existing accessKey by accessId. It can be used to enable or disable the access key and to update the corsHeaders list. |
