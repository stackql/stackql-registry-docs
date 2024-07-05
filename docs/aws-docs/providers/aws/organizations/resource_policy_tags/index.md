---
title: resource_policy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy_tags
  - organizations
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

Expands all tag keys and values for <code>resource_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>You can use AWS::Organizations::ResourcePolicy to delegate policy management for AWS Organizations to specified member accounts to perform policy actions that are by default available only to the management account.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.resource_policy_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier (ID) associated with this resource policy.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the resource policy.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The policy document. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.</td></tr>
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
Expands tags for all <code>resource_policies</code> in a region.
```sql
SELECT
region,
id,
arn,
content,
tag_key,
tag_value
FROM aws.organizations.resource_policy_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_policy_tags</code> resource, see <a href="/providers/aws/organizations/resource_policies/#permissions"><code>resource_policies</code></a>


