---
title: security_policies_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies_rule
  - compute
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
<tr><td><b>Name</b></td><td><code>security_policies_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.security_policies_rule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `rateLimitOptions` | `object` |  |
| `kind` | `string` | [Output only] Type of the resource. Always compute#securityPolicyRule for security policy rules |
| `headerAction` | `object` |  |
| `match` | `object` | Represents a match condition that incoming traffic is evaluated against. Exactly one field must be specified. |
| `priority` | `integer` | An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. |
| `redirectOptions` | `object` |  |
| `preview` | `boolean` | If set to true, the specified action is not enforced. |
| `action` | `string` | The Action to perform when the rule is matched. The following are the valid actions: - allow: allow access to target. - deny(): deny access to target, returns the HTTP response code specified (valid values are 403, 404, and 502). - rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set. - redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. - throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `securityPolicies_getRule` | `SELECT` | `project, securityPolicy` | Gets a rule at the specified priority. |
| `securityPolicies_addRule` | `INSERT` | `project, securityPolicy` | Inserts a rule into a security policy. |
| `securityPolicies_removeRule` | `DELETE` | `project, securityPolicy` | Deletes a rule at the specified priority. |
