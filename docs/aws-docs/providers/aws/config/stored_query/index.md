---
title: stored_query
hide_title: false
hide_table_of_contents: false
keywords:
  - stored_query
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


Gets or updates an individual <code>stored_query</code> resource, use <code>stored_queries</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stored_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::StoredQuery</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.stored_query" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="query_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_expression" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the stored query.</td></tr>
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
query_arn,
query_id,
query_name,
query_description,
query_expression,
tags
FROM aws.config.stored_query
WHERE region = 'us-east-1' AND data__Identifier = '<QueryName>';
```


## Permissions

To operate on the <code>stored_query</code> resource, the following permissions are required:

### Read
```json
config:GetStoredQuery,
config:ListTagsForResource
```

### Update
```json
config:PutStoredQuery,
config:GetStoredQuery,
config:TagResource,
config:UntagResource,
config:ListTagsForResource
```

