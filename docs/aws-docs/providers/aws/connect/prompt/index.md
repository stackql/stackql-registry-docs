---
title: prompt
hide_title: false
hide_table_of_contents: false
keywords:
  - prompt
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


Gets or updates an individual <code>prompt</code> resource, use <code>prompts</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompt</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Prompt</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.prompt" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the prompt.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the prompt.</td></tr>
<tr><td><CopyableCode code="s3_uri" /></td><td><code>string</code></td><td>S3 URI of the customer's audio file for creating prompts resource..</td></tr>
<tr><td><CopyableCode code="prompt_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the prompt.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
instance_arn,
name,
description,
s3_uri,
prompt_arn,
tags
FROM aws.connect.prompt
WHERE region = 'us-east-1' AND data__Identifier = '<PromptArn>';
```


## Permissions

To operate on the <code>prompt</code> resource, the following permissions are required:

### Read
```json
connect:DescribePrompt
```

### Update
```json
connect:UpdatePrompt,
connect:TagResource,
connect:UntagResource
```

