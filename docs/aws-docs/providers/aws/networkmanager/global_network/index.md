---
title: global_network
hide_title: false
hide_table_of_contents: false
keywords:
  - global_network
  - networkmanager
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

Gets or operates on an individual <code>global_network</code> resource, use <code>global_networks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::GlobalNetwork type specifies a global network of the user's account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.global_network" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the global network.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the global network.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the global network.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time that the global network was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the global network.</td></tr>
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
arn,
id,
description,
tags,
created_at,
state
FROM aws.networkmanager.global_network
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>global_network</code> resource, the following permissions are required:

### Read
```json
networkmanager:DescribeGlobalNetworks
```

### Update
```json
networkmanager:UpdateGlobalNetwork,
networkmanager:DescribeGlobalNetworks,
networkmanager:TagResource,
networkmanager:UntagResource,
networkmanager:ListTagsForResource
```

### Delete
```json
networkmanager:DeleteGlobalNetwork,
networkmanager:DescribeGlobalNetworks
```

