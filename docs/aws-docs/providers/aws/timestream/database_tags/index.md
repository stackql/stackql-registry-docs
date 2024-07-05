---
title: database_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - database_tags
  - timestream
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

Expands all tag keys and values for <code>databases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::Database resource creates a Timestream database.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.database_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name for the database. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the database name.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key for the database. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS key located in your account.</td></tr>
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
Expands tags for all <code>databases</code> in a region.
```sql
SELECT
region,
arn,
database_name,
kms_key_id,
tag_key,
tag_value
FROM aws.timestream.database_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>database_tags</code> resource, see <a href="/providers/aws/timestream/databases/#permissions"><code>databases</code></a>


