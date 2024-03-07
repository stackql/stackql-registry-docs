---
title: protection
hide_title: false
hide_table_of_contents: false
keywords:
  - protection
  - shield
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>protection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>protection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.shield.protection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>protection_id</code></td><td><code>string</code></td><td>The unique identifier (ID) of the protection.</td></tr>
<tr><td><code>protection_arn</code></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Friendly name for the Protection.</td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the resource to be protected.</td></tr>
<tr><td><code>health_check_arns</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the health check to associate with the protection.</td></tr>
<tr><td><code>application_layer_automatic_response_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tag key-value pairs for the Protection object.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>protection</code> resource, the following permissions are required:

### Delete
```json
shield:DeleteProtection,
shield:UntagResource
```

### Read
```json
shield:DescribeProtection,
shield:ListTagsForResource
```

### Update
```json
shield:DescribeProtection,
shield:AssociateHealthCheck,
shield:DisassociateHealthCheck,
shield:EnableApplicationLayerAutomaticResponse,
shield:UpdateApplicationLayerAutomaticResponse,
shield:DisableApplicationLayerAutomaticResponse,
shield:ListTagsForResource,
shield:TagResource,
shield:UntagResource,
route53:GetHealthCheck,
iam:GetRole,
iam:CreateServiceLinkedRole,
wafv2:GetWebACLForResource,
wafv2:GetWebACL
```


## Example
```sql
SELECT
region,
protection_id,
protection_arn,
name,
resource_arn,
health_check_arns,
application_layer_automatic_response_configuration,
tags
FROM awscc.shield.protection
WHERE data__Identifier = '&lt;ProtectionArn&gt;'
```
