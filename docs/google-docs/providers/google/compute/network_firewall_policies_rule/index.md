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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `kind` | `string` | [Output only] Type of the resource. Always compute#firewallPolicyRule for firewall policy rules |
| `match` | `object` | Represents a match condition that incoming traffic is evaluated against. Exactly one field must be specified. |
| `ruleName` | `string` | An optional name for the rule. This field is not a unique identifier and can be updated. |
| `enableLogging` | `boolean` | Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. |
| `ruleTupleCount` | `integer` | [Output Only] Calculation of the complexity of a single firewall policy rule. |
| `action` | `string` | The Action to perform when the client connection triggers the rule. Valid actions are "allow", "deny" and "goto_next". |
| `direction` | `string` | The direction in which this rule applies. |
| `disabled` | `boolean` | Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. |
| `targetServiceAccounts` | `array` | A list of service accounts indicating the sets of instances that are applied with this rule. |
| `priority` | `integer` | An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest prority. |
| `targetSecureTags` | `array` | A list of secure tags that controls which instances the firewall rule applies to. If targetSecureTag are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the target_secure_tag are in INEFFECTIVE state, then this rule will be ignored. targetSecureTag may not be set at the same time as targetServiceAccounts. If neither targetServiceAccounts nor targetSecureTag are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256. |
| `targetResources` | `array` | A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_rule` | `SELECT` | `firewallPolicy, project` | Gets a rule of the specified priority. |
| `add_rule` | `EXEC` | `firewallPolicy, project` | Inserts a rule into a firewall policy. |
| `remove_rule` | `EXEC` | `firewallPolicy, project` | Deletes a rule of the specified priority. |
