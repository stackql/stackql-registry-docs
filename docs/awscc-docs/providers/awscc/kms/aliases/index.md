---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
  - kms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>aliases</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kms.aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alias_name</code></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with ``alias&#x2F;`` followed by a name, such as ``alias&#x2F;ExampleAlias``. &lt;br&#x2F;&gt;  If you change the value of the ``AliasName`` property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC).&lt;br&#x2F;&gt;  The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (&#x2F;), underscores (_), and dashes (-). The alias name cannot begin with ``alias&#x2F;aws&#x2F;``. The ``alias&#x2F;aws&#x2F;`` prefix is reserved for &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;developerguide&#x2F;concepts.html#aws-managed-cmk).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>aliases</code> resource, the following permissions are required:

### Create
<pre>
kms:CreateAlias</pre>

### List
<pre>
kms:ListAliases</pre>


## Example
```sql
SELECT
region,
alias_name
FROM awscc.kms.aliases
WHERE region = 'us-east-1'
```
