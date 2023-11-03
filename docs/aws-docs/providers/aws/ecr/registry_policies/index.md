---
title: registry_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policies
  - ecr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>registry_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecr.registry_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RegistryId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PolicyText</code></td><td><code>object</code></td><td>The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the Amazon Elastic Container Registry User Guide.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ecr.registry_policies
WHERE region = 'us-east-1'
```
