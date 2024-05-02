---
title: tls_inspection_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_inspection_configuration
  - networkfirewall
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>tls_inspection_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tls_inspection_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.tls_inspection_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tls_inspection_configuration_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tls_inspection_configuration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tls_inspection_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tls_inspection_configuration_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
tls_inspection_configuration_name,
tls_inspection_configuration_arn,
tls_inspection_configuration,
tls_inspection_configuration_id,
description,
tags
FROM aws.networkfirewall.tls_inspection_configuration
WHERE data__Identifier = '<TLSInspectionConfigurationArn>';
```

## Permissions

To operate on the <code>tls_inspection_configuration</code> resource, the following permissions are required:

### Read
```json
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:UpdateTLSInspectionConfiguration,
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:TagResource,
network-firewall:UntagResource
```

### Delete
```json
network-firewall:DeleteTLSInspectionConfiguration,
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:UntagResource
```

