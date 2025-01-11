---
title: flow_alias_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_alias_tags
  - bedrock
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

Expands all tag keys and values for <code>flow_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_alias_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::FlowAlias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.flow_alias_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn of the Flow Alias</td></tr>
<tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>Arn representation of the Flow</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="flow_id" /></td><td><code>string</code></td><td>Identifier for a flow resource.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for a Flow Alias generated at the server side.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for a resource.</td></tr>
<tr><td><CopyableCode code="routing_configuration" /></td><td><code>array</code></td><td>Routing configuration for a Flow alias.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
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
Expands tags for all <code>flow_aliases</code> in a region.
```sql
SELECT
region,
arn,
flow_arn,
created_at,
description,
flow_id,
id,
name,
routing_configuration,
updated_at,
tag_key,
tag_value
FROM aws.bedrock.flow_alias_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flow_alias_tags</code> resource, see <a href="/providers/aws/bedrock/flow_aliases/#permissions"><code>flow_aliases</code></a>

