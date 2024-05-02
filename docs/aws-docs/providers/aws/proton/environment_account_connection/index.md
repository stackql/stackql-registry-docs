---
title: environment_account_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_account_connection
  - proton
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>environment_account_connection</code> resource, use <code>environment_account_connections</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_account_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema describing various properties for AWS Proton Environment Account Connections resources.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.proton.environment_account_connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the environment account connection.</td></tr>
<tr><td><code>codebuild_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</td></tr>
<tr><td><code>component_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</td></tr>
<tr><td><code>environment_account_id</code></td><td><code>string</code></td><td>The environment account that's connected to the environment account connection.</td></tr>
<tr><td><code>environment_name</code></td><td><code>string</code></td><td>The name of the AWS Proton environment that's created in the associated management account.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the environment account connection.</td></tr>
<tr><td><code>management_account_id</code></td><td><code>string</code></td><td>The ID of the management account that accepts or rejects the environment account connection. You create an manage the AWS Proton environment in this account. If the management account accepts the environment account connection, AWS Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. AWS Proton uses this role to provision infrastructure resources in the associated environment account.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the environment account connection.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>&lt;p&gt;An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.&lt;&#x2F;p&gt;&lt;br&#x2F;&gt;         &lt;p&gt;For more information, see &lt;a href="https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;proton&#x2F;latest&#x2F;userguide&#x2F;resources.html"&gt;Proton resources and tagging&lt;&#x2F;a&gt; in the&lt;br&#x2F;&gt;        &lt;i&gt;Proton User Guide&lt;&#x2F;i&gt;.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
codebuild_role_arn,
component_role_arn,
environment_account_id,
environment_name,
id,
management_account_id,
role_arn,
status,
tags
FROM aws.proton.environment_account_connection
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>environment_account_connection</code> resource, the following permissions are required:

### Read
```json
proton:GetEnvironmentAccountConnection,
proton:ListTagsForResource,
iam:PassRole,
proton:GetEnvironmentAccountConnection
```

### Update
```json
proton:CreateEnvironmentAccountConnection,
proton:ListTagsForResource,
proton:TagResource,
proton:UntagResource,
proton:UpdateEnvironmentAccountConnection,
iam:PassRole,
proton:GetEnvironmentAccountConnection
```

### Delete
```json
proton:DeleteEnvironmentAccountConnection,
proton:UntagResource,
iam:PassRole,
proton:ListTagsForResource,
proton:GetEnvironmentAccountConnection
```

