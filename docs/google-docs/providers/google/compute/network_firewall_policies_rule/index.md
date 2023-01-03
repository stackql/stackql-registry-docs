---
title: network_firewall_policies_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - network_firewall_policies_rule
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
<tr><td><b>Name</b></td><td><code>network_firewall_policies_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.network_firewall_policies_rule</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | An optional description for this resource. |
| `action` | `string` | The Action to perform when the client connection triggers the rule. Can currently be either "allow" or "deny()" where valid values for status are 403, 404, and 502. |
| `targetSecureTags` | `array` | A list of secure tags that controls which instances the firewall rule applies to. If targetSecureTag are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the target_secure_tag are in INEFFECTIVE state, then this rule will be ignored. targetSecureTag may not be set at the same time as targetServiceAccounts. If neither targetServiceAccounts nor targetSecureTag are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256. |
| `direction` | `string` | The direction in which this rule applies. |
| `kind` | `string` | [Output only] Type of the resource. Always compute#firewallPolicyRule for firewall policy rules |
| `ruleTupleCount` | `integer` | [Output Only] Calculation of the complexity of a single firewall policy rule. |
| `priority` | `integer` | An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority. |
| `disabled` | `boolean` | Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. |
| `ruleName` | `string` | An optional name for the rule. This field is not a unique identifier and can be updated. |
| `targetResources` | `array` | A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. |
| `enableLogging` | `boolean` | Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. |
| `targetServiceAccounts` | `array` | A list of service accounts indicating the sets of instances that are applied with this rule. |
| `match` | `object` | Represents a match condition that incoming traffic is evaluated against. Exactly one field must be specified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `networkFirewallPolicies_getRule` | `SELECT` | `firewallPolicy, project` | Gets a rule of the specified priority. |
| `networkFirewallPolicies_addRule` | `INSERT` | `firewallPolicy, project` | Inserts a rule into a firewall policy. |
| `networkFirewallPolicies_removeRule` | `DELETE` | `firewallPolicy, project` | Deletes a rule of the specified priority. |
