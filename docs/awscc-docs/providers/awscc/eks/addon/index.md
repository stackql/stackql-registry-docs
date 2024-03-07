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
Gets an individual <code>addon</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addon</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>addon</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eks.addon</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>Name of Cluster</td></tr>
<tr><td><code>addon_name</code></td><td><code>string</code></td><td>Name of Addon</td></tr>
<tr><td><code>addon_version</code></td><td><code>string</code></td><td>Version of Addon</td></tr>
<tr><td><code>preserve_on_delete</code></td><td><code>boolean</code></td><td>PreserveOnDelete parameter value</td></tr>
<tr><td><code>resolve_conflicts</code></td><td><code>string</code></td><td>Resolve parameter value conflicts</td></tr>
<tr><td><code>service_account_role_arn</code></td><td><code>string</code></td><td>IAM role to bind to the add-on's service account</td></tr>
<tr><td><code>configuration_values</code></td><td><code>string</code></td><td>The configuration values to use with the add-on</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the add-on</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
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
FROM awscc.eks.addon
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ClusterName&gt;'
AND data__Identifier = '&lt;AddonName&gt;'
```
