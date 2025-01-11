---
title: hosted_zones_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - hosted_zones_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>hosted_zones</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/hosted_zones/"><code>hosted_zones</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosted_zones_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs). <br />You can't convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.<br />For more information about charges for hosted zones, see &#91;Amazon Route 53 Pricing&#93;(https://docs.aws.amazon.com/route53/pricing/).<br />Note the following:<br />+ You can't create a hosted zone for a top-level domain (TLD) such as .com.<br />+ If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see &#91;Migrating DNS Service for an Existing Domain to Amazon Route 53&#93;(https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html) in the *Amazon Route 53 Developer Guide*. <br /><br />When you submit a <code>CreateHostedZone</code> request, the initial status of the hosted zone is <code>PENDING</code>. For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to <code>INSYNC</code>.<br />The <code>CreateHostedZone</code> request requires the caller to have an <code>ec2:DescribeVpcs</code> permission.<br />When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of AWS-Regions. Each AWS-account is scoped to one partition.<br />The following are the supported partitions:<br />+ <code>aws</code> - AWS-Regions <br />+ <code>aws-cn</code> - China Regions<br />+ <code>aws-us-gov</code> - govcloud-us-region <br /><br />For more information, see &#91;Access Management&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.hosted_zones_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>hosted_zones</code> in a region.
```sql
SELECT
region,
id
FROM aws.route53.hosted_zones_list_only
;
```


## Permissions

For permissions required to operate on the <code>hosted_zones_list_only</code> resource, see <a href="/providers/aws/route53/hosted_zones/#permissions"><code>hosted_zones</code></a>

