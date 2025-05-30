---
title: protections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - protections_list_only
  - shield
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

Lists <code>protections</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/protections/"><code>protections</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protections_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="protection_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection.</td></tr>
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
Lists all <code>protections</code> in a region.
```sql
SELECT
region,
protection_arn
FROM aws.shield.protections_list_only
;
```


## Permissions

For permissions required to operate on the <code>protections_list_only</code> resource, see <a href="/providers/aws/shield/protections/#permissions"><code>protections</code></a>

