---
title: service_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_actions
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_actions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.servicecatalog.service_actions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>service_actions</code> resource, the following permissions are required:

### Create
```json
servicecatalog:CreateServiceAction,
ssm:DescribeDocument,
iam:GetRole
```

### List
```json
servicecatalog:ListServiceActions
```


## Example
```sql
SELECT
region,
id
FROM awscc.servicecatalog.service_actions
WHERE region = 'us-east-1'
```
