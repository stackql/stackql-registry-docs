---
title: hosted_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_zones
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
Retrieves a list of <code>hosted_zones</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.hosted_zones</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HostedZoneConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>HostedZoneTags</code></td><td><code>array</code></td><td>Adds, edits, or deletes tags for a health check or a hosted zone.

For information about using tags for cost allocation, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the domain. Specify a fully qualified domain name, for example, www.example.com. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.

If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that are returned by the Fn::GetAtt intrinsic function.</td></tr><tr><td><code>QueryLoggingConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>VPCs</code></td><td><code>array</code></td><td>A complex type that contains information about the VPCs that are associated with the specified hosted zone.</td></tr><tr><td><code>NameServers</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.route53.hosted_zones
WHERE region = 'us-east-1'
```
