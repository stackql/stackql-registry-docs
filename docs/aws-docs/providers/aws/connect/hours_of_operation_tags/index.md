---
title: hours_of_operation_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - hours_of_operation_tags
  - connect
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

Expands all tag keys and values for <code>hours_of_operations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hours_of_operation_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::HoursOfOperation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.hours_of_operation_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the hours of operation.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the hours of operation.</td></tr>
<tr><td><CopyableCode code="time_zone" /></td><td><code>string</code></td><td>The time zone of the hours of operation.</td></tr>
<tr><td><CopyableCode code="config" /></td><td><code>array</code></td><td>Configuration information for the hours of operation: day, start time, and end time.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the hours of operation.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_overrides" /></td><td><code>array</code></td><td>One or more hours of operation overrides assigned to an hour of operation.</td></tr>
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
Expands tags for all <code>hours_of_operations</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
description,
time_zone,
config,
hours_of_operation_arn,
hours_of_operation_overrides,
tag_key,
tag_value
FROM aws.connect.hours_of_operation_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>hours_of_operation_tags</code> resource, see <a href="/providers/aws/connect/hours_of_operations/#permissions"><code>hours_of_operations</code></a>

