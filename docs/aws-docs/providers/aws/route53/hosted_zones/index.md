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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>hosted_zones</code> in a region or create a <code>hosted_zones</code> resource, use <code>hosted_zone</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs). &lt;br&#x2F;&gt;  You can't convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.&lt;br&#x2F;&gt;  For more information about charges for hosted zones, see &#91;Amazon Route 53 Pricing&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;route53&#x2F;pricing&#x2F;).&lt;br&#x2F;&gt; Note the following:&lt;br&#x2F;&gt;  +  You can't create a hosted zone for a top-level domain (TLD) such as .com.&lt;br&#x2F;&gt;  +  If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see &#91;Migrating DNS Service for an Existing Domain to Amazon Route 53&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;Route53&#x2F;latest&#x2F;DeveloperGuide&#x2F;MigratingDNS.html) in the *Amazon Route 53 Developer Guide*. &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; When you submit a ``CreateHostedZone`` request, the initial status of the hosted zone is ``PENDING``. For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to ``INSYNC``.&lt;br&#x2F;&gt; The ``CreateHostedZone`` request requires the caller to have an ``ec2:DescribeVpcs`` permission.&lt;br&#x2F;&gt;  When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of AWS-Regions. Each AWS-account is scoped to one partition.&lt;br&#x2F;&gt; The following are the supported partitions:&lt;br&#x2F;&gt;  +   ``aws`` - AWS-Regions &lt;br&#x2F;&gt;  +   ``aws-cn`` - China Regions&lt;br&#x2F;&gt;  +   ``aws-us-gov`` - govcloud-us-region &lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information, see &#91;Access Management&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.hosted_zones" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.route53.hosted_zones

```

## Permissions

To operate on the <code>hosted_zones</code> resource, the following permissions are required:

### Create
```json
route53:CreateHostedZone,
route53:CreateQueryLoggingConfig,
route53:ChangeTagsForResource,
route53:GetChange,
route53:AssociateVPCWithHostedZone,
ec2:DescribeVpcs
```

### List
```json
route53:GetHostedZone,
route53:ListHostedZones,
route53:ListHostedZonesByName,
route53:ListQueryLoggingConfigs,
route53:ListTagsForResource
```

