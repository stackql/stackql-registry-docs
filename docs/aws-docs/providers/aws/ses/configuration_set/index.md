---
title: configuration_set
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_set
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
Gets or operates on an individual <code>configuration_set</code> resource, use <code>configuration_sets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ConfigurationSet.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.configuration_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
<tr><td><code>tracking_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>delivery_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>reputation_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sending_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>suppression_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vdm_options</code></td><td><code>object</code></td><td></td></tr>
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
name,
tracking_options,
delivery_options,
reputation_options,
sending_options,
suppression_options,
vdm_options
FROM aws.ses.configuration_set
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>configuration_set</code> resource, the following permissions are required:

### Read
```json
ses:GetConfigurationSet,
ses:DescribeConfigurationSet
```

### Update
```json
ses:PutConfigurationSetTrackingOptions,
ses:PutConfigurationSetDeliveryOptions,
ses:PutConfigurationSetReputationOptions,
ses:PutConfigurationSetSendingOptions,
ses:PutConfigurationSetSuppressionOptions,
ses:PutConfigurationSetVdmOptions
```

### Delete
```json
ses:DeleteConfigurationSet
```

