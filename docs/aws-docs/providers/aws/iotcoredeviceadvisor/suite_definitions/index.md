---
title: suite_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - suite_definitions
  - iotcoredeviceadvisor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>suite_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suite_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotcoredeviceadvisor.suite_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>suite_definition_id</code></td><td><code>string</code></td><td>The unique identifier for the suite definition.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
suite_definition_id
FROM aws.iotcoredeviceadvisor.suite_definitions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>suite_definitions</code> resource, the following permissions are required:

### Create
```json
iot:DescribeCertificate,
iot:DescribeThing,
iot:GetPolicy,
iot:ListAttachedPolicies,
iot:ListCertificates,
iot:ListPrincipalPolicies,
iot:ListTagsForResource,
iot:ListThingPrincipals,
iot:ListThings,
iotdeviceadvisor:CreateSuiteDefinition,
iotdeviceadvisor:TagResource,
iam:PassRole
```

### List
```json
iotdeviceadvisor:ListSuiteDefinitions
```

