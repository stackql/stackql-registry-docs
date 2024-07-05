---
title: aggregation_authorization_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregation_authorization_tags
  - config
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

Expands all tag keys and values for <code>aggregation_authorizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aggregation_authorization_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::AggregationAuthorization</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.aggregation_authorization_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="authorized_account_id" /></td><td><code>string</code></td><td>The 12-digit account ID of the account authorized to aggregate data.</td></tr>
<tr><td><CopyableCode code="authorized_aws_region" /></td><td><code>string</code></td><td>The region authorized to collect aggregated data.</td></tr>
<tr><td><CopyableCode code="aggregation_authorization_arn" /></td><td><code>string</code></td><td>The ARN of the AggregationAuthorization.</td></tr>
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
Expands tags for all <code>aggregation_authorizations</code> in a region.
```sql
SELECT
region,
authorized_account_id,
authorized_aws_region,
aggregation_authorization_arn,
tag_key,
tag_value
FROM aws.config.aggregation_authorization_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>aggregation_authorization_tags</code> resource, see <a href="/providers/aws/config/aggregation_authorizations/#permissions"><code>aggregation_authorizations</code></a>


