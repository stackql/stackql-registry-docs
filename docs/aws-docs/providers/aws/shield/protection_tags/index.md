---
title: protection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_tags
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

Expands all tag keys and values for <code>protections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="protection_id" /></td><td><code>string</code></td><td>The unique identifier (ID) of the protection.</td></tr>
<tr><td><CopyableCode code="protection_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Friendly name for the Protection.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the resource to be protected.</td></tr>
<tr><td><CopyableCode code="health_check_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the health check to associate with the protection.</td></tr>
<tr><td><CopyableCode code="application_layer_automatic_response_configuration" /></td><td><code>object</code></td><td>The automatic application layer DDoS mitigation settings for a Protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>protections</code> in a region.
```sql
SELECT
region,
protection_id,
protection_arn,
name,
resource_arn,
health_check_arns,
application_layer_automatic_response_configuration,
tag_key,
tag_value
FROM aws.shield.protection_tags
;
```


## Permissions

For permissions required to operate on the <code>protection_tags</code> resource, see <a href="/providers/aws/shield/protections/#permissions"><code>protections</code></a>


