---
title: policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_list_only
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

Lists <code>policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/policies/"><code>policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Policies in AWS Organizations enable you to manage different features of the AWS accounts in your organization. You can use policies when all features are enabled in your organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Policy</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Human readable description of the policy</td></tr>
<tr><td><CopyableCode code="target_ids" /></td><td><code>array</code></td><td>List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the Policy</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the Policy</td></tr>
<tr><td><CopyableCode code="aws_managed" /></td><td><code>boolean</code></td><td>A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.</td></tr>
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
Lists all <code>policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.organizations.policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>policies_list_only</code> resource, see <a href="/providers/aws/organizations/policies/#permissions"><code>policies</code></a>


