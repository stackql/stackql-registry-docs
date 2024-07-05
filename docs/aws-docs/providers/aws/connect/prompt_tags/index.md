---
title: prompt_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - prompt_tags
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

Expands all tag keys and values for <code>prompts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompt_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Prompt</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.prompt_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the prompt.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the prompt.</td></tr>
<tr><td><CopyableCode code="s3_uri" /></td><td><code>string</code></td><td>S3 URI of the customer's audio file for creating prompts resource..</td></tr>
<tr><td><CopyableCode code="prompt_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the prompt.</td></tr>
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
Expands tags for all <code>prompts</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
description,
s3_uri,
prompt_arn,
tag_key,
tag_value
FROM aws.connect.prompt_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>prompt_tags</code> resource, see <a href="/providers/aws/connect/prompts/#permissions"><code>prompts</code></a>


