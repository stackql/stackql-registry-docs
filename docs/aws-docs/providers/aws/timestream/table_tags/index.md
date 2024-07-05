---
title: table_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - table_tags
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

Expands all tag keys and values for <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::Table resource creates a Timestream Table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.table_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The table name exposed as a read-only attribute.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name for the database which the table to be created belongs to.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.</td></tr>
<tr><td><CopyableCode code="retention_properties" /></td><td><code>object</code></td><td>The retention duration of the memory store and the magnetic store.</td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td>A Schema specifies the expected data model of the table.</td></tr>
<tr><td><CopyableCode code="magnetic_store_write_properties" /></td><td><code>object</code></td><td>The properties that determine whether magnetic store writes are enabled.</td></tr>
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
Expands tags for all <code>tables</code> in a region.
```sql
SELECT
region,
arn,
name,
database_name,
table_name,
retention_properties,
schema,
magnetic_store_write_properties,
tag_key,
tag_value
FROM aws.timestream.table_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>table_tags</code> resource, see <a href="/providers/aws/timestream/tables/#permissions"><code>tables</code></a>


