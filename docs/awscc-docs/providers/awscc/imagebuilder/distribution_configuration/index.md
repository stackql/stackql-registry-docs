---
title: distribution_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution_configuration
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>distribution_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>distribution_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.distribution_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the distribution configuration.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the distribution configuration.</td></tr>
<tr><td><code>distributions</code></td><td><code>array</code></td><td>The distributions of the distribution configuration.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
description,
distributions,
tags
FROM awscc.imagebuilder.distribution_configuration
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>distribution_configuration</code> resource, the following permissions are required:

### Update
```json
ec2:DescribeLaunchTemplates,
ec2:CreateLaunchTemplateVersion,
ec2:ModifyLaunchTemplate,
imagebuilder:GetDistributionConfiguration,
imagebuilder:UpdateDistributionConfiguration
```

### Read
```json
imagebuilder:GetDistributionConfiguration
```

### Delete
```json
imagebuilder:GetDistributionConfiguration,
imagebuilder:UnTagResource,
imagebuilder:DeleteDistributionConfiguration
```

