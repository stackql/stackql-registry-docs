---
title: studio_components
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_components
  - nimblestudio
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>studio_components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>studio_components</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.nimblestudio.studio_components</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>studio_component_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
studio_component_id,
studio_id
FROM awscc.nimblestudio.studio_components
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>studio_components</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
nimble:CreateStudioComponent,
nimble:GetStudioComponent,
nimble:TagResource,
ds:AuthorizeApplication,
ec2:DescribeSecurityGroups,
fsx:DescribeFilesystems,
ds:DescribeDirectories
```

### List
```json
nimble:ListStudioComponents
```

