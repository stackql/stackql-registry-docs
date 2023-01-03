---
title: sms
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.template.sms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `type` | `string` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `template` | `string` |
| `translations` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `templateId` | Fetches a specific template by `id` |
| `list` | `SELECT` |  | Enumerates custom SMS templates in your organization. A subset of templates can be returned that match a template type. |
| `insert` | `INSERT` |  | Adds a new custom SMS template to your organization. |
| `delete` | `DELETE` | `templateId` | Removes an SMS template. |
| `partialUpdate` | `EXEC` | `templateId` | Updates only some of the SMS template properties: |
| `update` | `EXEC` | `templateId` | Updates the SMS template. |
