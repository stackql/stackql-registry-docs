---
title: addon
hide_title: false
hide_table_of_contents: false
keywords:
  - addon
  - eks
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

Gets or operates on an individual <code>addon</code> resource, use <code>addons</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addon</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::EKS::Addon</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.addon" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>Name of Cluster</td></tr>
<tr><td><CopyableCode code="addon_name" /></td><td><code>string</code></td><td>Name of Addon</td></tr>
<tr><td><CopyableCode code="addon_version" /></td><td><code>string</code></td><td>Version of Addon</td></tr>
<tr><td><CopyableCode code="preserve_on_delete" /></td><td><code>boolean</code></td><td>PreserveOnDelete parameter value</td></tr>
<tr><td><CopyableCode code="resolve_conflicts" /></td><td><code>string</code></td><td>Resolve parameter value conflicts</td></tr>
<tr><td><CopyableCode code="service_account_role_arn" /></td><td><code>string</code></td><td>IAM role to bind to the add-on's service account</td></tr>
<tr><td><CopyableCode code="configuration_values" /></td><td><code>string</code></td><td>The configuration values to use with the add-on</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the add-on</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
cluster_name,
addon_name,
addon_version,
preserve_on_delete,
resolve_conflicts,
service_account_role_arn,
configuration_values,
arn,
tags
FROM aws.eks.addon
WHERE data__Identifier = '<ClusterName>|<AddonName>';
```

## Permissions

To operate on the <code>addon</code> resource, the following permissions are required:

### Read
```json
eks:DescribeAddon
```

### Delete
```json
eks:DeleteAddon,
eks:DescribeAddon
```

### Update
```json
iam:PassRole,
eks:UpdateAddon,
eks:DescribeAddon,
eks:DescribeUpdate,
eks:ListTagsForResource,
eks:TagResource,
eks:UntagResource
```

