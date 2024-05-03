---
title: studio_component
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_component
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

Gets or operates on an individual <code>studio_component</code> resource, use <code>studio_components</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio component that connects a non-Nimble Studio resource in your account to your studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studio_component" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>&lt;p&gt;The description.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="ec2_security_group_ids" /></td><td><code>array</code></td><td>&lt;p&gt;The EC2 security groups that control access to the studio component.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="initialization_scripts" /></td><td><code>array</code></td><td>&lt;p&gt;Initialization scripts for studio components.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>&lt;p&gt;The name for the studio component.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="script_parameters" /></td><td><code>array</code></td><td>&lt;p&gt;Parameters for the studio component scripts.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="secure_initialization_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_component_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="subtype" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
configuration,
description,
ec2_security_group_ids,
initialization_scripts,
name,
runtime_role_arn,
script_parameters,
secure_initialization_role_arn,
studio_component_id,
studio_id,
subtype,
tags,
type
FROM aws.nimblestudio.studio_component
WHERE data__Identifier = '<StudioComponentId>|<StudioId>';
```

## Permissions

To operate on the <code>studio_component</code> resource, the following permissions are required:

### Read
```json
nimble:GetStudioComponent
```

### Update
```json
iam:PassRole,
nimble:UpdateStudioComponent,
nimble:GetStudioComponent,
ds:AuthorizeApplication,
ec2:DescribeSecurityGroups,
fsx:DescribeFilesystems,
ds:DescribeDirectories
```

### Delete
```json
nimble:DeleteStudioComponent,
nimble:GetStudioComponent,
nimble:UntagResource,
ds:UnauthorizeApplication
```

