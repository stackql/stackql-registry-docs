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
<tr><td><b>Description</b></td><td>Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs). &lt;br&#x2F;&gt;  You can't convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.&lt;br&#x2F;&gt;  For more information about charges for hosted zones, see &#91;Amazon Route 53 Pricing&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;route53&#x2F;pricing&#x2F;).&lt;br&#x2F;&gt; Note the following:&lt;br&#x2F;&gt;  +  You can't create a hosted zone for a top-level domain (TLD) such as .com.&lt;br&#x2F;&gt;  +  If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see &#91;Migrating DNS Service for an Existing Domain to Amazon Route 53&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;DeveloperGuide&#x2F;MigratingDNS.html) in the *Amazon Route 53 Developer Guide*. &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; When you submit a ``CreateHostedZone`` request, the initial status of the hosted zone is ``PENDING``. For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to ``INSYNC``.&lt;br&#x2F;&gt; The ``CreateHostedZone`` request requires the caller to have an ``ec2:DescribeVpcs`` permission.&lt;br&#x2F;&gt;  When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of AWS-Regions. Each AWS-account is scoped to one partition.&lt;br&#x2F;&gt; The following are the supported partitions:&lt;br&#x2F;&gt;  +   ``aws`` - AWS-Regions &lt;br&#x2F;&gt;  +   ``aws-cn`` - China Regions&lt;br&#x2F;&gt;  +   ``aws-us-gov`` - govcloud-us-region &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information, see &#91;Access Management&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.hosted_zone</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hosted_zone_config</code></td><td><code>object</code></td><td>A complex type that contains an optional comment.&lt;br&#x2F;&gt; If you don't want to specify a comment, omit the ``HostedZoneConfig`` and ``Comment`` elements.</td></tr>
<tr><td><code>hosted_zone_tags</code></td><td><code>array</code></td><td>Adds, edits, or deletes tags for a health check or a hosted zone.&lt;br&#x2F;&gt; For information about using tags for cost allocation, see &#91;Using Cost Allocation Tags&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;awsaccountbilling&#x2F;latest&#x2F;aboutv2&#x2F;cost-alloc-tags.html) in the *User Guide*.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the domain. Specify a fully qualified domain name, for example, *www.example.com*. The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical.&lt;br&#x2F;&gt; If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of ``NameServers`` that are returned by the ``Fn::GetAtt`` intrinsic function.</td></tr>
<tr><td><code>query_logging_config</code></td><td><code>object</code></td><td>Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.&lt;br&#x2F;&gt; DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:&lt;br&#x2F;&gt;  +  Route 53 edge location that responded to the DNS query&lt;br&#x2F;&gt;  +  Domain or subdomain that was requested&lt;br&#x2F;&gt;  +  DNS record type, such as A or AAAA&lt;br&#x2F;&gt;  +  DNS response code, such as ``NoError`` or ``ServFail`` &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  + Log Group and Resource Policy Before you create a query logging configuration, perform the following operations. If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically. Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following: You must create the log group in the us-east-1 region. You must use the same to create the log group and the hosted zone that you want to configure query logging for. When you create log groups for query logging, we recommend that you use a consistent prefix, for example: &#x2F;aws&#x2F;route53&#x2F;hosted zone name In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated resources, such as Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging. Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. For the value of Resource, specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with *, for example: arn:aws:logs:us-east-1:123412341234:log-group:&#x2F;aws&#x2F;route53&#x2F;* To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values: For aws:SourceArn, supply the hosted zone ARN used in creating the query logging configuration. For example, aws:SourceArn: arn:aws:route53:::hostedzone&#x2F;hosted zone ID. For aws:SourceAccount, supply the account ID for the account that creates the query logging configuration. For example, aws:SourceAccount:111111111111. For more information, see The confused deputy problem in the IAM User Guide. You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the SDKs, or the . + Log Streams and Edge Locations When Route 53 finishes creating the configuration for DNS query logging, it does the following: Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location. Begins to send query logs to the applicable log stream. The name of each log stream is in the following format: hosted zone ID&#x2F;edge location code The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the Route 53 Product Details page. + Queries That Are Logged Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see Routing Internet Traffic to Your Website or Web Application in the Amazon Route 53 Developer Guide. + Log File Format For a list of the values in each query log and the format of each value, see Logging DNS Queries in the Amazon Route 53 Developer Guide. + Pricing For information about charges for query logs, see Amazon CloudWatch Pricing. + How to Stop Logging If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see DeleteQueryLoggingConfig.</td></tr>
<tr><td><code>vpcs</code></td><td><code>array</code></td><td>*Private hosted zones:* A complex type that contains information about the VPCs that are associated with the specified hosted zone.&lt;br&#x2F;&gt;  For public hosted zones, omit ``VPCs``, ``VPCId``, and ``VPCRegion``.</td></tr>
<tr><td><code>name_servers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
hosted_zone_config,
hosted_zone_tags,
name,
query_logging_config,
vpcs,
name_servers
FROM aws.route53.hosted_zone
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>hosted_zone</code> resource, the following permissions are required:

### Read
```json
route53:GetHostedZone,
route53:ListTagsForResource,
route53:ListQueryLoggingConfigs
```

### Update
```json
route53:GetChange,
route53:ListTagsForResource,
route53:UpdateHostedZoneComment,
route53:ChangeTagsForResource,
route53:AssociateVPCWithHostedZone,
route53:DisassociateVPCFromHostedZone,
route53:CreateQueryLoggingConfig,
route53:DeleteQueryLoggingConfig,
ec2:DescribeVpcs
```

### Delete
```json
route53:DeleteHostedZone,
route53:DeleteQueryLoggingConfig,
route53:ListQueryLoggingConfigs,
route53:GetChange
```

