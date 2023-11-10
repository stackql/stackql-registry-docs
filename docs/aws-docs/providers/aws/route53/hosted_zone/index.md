---
title: hosted_zone
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_zone
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>hosted_zone</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_zone</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hosted_zone</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.hosted_zone</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hosted_zone_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>hosted_zone_tags</code></td><td><code>array</code></td><td>Adds, edits, or deletes tags for a health check or a hosted zone.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.</td></tr>
<tr><td><code>query_logging_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>v_pcs</code></td><td><code>array</code></td><td>A complex type that contains information about the VPCs that are associated with the specified hosted zone.</td></tr>
<tr><td><code>name_servers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
hosted_zone_config,
hosted_zone_tags,
name,
query_logging_config,
v_pcs,
name_servers
FROM aws.route53.hosted_zone
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
