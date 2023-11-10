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
<tr><td><b>Id</b></td><td><code>aws.kms.aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alias_name</code></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with alias&#x2F; followed by a name, such as alias&#x2F;ExampleAlias. The alias name cannot begin with alias&#x2F;aws&#x2F;. The alias&#x2F;aws&#x2F; prefix is reserved for AWS managed keys.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
alias_name
FROM aws.kms.aliases
WHERE region = 'us-east-1'
```
