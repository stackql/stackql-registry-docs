---
title: distribution_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution_configurations
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
Retrieves a list of <code>distribution_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>distribution_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.distribution_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>distribution_configurations</code> resource, the following permissions are required:

### Create
<pre>
iam:GetRole,
iam:CreateServiceLinkedRole,
ec2:DescribeLaunchTemplates,
ec2:CreateLaunchTemplateVersion,
ec2:ModifyLaunchTemplate,
imagebuilder:TagResource,
imagebuilder:GetDistributionConfiguration,
imagebuilder:CreateDistributionConfiguration</pre>

### List
<pre>
imagebuilder:ListDistributionConfigurations</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.imagebuilder.distribution_configurations
WHERE region = 'us-east-1'
```
