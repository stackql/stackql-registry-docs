---
title: parameter
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter
  - ssm
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


Gets or updates an individual <code>parameter</code> resource, use <code>parameters</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SSM::Parameter`` resource creates an SSM parameter in SYSlong Parameter Store.&lt;br&#x2F;&gt;  To create an SSM parameter, you must have the IAMlong (IAM) permissions ``ssm:PutParameter`` and ``ssm:AddTagsToResource``. On stack creation, CFNlong adds the following three tags to the parameter: ``aws:cloudformation:stack-name``, ``aws:cloudformation:logical-id``, and ``aws:cloudformation:stack-id``, in addition to any custom tags you specify.&lt;br&#x2F;&gt; To add, update, or remove tags during stack update, you must have IAM permissions for both ``ssm:AddTagsToResource`` and ``ssm:RemoveTagsFromResource``. For more information, see &#91;Managing Access Using Policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;userguide&#x2F;security-iam.html#security_iam_access-manage) in the *User Guide*.&lt;br&#x2F;&gt;  For information about valid values for parameters, see &#91;About requirements and constraints for parameter names&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;userguide&#x2F;sysman-paramstore-su-create.html#sysman-parameter-name-constraints) in the *User Guide* and &#91;PutParameter&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;APIReference&#x2F;API_PutParameter.html) in the *API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.parameter" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of parameter.</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>The parameter value.&lt;br&#x2F;&gt;  If type is ``StringList``, the system returns a comma-separated string with no spaces between commas in the ``Value`` field.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Information about the parameter.</td></tr>
<tr><td><CopyableCode code="policies" /></td><td><code>string</code></td><td>Information about the policies assigned to a parameter.&lt;br&#x2F;&gt;  &#91;Assigning parameter policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;userguide&#x2F;parameter-store-policies.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="allowed_pattern" /></td><td><code>string</code></td><td>A regular expression used to validate the parameter value. For example, for ``String`` types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\d+$``</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>The parameter tier.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a SYS parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.</td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>string</code></td><td>The data type of the parameter, such as ``text`` or ``aws:ec2:image``. The default is ``text``.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the parameter.&lt;br&#x2F;&gt;  The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter&#x2F;ExampleParameterName``</td></tr>
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
type,
value,
description,
policies,
allowed_pattern,
tier,
tags,
data_type,
name
FROM aws.ssm.parameter
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>parameter</code> resource, the following permissions are required:

### Read
```json
ssm:GetParameters
```

### Update
```json
ssm:PutParameter,
ssm:AddTagsToResource,
ssm:RemoveTagsFromResource,
ssm:GetParameters
```

