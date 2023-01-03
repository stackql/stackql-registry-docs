---
title: response_policy_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - response_policy_rules
  - dns
  - google    
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
<tr><td><b>Name</b></td><td><code>response_policy_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.response_policy_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `localData` | `object` |  |
| `ruleName` | `string` | An identifier for this rule. Must be unique with the ResponsePolicy. |
| `behavior` | `string` | Answer this query with a behavior rather than DNS data. |
| `dnsName` | `string` | The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule. |
| `kind` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `responsePolicyRules_get` | `SELECT` | `project, responsePolicy, responsePolicyRule` | Fetches the representation of an existing Response Policy Rule. |
| `responsePolicyRules_list` | `SELECT` | `project, responsePolicy` | Enumerates all Response Policy Rules associated with a project. |
| `responsePolicyRules_create` | `INSERT` | `project, responsePolicy` | Creates a new Response Policy Rule. |
| `responsePolicyRules_delete` | `DELETE` | `project, responsePolicy, responsePolicyRule` | Deletes a previously created Response Policy Rule. |
| `responsePolicyRules_patch` | `EXEC` | `project, responsePolicy, responsePolicyRule` | Applies a partial update to an existing Response Policy Rule. |
| `responsePolicyRules_update` | `EXEC` | `project, responsePolicy, responsePolicyRule` | Updates an existing Response Policy Rule. |
