---
title: api_key
hide_title: false
hide_table_of_contents: false
keywords:
  - api_key
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>api_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.api_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>customer_id</code></td><td><code>string</code></td><td>An MKT customer identifier, when integrating with the AWS SaaS Marketplace.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the ApiKey.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>Specifies whether the ApiKey can be used by callers.</td></tr>
<tr><td><code>generate_distinct_id</code></td><td><code>boolean</code></td><td>Specifies whether (``true``) or not (``false``) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the API key. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the API key name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt; If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>stage_keys</code></td><td><code>array</code></td><td>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The key-value map of strings. The valid character set is &#91;a-zA-Z+-=._:&#x2F;&#93;. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.</td></tr>
<tr><td><code>value</code></td><td><code>string</code></td><td>Specifies a value of the API key.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
api_key_id,
customer_id,
description,
enabled,
generate_distinct_id,
name,
stage_keys,
tags,
value
FROM awscc.apigateway.api_key
WHERE data__Identifier = '<APIKeyId>';
```

## Permissions

To operate on the <code>api_key</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:GET,
apigateway:PATCH,
apigateway:PUT,
apigateway:DELETE
```

### Delete
```json
apigateway:DELETE,
apigateway:GET
```

