---
title: collection
hide_title: false
hide_table_of_contents: false
keywords:
  - collection
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>collection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>collection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opensearchserverless.collection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the collection</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The identifier of the collection</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the collection.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The name must meet the following criteria:&lt;br&#x2F;&gt;Unique to your account and AWS Region&lt;br&#x2F;&gt;Starts with a lowercase letter&lt;br&#x2F;&gt;Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)&lt;br&#x2F;&gt;Contains between 3 and 32 characters&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>List of tags to be added to the resource</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr>
<tr><td><code>collection_endpoint</code></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr>
<tr><td><code>dashboard_endpoint</code></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>standby_replicas</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
id,
name,
tags,
arn,
collection_endpoint,
dashboard_endpoint,
type,
standby_replicas
FROM awscc.opensearchserverless.collection
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>collection</code> resource, the following permissions are required:

### Delete
```json
aoss:DeleteCollection,
aoss:BatchGetCollection
```

### Read
```json
aoss:BatchGetCollection
```

### Update
```json
aoss:UpdateCollection,
aoss:BatchGetCollection
```

