---
title: cis_scan_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - cis_scan_configuration
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
Gets an individual <code>cis_scan_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cis_scan_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cis_scan_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.inspectorv2.cis_scan_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scan_name</code></td><td><code>string</code></td><td>Name of the scan</td></tr>
<tr><td><code>security_level</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>CIS Scan configuration unique identifier</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>cis_scan_configuration</code> resource, the following permissions are required:

### Read
```json
inspector2:ListCisScanConfigurations,
inspector2:ListTagsForResource
```

### Update
```json
inspector2:ListCisScanConfigurations,
inspector2:UpdateCisScanConfiguration,
inspector2:TagResource,
inspector2:UntagResource,
inspector2:ListTagsForResource
```

### Delete
```json
inspector2:ListCisScanConfigurations,
inspector2:DeleteCisScanConfiguration,
inspector2:UntagResource
```


## Example
```sql
SELECT
region,
scan_name,
security_level,
schedule,
targets,
arn,
tags
FROM awscc.inspectorv2.cis_scan_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
