---
title: replication_set_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_set_tags
  - ssmincidents
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

Expands all tag keys and values for <code>replication_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_set_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ReplicationSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.replication_set_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the ReplicationSet.</td></tr>
<tr><td><CopyableCode code="regions" /></td><td><code>array</code></td><td>The ReplicationSet configuration.</td></tr>
<tr><td><CopyableCode code="deletion_protected" /></td><td><code>boolean</code></td><td>Configures the ReplicationSet deletion protection.</td></tr>
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
Expands tags for all <code>replication_sets</code> in a region.
```sql
SELECT
region,
arn,
regions,
deletion_protected,
tag_key,
tag_value
FROM aws.ssmincidents.replication_set_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>replication_set_tags</code> resource, see <a href="/providers/aws/ssmincidents/replication_sets/#permissions"><code>replication_sets</code></a>

