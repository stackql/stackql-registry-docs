---
title: subscriber_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriber_tags
  - securitylake
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

Expands all tag keys and values for <code>subscribers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriber_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::Subscriber</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securitylake.subscriber_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_types" /></td><td><code>array</code></td><td>The Amazon S3 or AWS Lake Formation access type.</td></tr>
<tr><td><CopyableCode code="data_lake_arn" /></td><td><code>string</code></td><td>The ARN for the data lake.</td></tr>
<tr><td><CopyableCode code="subscriber_identity" /></td><td><code>object</code></td><td>The AWS identity used to access your data.</td></tr>
<tr><td><CopyableCode code="subscriber_name" /></td><td><code>string</code></td><td>The name of your Security Lake subscriber account.</td></tr>
<tr><td><CopyableCode code="subscriber_description" /></td><td><code>string</code></td><td>The description for your subscriber account in Security Lake.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>The supported AWS services from which logs and events are collected.</td></tr>
<tr><td><CopyableCode code="resource_share_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_share_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subscriber_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_bucket_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subscriber_arn" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>subscribers</code> in a region.
```sql
SELECT
region,
access_types,
data_lake_arn,
subscriber_identity,
subscriber_name,
subscriber_description,
sources,
resource_share_arn,
resource_share_name,
subscriber_role_arn,
s3_bucket_arn,
subscriber_arn,
tag_key,
tag_value
FROM aws.securitylake.subscriber_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>subscriber_tags</code> resource, see <a href="/providers/aws/securitylake/subscribers/#permissions"><code>subscribers</code></a>

