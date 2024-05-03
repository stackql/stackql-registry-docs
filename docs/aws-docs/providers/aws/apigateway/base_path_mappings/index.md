---
title: base_path_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - base_path_mappings
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

Used to retrieve a list of <code>base_path_mappings</code> in a region or create a <code>base_path_mappings</code> resource, use <code>base_path_mapping</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>base_path_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGateway::BasePathMapping`` resource creates a base path that clients who call your API must use in the invocation URL.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.base_path_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The domain name of the BasePathMapping resource to be described.</td></tr>
<tr><td><CopyableCode code="base_path" /></td><td><code>string</code></td><td>The base path name that callers of the API must provide as part of the URL after the domain name.</td></tr>
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
domain_name,
base_path
FROM aws.apigateway.base_path_mappings
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>base_path_mappings</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET
```

### List
```json
apigateway:GET
```

