---
title: ingress_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - ingress_rules
  - appengine
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
<tr><td><b>Name</b></td><td><code>ingress_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.ingress_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | An optional string description of this rule. This field has a maximum length of 400 characters. |
| `sourceRange` | `string` | IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. Truncation will be silently performed on addresses which are not properly truncated. For example, 1.2.3.4/24 is accepted as the same address as 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 is accepted as the same address as 2001:db8::/32. |
| `action` | `string` | The action to take on matched requests. |
| `priority` | `integer` | A positive integer between 1, Int32.MaxValue-1 that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `apps_firewall_ingressRules_get` | `SELECT` | `appsId, ingressRulesId` | Gets the specified firewall rule. |
| `apps_firewall_ingressRules_list` | `SELECT` | `appsId` | Lists the firewall rules of an application. |
| `apps_firewall_ingressRules_create` | `INSERT` | `appsId` | Creates a firewall rule for the application. |
| `apps_firewall_ingressRules_delete` | `DELETE` | `appsId, ingressRulesId` | Deletes the specified firewall rule. |
| `apps_firewall_ingressRules_batchUpdate` | `EXEC` | `appsId` | Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list. |
| `apps_firewall_ingressRules_patch` | `EXEC` | `appsId, ingressRulesId` | Updates the specified firewall rule. |
