---
title: registry_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policy
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
Gets an individual <code>registry_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>registry_policy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecr.registry_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>registry_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_text</code></td><td><code>object</code></td><td>The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see Registry permissions (https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;registry-permissions.html) in the Amazon Elastic Container Registry User Guide.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
registry_id,
policy_text
FROM aws.ecr.registry_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RegistryId&gt;'
```
