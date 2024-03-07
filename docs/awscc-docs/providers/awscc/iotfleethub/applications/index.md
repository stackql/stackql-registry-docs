---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - iotfleethub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>applications</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotfleethub.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The ID of the application.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
application_id
FROM awscc.iotfleethub.applications
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
iotfleethub:CreateApplication,
iotfleethub:TagResource,
iam:PassRole,
sso:CreateManagedApplicationInstance,
sso:DescribeRegisteredRegions
```

### List
```json
iotfleethub:ListApplications
```

