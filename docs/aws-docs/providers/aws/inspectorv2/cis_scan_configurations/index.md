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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>cis_scan_configurations</code> in a region or to create or delete a <code>cis_scan_configurations</code> resource, use <code>cis_scan_configuration</code> to read or update an individual resource.

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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>cis_scan_configuration</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- cis_scan_configuration.iql (required properties only)
INSERT INTO aws.inspectorv2.cis_scan_configurations (
 ScanName,
 SecurityLevel,
 Schedule,
 Targets,
 Tags,
 region
)
SELECT 
'{{ ScanName }}',
 '{{ SecurityLevel }}',
 '{{ Schedule }}',
 '{{ Targets }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- cis_scan_configuration.iql (all properties)
INSERT INTO aws.inspectorv2.cis_scan_configurations (
 ScanName,
 SecurityLevel,
 Schedule,
 Targets,
 Tags,
 region
)
SELECT 
 '{{ ScanName }}',
 '{{ SecurityLevel }}',
 '{{ Schedule }}',
 '{{ Targets }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: cis_scan_configuration
    props:
      - name: ScanName
        value: '{{ ScanName }}'
      - name: SecurityLevel
        value: '{{ SecurityLevel }}'
      - name: Schedule
        value: null
      - name: Targets
        value: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.inspectorv2.cis_scan_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cis_scan_configurations</code> resource, the following permissions are required:

### Create
```json
inspector2:CreateCisScanConfiguration,
inspector2:ListCisScanConfigurations,
inspector2:TagResource
```

### Delete
```json
inspector2:ListCisScanConfigurations,
inspector2:DeleteCisScanConfiguration,
inspector2:UntagResource
```

### List
```json
inspector2:ListCisScanConfigurations,
inspector2:ListTagsForResource
```

