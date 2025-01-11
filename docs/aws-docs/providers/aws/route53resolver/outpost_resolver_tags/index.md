---
title: outpost_resolver_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - outpost_resolver_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>outpost_resolvers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outpost_resolver_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::OutpostResolver.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.outpost_resolver_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The OutpostResolver name.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The OutpostResolver ARN.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Outpost ARN.</td></tr>
<tr><td><CopyableCode code="preferred_instance_type" /></td><td><code>string</code></td><td>The OutpostResolver instance type.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.</td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td>The OutpostResolver status message.</td></tr>
<tr><td><CopyableCode code="instance_count" /></td><td><code>integer</code></td><td>The number of OutpostResolvers.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The OutpostResolver creation time</td></tr>
<tr><td><CopyableCode code="modification_time" /></td><td><code>string</code></td><td>The OutpostResolver last modified time</td></tr>
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
Expands tags for all <code>outpost_resolvers</code> in a region.
```sql
SELECT
region,
id,
creator_request_id,
name,
arn,
outpost_arn,
preferred_instance_type,
status,
status_message,
instance_count,
creation_time,
modification_time,
tag_key,
tag_value
FROM aws.route53resolver.outpost_resolver_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>outpost_resolver_tags</code> resource, see <a href="/providers/aws/route53resolver/outpost_resolvers/#permissions"><code>outpost_resolvers</code></a>

