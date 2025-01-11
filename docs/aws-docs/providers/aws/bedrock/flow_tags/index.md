---
title: flow_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_tags
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

Expands all tag keys and values for <code>flows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::Flow Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.flow_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn representation of the Flow</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td>Flow definition</td></tr>
<tr><td><CopyableCode code="definition_string" /></td><td><code>string</code></td><td>A JSON string containing a Definition with the same schema as the Definition property of this resource</td></tr>
<tr><td><CopyableCode code="definition_s3_location" /></td><td><code>object</code></td><td>An Amazon S3 location.</td></tr>
<tr><td><CopyableCode code="definition_substitutions" /></td><td><code>object</code></td><td>When supplied with DefinitionString or DefinitionS3Location, substrings in the definition matching $&#123;keyname&#125; will be replaced with the associated value from this map</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the flow</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>ARN of a IAM role</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Identifier for a Flow</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for the flow</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Schema Type for Flow APIs</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="validations" /></td><td><code>array</code></td><td>List of flow validations</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Draft Version.</td></tr>
<tr><td><CopyableCode code="test_alias_tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
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
Expands tags for all <code>flows</code> in a region.
```sql
SELECT
region,
arn,
created_at,
definition,
definition_string,
definition_s3_location,
definition_substitutions,
description,
execution_role_arn,
id,
name,
status,
updated_at,
customer_encryption_key_arn,
validations,
version,
test_alias_tags,
tag_key,
tag_value
FROM aws.bedrock.flow_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flow_tags</code> resource, see <a href="/providers/aws/bedrock/flows/#permissions"><code>flows</code></a>

