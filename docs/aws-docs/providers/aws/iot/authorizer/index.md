---
title: authorizer
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizer
  - iot
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


Gets or updates an individual <code>authorizer</code> resource, use <code>authorizers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an authorizer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.authorizer" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="authorizer_function_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signing_disabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="token_key_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="token_signing_public_keys" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_caching_for_http" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
authorizer_function_arn,
arn,
authorizer_name,
signing_disabled,
status,
token_key_name,
token_signing_public_keys,
enable_caching_for_http,
tags
FROM aws.iot.authorizer
WHERE region = 'us-east-1' AND data__Identifier = '<AuthorizerName>';
```


## Permissions

To operate on the <code>authorizer</code> resource, the following permissions are required:

### Read
```json
iot:DescribeAuthorizer,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateAuthorizer,
iot:DescribeAuthorizer,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

