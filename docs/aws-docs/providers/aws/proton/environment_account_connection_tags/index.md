---
title: environment_account_connection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_account_connection_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>environment_account_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_account_connection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema describing various properties for AWS Proton Environment Account Connections resources.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.proton.environment_account_connection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the environment account connection.</td></tr>
<tr><td><CopyableCode code="codebuild_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</td></tr>
<tr><td><CopyableCode code="component_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</td></tr>
<tr><td><CopyableCode code="environment_account_id" /></td><td><code>string</code></td><td>The environment account that's connected to the environment account connection.</td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td>The name of the AWS Proton environment that's created in the associated management account.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the environment account connection.</td></tr>
<tr><td><CopyableCode code="management_account_id" /></td><td><code>string</code></td><td>The ID of the management account that accepts or rejects the environment account connection. You create an manage the AWS Proton environment in this account. If the management account accepts the environment account connection, AWS Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. AWS Proton uses this role to provision infrastructure resources in the associated environment account.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the environment account connection.</td></tr>
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
Expands tags for all <code>environment_account_connections</code> in a region.
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
tag_key,
tag_value
FROM aws.proton.environment_account_connection_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environment_account_connection_tags</code> resource, see <a href="/providers/aws/proton/environment_account_connections/#permissions"><code>environment_account_connections</code></a>

