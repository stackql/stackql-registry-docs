---
title: namespaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_list_only
  - redshiftserverless
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

Lists <code>namespaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/namespaces/"><code>namespaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RedshiftServerless::Namespace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshiftserverless.namespaces_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="admin_password_secret_kms_key_id" /></td><td><code>string</code></td><td>The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if manageAdminPassword is true.</td></tr>
<tr><td><CopyableCode code="admin_user_password" /></td><td><code>string</code></td><td>The password associated with the admin user for the namespace that is being created. Password must be at least 8 characters in length, should be any printable ASCII character. Must contain at least one lowercase letter, one uppercase letter and one decimal digit. You can't use adminUserPassword if manageAdminPassword is true.</td></tr>
<tr><td><CopyableCode code="admin_username" /></td><td><code>string</code></td><td>The user name associated with the admin user for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.</td></tr>
<tr><td><CopyableCode code="db_name" /></td><td><code>string</code></td><td>The database name associated for the namespace that is being created. Only alphanumeric characters and underscores are allowed. It should start with an alphabet.</td></tr>
<tr><td><CopyableCode code="default_iam_role_arn" /></td><td><code>string</code></td><td>The default IAM role ARN for the namespace that is being created.</td></tr>
<tr><td><CopyableCode code="iam_roles" /></td><td><code>array</code></td><td>A list of AWS Identity and Access Management (IAM) roles that can be used by the namespace to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. The Default role limit for each request is 10.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the namespace.</td></tr>
<tr><td><CopyableCode code="log_exports" /></td><td><code>array</code></td><td>The collection of log types to be exported provided by the customer. Should only be one of the three supported log types: userlog, useractivitylog and connectionlog</td></tr>
<tr><td><CopyableCode code="manage_admin_password" /></td><td><code>boolean</code></td><td>If true, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials. You can't use adminUserPassword if manageAdminPassword is true. If manageAdminPassword is false or not set, Amazon Redshift uses adminUserPassword for the admin user account's password.</td></tr>
<tr><td><CopyableCode code="namespace" /></td><td><code>object</code></td><td>Definition of Namespace resource.</td></tr>
<tr><td><CopyableCode code="namespace_name" /></td><td><code>string</code></td><td>A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tags for the namespace.</td></tr>
<tr><td><CopyableCode code="final_snapshot_name" /></td><td><code>string</code></td><td>The name of the namespace the source snapshot was created from. Please specify the name if needed before deleting namespace</td></tr>
<tr><td><CopyableCode code="final_snapshot_retention_period" /></td><td><code>integer</code></td><td>The number of days to retain automated snapshot in the destination region after they are copied from the source region. If the value is -1, the manual snapshot is retained indefinitely. The value must be either -1 or an integer between 1 and 3,653.</td></tr>
<tr><td><CopyableCode code="namespace_resource_policy" /></td><td><code>object</code></td><td>The resource policy document that will be attached to the namespace.</td></tr>
<tr><td><CopyableCode code="redshift_idc_application_arn" /></td><td><code>string</code></td><td>The ARN for the Redshift application that integrates with IAM Identity Center.</td></tr>
<tr><td><CopyableCode code="snapshot_copy_configurations" /></td><td><code>array</code></td><td>The snapshot copy configurations for the namespace.</td></tr>
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
Lists all <code>namespaces</code> in a region.
```sql
SELECT
region,
namespace_name
FROM aws.redshiftserverless.namespaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>namespaces_list_only</code> resource, see <a href="/providers/aws/redshiftserverless/namespaces/#permissions"><code>namespaces</code></a>


