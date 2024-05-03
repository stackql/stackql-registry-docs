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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>vdm_attributes</code> resource, use <code>vdm_attributes</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vdm_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::VdmAttributes</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.vdm_attributes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vdm_attributes_resource_id" /></td><td><code>string</code></td><td>Unique identifier for this resource</td></tr>
<tr><td><CopyableCode code="dashboard_attributes" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="guardian_attributes" /></td><td><code>object</code></td><td></td></tr>
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
vdm_attributes_resource_id,
dashboard_attributes,
guardian_attributes
FROM aws.ses.vdm_attributes
WHERE data__Identifier = '<VdmAttributesResourceId>';
```

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

