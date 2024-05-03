---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - datazone
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

Used to retrieve a list of <code>domains</code> in a region or create a <code>domains</code> resource, use <code>domain</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain is an organizing entity for connecting together assets, users, and their projects</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the Amazon DataZone domain.</td></tr>
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
id
FROM aws.datazone.domains
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
datazone:CreateDomain,
datazone:UpdateDomain,
datazone:GetDomain,
datazone:TagResource,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:PutApplicationAssignmentConfiguration
```

### List
```json
datazone:ListDomains
```
