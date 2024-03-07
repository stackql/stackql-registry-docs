---
title: zonal_autoshift_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - zonal_autoshift_configuration
  - arczonalshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>zonal_autoshift_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zonal_autoshift_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>zonal_autoshift_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.arczonalshift.zonal_autoshift_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>zonal_autoshift_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>practice_run_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
zonal_autoshift_status,
practice_run_configuration,
resource_identifier
FROM awscc.arczonalshift.zonal_autoshift_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '{ResourceIdentifier}';
```

## Permissions

To operate on the <code>zonal_autoshift_configuration</code> resource, the following permissions are required:

### Read
```json
arc-zonal-shift:GetManagedResource
```

### Update
```json
arc-zonal-shift:GetManagedResource,
arc-zonal-shift:UpdatePracticeRunConfiguration,
arc-zonal-shift:UpdateZonalAutoshiftConfiguration,
cloudwatch:DescribeAlarms
```

### Delete
```json
arc-zonal-shift:DeletePracticeRunConfiguration,
arc-zonal-shift:GetManagedResource,
arc-zonal-shift:UpdateZonalAutoshiftConfiguration
```

