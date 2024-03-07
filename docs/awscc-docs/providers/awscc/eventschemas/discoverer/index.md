---
title: discoverer
hide_title: false
hide_table_of_contents: false
keywords:
  - discoverer
  - eventschemas
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>discoverer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discoverer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>discoverer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eventschemas.discoverer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>discoverer_arn</code></td><td><code>string</code></td><td>The ARN of the discoverer.</td></tr>
<tr><td><code>discoverer_id</code></td><td><code>string</code></td><td>The Id of the discoverer.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the discoverer.</td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td>The ARN of the event bus.</td></tr>
<tr><td><code>cross_account</code></td><td><code>boolean</code></td><td>Defines whether event schemas from other accounts are discovered. Default is True.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>Defines the current state of the discoverer.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>discoverer</code> resource, the following permissions are required:

### Read
```json
schemas:DescribeDiscoverer
```

### Update
```json
schemas:DescribeDiscoverer,
schemas:UpdateDiscoverer,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource,
events:PutTargets,
events:PutRule
```

### Delete
```json
schemas:DescribeDiscoverer,
schemas:DeleteDiscoverer,
events:DeleteRule,
events:DisableRule,
events:RemoveTargets
```


## Example
```sql
SELECT
region,
discoverer_arn,
discoverer_id,
description,
source_arn,
cross_account,
state,
tags
FROM awscc.eventschemas.discoverer
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DiscovererArn&gt;'
```
