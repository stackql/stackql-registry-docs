---
title: grant
hide_title: false
hide_table_of_contents: false
keywords:
  - grant
  - licensemanager
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>grant</code> resource, use <code>grants</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.grant" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="grant_arn" /></td><td><code>string</code></td><td>Arn of the grant.</td></tr>
<tr><td><CopyableCode code="grant_name" /></td><td><code>string</code></td><td>Name for the created Grant.</td></tr>
<tr><td><CopyableCode code="license_arn" /></td><td><code>string</code></td><td>License Arn for the grant.</td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td>Home region for the created grant.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the grant.</td></tr>
<tr><td><CopyableCode code="allowed_operations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="principals" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
grant_arn,
grant_name,
license_arn,
home_region,
version,
allowed_operations,
principals,
status
FROM aws.licensemanager.grant
WHERE region = 'us-east-1' AND data__Identifier = '<GrantArn>';
```


## Permissions

To operate on the <code>grant</code> resource, the following permissions are required:

### Read
```json
license-manager:GetGrant
```

### Update
```json
license-manager:CreateGrantVersion
```

