---
title: network_acl_entry
hide_title: false
hide_table_of_contents: false
keywords:
  - network_acl_entry
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_acl_entry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_acl_entry</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_acl_entry_Create` | `INSERT` | `Egress, NetworkAclId, Protocol, RuleAction, RuleNumber` | &lt;p&gt;Creates an entry (a rule) in a network ACL with the specified rule number. Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the ACL, we process the entries in the ACL according to the rule numbers, in ascending order. Each network ACL has a set of ingress rules and a separate set of egress rules.&lt;/p&gt; &lt;p&gt;We recommend that you leave room between the rule numbers (for example, 100, 110, 120, ...), and not number them one right after the other (for example, 101, 102, 103, ...). This makes it easier to add a rule between existing ones without having to renumber the rules.&lt;/p&gt; &lt;p&gt;After you add an entry, you can't modify it; you must either replace it, or create an entry and delete the old one.&lt;/p&gt; &lt;p&gt;For more information about network ACLs, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html"&gt;Network ACLs&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `network_acl_entry_Delete` | `DELETE` | `Egress, NetworkAclId, RuleNumber` | Deletes the specified ingress or egress entry (rule) from the specified network ACL. |
| `network_acl_entry_Replace` | `EXEC` | `Egress, NetworkAclId, Protocol, RuleAction, RuleNumber` | Replaces an entry (rule) in a network ACL. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html"&gt;Network ACLs&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;. |
