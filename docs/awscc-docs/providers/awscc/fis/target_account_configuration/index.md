---
title: target_account_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - target_account_configuration
  - fis
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>target_account_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_account_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>target_account_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.fis.target_account_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>experiment_template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
experiment_template_id,
account_id,
role_arn,
description
FROM awscc.fis.target_account_configuration
WHERE data__Identifier = '<ExperimentTemplateId>|<AccountId>';
```

## Permissions

To operate on the <code>target_account_configuration</code> resource, the following permissions are required:

### Read
```json
fis:GetTargetAccountConfiguration
```

### Update
```json
fis:UpdateTargetAccountConfiguration
```

### Delete
```json
fis:DeleteTargetAccountConfiguration
```

