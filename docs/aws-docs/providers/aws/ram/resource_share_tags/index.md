---
title: resource_share_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_share_tags
  - ram
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

Expands all tag keys and values for <code>resource_shares</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_share_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::RAM::ResourceShare</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ram.resource_share_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allow_external_principals" /></td><td><code>boolean</code></td><td>Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share. A value of `true` lets you share with individual AWS accounts that are not in your organization. A value of `false` only has meaning if your account is a member of an AWS Organization. The default value is `true`.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Specifies the name of the resource share.</td></tr>
<tr><td><CopyableCode code="permission_arns" /></td><td><code>array</code></td><td>Specifies the &#91;Amazon Resource Names (ARNs)&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.</td></tr>
<tr><td><CopyableCode code="principals" /></td><td><code>array</code></td><td>Specifies the principals to associate with the resource share. The possible values are:<br />- An AWS account ID<br />- An Amazon Resource Name (ARN) of an organization in AWS Organizations<br />- An ARN of an organizational unit (OU) in AWS Organizations<br />- An ARN of an IAM role<br />- An ARN of an IAM user</td></tr>
<tr><td><CopyableCode code="resource_arns" /></td><td><code>array</code></td><td>Specifies a list of one or more ARNs of the resources to associate with the resource share.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>Specifies from which source accounts the service principal has access to the resources in this resource share.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>resource_shares</code> in a region.
```sql
SELECT
region,
allow_external_principals,
arn,
name,
permission_arns,
principals,
resource_arns,
sources,
tag_key,
tag_value
FROM aws.ram.resource_share_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_share_tags</code> resource, see <a href="/providers/aws/ram/resource_shares/#permissions"><code>resource_shares</code></a>

