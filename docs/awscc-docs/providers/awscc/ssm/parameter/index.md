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
Gets an individual <code>parameter</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>parameter</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssm.parameter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of parameter.&lt;br&#x2F;&gt;  Although ``SecureString`` is included in the list of valid values, CFNlong does *not* currently support creating a ``SecureString`` parameter type.</td></tr>
<tr><td><code>value</code></td><td><code>string</code></td><td>The parameter value.&lt;br&#x2F;&gt;  If type is ``StringList``, the system returns a comma-separated string with no spaces between commas in the ``Value`` field.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Information about the parameter.</td></tr>
<tr><td><code>policies</code></td><td><code>string</code></td><td>Information about the policies assigned to a parameter.&lt;br&#x2F;&gt;  &#91;Assigning parameter policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;systems-manager&#x2F;latest&#x2F;userguide&#x2F;parameter-store-policies.html) in the *User Guide*.</td></tr>
<tr><td><code>allowed_pattern</code></td><td><code>string</code></td><td>A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: ``AllowedPattern=^\d+$``</td></tr>
<tr><td><code>tier</code></td><td><code>string</code></td><td>The parameter tier.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>Optional metadata that you assign to a resource in the form of an arbitrary set of tags (key-value pairs). Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a SYS parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter.</td></tr>
<tr><td><code>data_type</code></td><td><code>string</code></td><td>The data type of the parameter, such as ``text`` or ``aws:ec2:image``. The default is ``text``.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the parameter.&lt;br&#x2F;&gt; The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter ARN, is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: ``arn:aws:ssm:us-east-2:111222333444:parameter&#x2F;ExampleParameterName``</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.ssm.parameter
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
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

### Delete
```json
ssm:DeleteParameter
```

