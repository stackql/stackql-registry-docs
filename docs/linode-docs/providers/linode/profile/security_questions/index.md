---
title: security_questions
hide_title: false
hide_table_of_contents: false
keywords:
  - security_questions
  - profile
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_questions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.profile.security_questions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getSecurityQuestions` | `SELECT` |  | Returns a collection of security questions and their responses, if any, for your User Profile.<br /> |
| `_getSecurityQuestions` | `EXEC` |  | Returns a collection of security questions and their responses, if any, for your User Profile.<br /> |
| `postSecurityQuestions` | `EXEC` |  | Adds security question responses for your User.<br /><br />Requires exactly three unique questions.<br /><br />Previous responses are overwritten if answered or reset to `null` if unanswered.<br /><br />**Note**: Security questions must be answered for your User prior to accessing the **Two Factor Secret Create** ([POST /profile/tfa-enable](/docs/api/profile/#two-factor-secret-create)) command.<br /> |
