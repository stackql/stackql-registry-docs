---
title: work_group
hide_title: false
hide_table_of_contents: false
keywords:
  - work_group
  - athena
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


Gets or updates an individual <code>work_group</code> resource, use <code>work_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::WorkGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.work_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The workGroup name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The workgroup description.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags, separated by commas, that you want to attach to the workgroup as you create it</td></tr>
<tr><td><CopyableCode code="work_group_configuration" /></td><td><code>object</code></td><td>The workgroup configuration</td></tr>
<tr><td><CopyableCode code="work_group_configuration_updates" /></td><td><code>object</code></td><td>The workgroup configuration update object</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time the workgroup was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the workgroup: ENABLED or DISABLED.</td></tr>
<tr><td><CopyableCode code="recursive_delete_option" /></td><td><code>boolean</code></td><td>The option to delete the workgroup and its contents even if the workgroup contains any named queries.</td></tr>
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
name,
description,
tags,
work_group_configuration,
work_group_configuration_updates,
creation_time,
state,
recursive_delete_option
FROM aws.athena.work_group
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>work_group</code> resource, the following permissions are required:

### Read
```json
athena:GetWorkGroup,
athena:ListTagsForResource
```

### Update
```json
athena:UpdateWorkGroup,
athena:TagResource,
athena:UntagResource,
iam:PassRole,
s3:GetBucketLocation,
s3:GetObject,
s3:ListBucket,
s3:ListBucketMultipartUploads,
s3:AbortMultipartUpload,
s3:PutObject,
s3:ListMultipartUploadParts,
kms:Decrypt,
kms:GenerateDataKey
```

