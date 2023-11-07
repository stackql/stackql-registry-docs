---
title: firewall_domain_list
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_domain_list
  - route53resolver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>firewall_domain_list</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_domain_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_domain_list</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.firewall_domain_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>FirewallDomainListName</td></tr>
<tr><td><code>DomainCount</code></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.</td></tr>
<tr><td><code>StatusMessage</code></td><td><code>string</code></td><td>FirewallDomainListAssociationStatus</td></tr>
<tr><td><code>ManagedOwnerName</code></td><td><code>string</code></td><td>ServicePrincipal</td></tr>
<tr><td><code>CreatorRequestId</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>ModificationTime</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
<tr><td><code>Domains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DomainFileUrl</code></td><td><code>string</code></td><td>S3 URL to import domains from.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.route53resolver.firewall_domain_list<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
