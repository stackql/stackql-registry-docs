---
title: cis_scan_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - cis_scan_configurations
  - inspectorv2
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

Used to retrieve a list of <code>cis_scan_configurations</code> in a region or create a <code>cis_scan_configurations</code> resource, use <code>cis_scan_configuration</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cis_scan_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>CIS Scan Configuration resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.inspectorv2.cis_scan_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>CIS Scan configuration unique identifier</td></tr>
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
arn
FROM aws.inspectorv2.cis_scan_configurations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>cis_scan_configurations</code> resource, the following permissions are required:

### Create
```json
inspector2:CreateCisScanConfiguration,
inspector2:ListCisScanConfigurations,
inspector2:TagResource
```

### List
```json
inspector2:ListCisScanConfigurations,
inspector2:ListTagsForResource
```
