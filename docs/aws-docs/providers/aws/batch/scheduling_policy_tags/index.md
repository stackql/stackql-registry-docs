---
title: scheduling_policy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduling_policy_tags
  - batch
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

Expands all tag keys and values for <code>scheduling_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduling_policy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type schema for AWS::Batch::SchedulingPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.scheduling_policy_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Scheduling Policy.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the Scheduling Policy.</td></tr>
<tr><td><CopyableCode code="fairshare_policy" /></td><td><code>object</code></td><td>Fair Share Policy for the Job Queue.</td></tr>
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
Expands tags for all <code>scheduling_policies</code> in a region.
```sql
SELECT
region,
name,
arn,
fairshare_policy,
tag_key,
tag_value
FROM aws.batch.scheduling_policy_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scheduling_policy_tags</code> resource, see <a href="/providers/aws/batch/scheduling_policies/#permissions"><code>scheduling_policies</code></a>


