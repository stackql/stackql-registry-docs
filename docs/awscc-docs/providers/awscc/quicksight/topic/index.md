---
title: topic
hide_title: false
hide_table_of_contents: false
keywords:
  - topic
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>topic</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>topic</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.topic</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_sets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>topic_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_experience_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
aws_account_id,
data_sets,
description,
name,
topic_id,
user_experience_version
FROM awscc.quicksight.topic
WHERE data__Identifier = '<AwsAccountId>|<TopicId>';
```

## Permissions

To operate on the <code>topic</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeTopic
```

### Update
```json
quicksight:UpdateTopic,
quicksight:PassDataSet,
quicksight:DescribeTopicRefresh
```

### Delete
```json
quicksight:DeleteTopic
```

