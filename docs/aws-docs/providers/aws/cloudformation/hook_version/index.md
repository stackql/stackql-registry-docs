---
title: hook_version
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_version
  - cloudformation
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


Gets or updates an individual <code>hook_version</code> resource, use <code>hook_versions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Publishes new or first hook version to AWS CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the HookVersion. This is used to uniquely identify a HookVersion resource</td></tr>
<tr><td><CopyableCode code="type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without the versionID.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><CopyableCode code="is_default_version" /></td><td><code>boolean</code></td><td>Indicates if this type version is the current default version</td></tr>
<tr><td><CopyableCode code="logging_config" /></td><td><code>object</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><CopyableCode code="schema_handler_package" /></td><td><code>string</code></td><td>A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>The ID of the version of the type represented by this hook instance.</td></tr>
<tr><td><CopyableCode code="visibility" /></td><td><code>string</code></td><td>The scope at which the type is visible and usable in CloudFormation operations.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Valid values include:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;PUBLIC: The type is publically visible and usable within any Amazon account.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
type_arn,
execution_role_arn,
is_default_version,
logging_config,
schema_handler_package,
type_name,
version_id,
visibility
FROM aws.cloudformation.hook_version
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>hook_version</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribeType
```

