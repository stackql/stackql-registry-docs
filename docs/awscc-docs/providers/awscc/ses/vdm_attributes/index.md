---
title: vdm_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - vdm_attributes
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vdm_attributes</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vdm_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vdm_attributes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ses.vdm_attributes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vdm_attributes_resource_id</code></td><td><code>string</code></td><td>Unique identifier for this resource</td></tr>
<tr><td><code>dashboard_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>guardian_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vdm_attributes</code> resource, the following permissions are required:

### Read
```json
ses:GetAccount
```

### Update
```json
ses:PutAccountVdmAttributes,
ses:GetAccount
```

### Delete
```json
ses:PutAccountVdmAttributes,
ses:GetAccount
```


## Example
```sql
SELECT
region,
vdm_attributes_resource_id,
dashboard_attributes,
guardian_attributes
FROM awscc.ses.vdm_attributes
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;VdmAttributesResourceId&gt;'
```
