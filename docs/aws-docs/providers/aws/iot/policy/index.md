---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
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

Gets or operates on an individual <code>policy</code> resource, use <code>policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::Policy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td></td></tr>
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
id,
arn,
policy_document,
policy_name,
tags
FROM aws.iot.policy
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>policy</code> resource, the following permissions are required:

### Read
```json
iot:GetPolicy,
iot:ListTagsForResource
```

### Delete
```json
iot:DeletePolicy,
iot:GetPolicy,
iot:ListPolicyVersions,
iot:DeletePolicyVersion
```

### Update
```json
iot:GetPolicy,
iot:ListPolicyVersions,
iot:CreatePolicyVersion,
iot:DeletePolicyVersion,
iot:SetDefaultPolicyVersion,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

