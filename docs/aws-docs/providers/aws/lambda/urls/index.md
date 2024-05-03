---
title: urls
hide_title: false
hide_table_of_contents: false
keywords:
  - urls
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

Used to retrieve a list of <code>urls</code> in a region or create a <code>urls</code> resource, use <code>url</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::Url</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.urls" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="function_arn" /></td><td><code>string</code></td><td>The full Amazon Resource Name (ARN) of the function associated with the Function URL.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
function_arn
FROM aws.lambda.urls
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>urls</code> resource, the following permissions are required:

### Create
```json
lambda:CreateFunctionUrlConfig
```

### List
```json
lambda:ListFunctionUrlConfigs
```

