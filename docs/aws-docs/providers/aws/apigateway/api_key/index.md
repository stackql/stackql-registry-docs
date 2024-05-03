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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>api_key</code> resource, use <code>api_keys</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::ApiKey`` resource creates a unique key that you can distribute to clients who are executing API Gateway ``Method`` resources that require an API key. To specify which API key clients must use, map the API key with the ``RestApi`` and ``Stage`` resources that include the methods that require a key.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.api_key" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="api_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_id" /></td><td><code>string</code></td><td>An MKT customer identifier, when integrating with the AWS SaaS Marketplace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the ApiKey.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>Specifies whether the ApiKey can be used by callers.</td></tr>
<tr><td><CopyableCode code="generate_distinct_id" /></td><td><code>boolean</code></td><td>Specifies whether (``true``) or not (``false``) the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the API key. If you don't specify a name, CFN generates a unique physical ID and uses that ID for the API key name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt; If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="stage_keys" /></td><td><code>array</code></td><td>DEPRECATED FOR USAGE PLANS - Specifies stages associated with the API key.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The key-value map of strings. The valid character set is &#91;a-zA-Z+-=._:&#x2F;&#93;. The tag key can be up to 128 characters and must not start with ``aws:``. The tag value can be up to 256 characters.</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>Specifies a value of the API key.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
api_key_id,
customer_id,
description,
enabled,
generate_distinct_id,
name,
stage_keys,
tags,
value
FROM aws.apigateway.api_key
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

