---
title: questions
hide_title: false
hide_table_of_contents: false
keywords:
  - questions
  - userfactor
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>questions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.userfactor.questions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `question` | `string` |
| `questionText` | `string` |
| `answer` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `userId, subdomain` |
