---
title: personal
hide_title: false
hide_table_of_contents: false
keywords:
  - personal
  - access_keys
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>personal</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.access_keys.personal</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the access key. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `corsHeaders` | `array` | An array of domains for which the access key is valid. Whether Sumo Logic accepts or rejects an API request depends on whether it contains an ORIGIN header and the entries in the allowlist. Sumo Logic will reject:<br />  1. Requests with an ORIGIN header but the allowlist is empty.<br />  2. Requests with an ORIGIN header that don't match any entry in the allowlist. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `createdBy` | `string` | Identifier of the user who created the access key. |
| `disabled` | `boolean` | Indicates whether the access key is disabled or not. |
| `label` | `string` | The name of the access key. |
| `lastUsed` | `string` | Last used timestamp in UTC.  &lt;br&gt; **Note:** Property not in use, it is part of an upcoming feature. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listPersonalAccessKeys` | `SELECT` |  |
