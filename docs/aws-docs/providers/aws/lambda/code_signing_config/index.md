---
title: code_signing_config
hide_title: false
hide_table_of_contents: false
keywords:
  - code_signing_config
  - lambda
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


Gets or updates an individual <code>code_signing_config</code> resource, use <code>code_signing_configs</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>code_signing_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::CodeSigningConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.code_signing_config" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the CodeSigningConfig</td></tr>
<tr><td><CopyableCode code="allowed_publishers" /></td><td><code>object</code></td><td>When the CodeSigningConfig is later on attached to a function, the function code will be expected to be signed by profiles from this list</td></tr>
<tr><td><CopyableCode code="code_signing_policies" /></td><td><code>object</code></td><td>Policies to control how to act if a signature is invalid</td></tr>
<tr><td><CopyableCode code="code_signing_config_id" /></td><td><code>string</code></td><td>A unique identifier for CodeSigningConfig resource</td></tr>
<tr><td><CopyableCode code="code_signing_config_arn" /></td><td><code>string</code></td><td>A unique Arn for CodeSigningConfig resource</td></tr>
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
description,
allowed_publishers,
code_signing_policies,
code_signing_config_id,
code_signing_config_arn
FROM aws.lambda.code_signing_config
WHERE region = 'us-east-1' AND data__Identifier = '<CodeSigningConfigArn>';
```


## Permissions

To operate on the <code>code_signing_config</code> resource, the following permissions are required:

### Read
```json
lambda:GetCodeSigningConfig
```

### Update
```json
lambda:UpdateCodeSigningConfig
```

