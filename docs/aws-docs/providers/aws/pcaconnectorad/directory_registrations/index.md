---
title: directory_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_registrations
  - pcaconnectorad
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

Used to retrieve a list of <code>directory_registrations</code> in a region or create a <code>directory_registrations</code> resource, use <code>directory_registration</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::DirectoryRegistration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.directory_registrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="directory_registration_arn" /></td><td><code>string</code></td><td></td></tr>
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
directory_registration_arn
FROM aws.pcaconnectorad.directory_registrations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>directory_registrations</code> resource, the following permissions are required:

### Create
```json
pca-connector-ad:GetDirectoryRegistration,
pca-connector-ad:CreateDirectoryRegistration,
ds:AuthorizeApplication,
ds:DescribeDirectories
```

### List
```json
pca-connector-ad:ListDirectoryRegistrations
```
