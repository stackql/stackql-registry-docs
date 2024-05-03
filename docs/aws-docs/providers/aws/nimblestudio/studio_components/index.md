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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>studio_components</code> in a region or create a <code>studio_components</code> resource, use <code>studio_component</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio component that connects a non-Nimble Studio resource in your account to your studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studio_components" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_component_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
studio_component_id,
studio_id
FROM aws.nimblestudio.studio_components
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

