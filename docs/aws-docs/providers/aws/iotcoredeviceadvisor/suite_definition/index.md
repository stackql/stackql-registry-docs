---
title: suite_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - suite_definition
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>suite_definition</code> resource, use <code>suite_definitions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suite_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotcoredeviceadvisor.suite_definition" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="suite_definition_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="suite_definition_id" /></td><td><code>string</code></td><td>The unique identifier for the suite definition.</td></tr>
<tr><td><CopyableCode code="suite_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource name for the suite definition.</td></tr>
<tr><td><CopyableCode code="suite_definition_version" /></td><td><code>string</code></td><td>The suite definition version of a test suite.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
suite_definition_configuration,
suite_definition_id,
suite_definition_arn,
suite_definition_version,
tags
FROM aws.iotcoredeviceadvisor.suite_definition
WHERE data__Identifier = '<SuiteDefinitionId>';
```

## Permissions

To operate on the <code>suite_definition</code> resource, the following permissions are required:

### Read
```json
iotdeviceadvisor:GetSuiteDefinition,
iotdeviceadvisor:TagResource
```

### Update
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
iotdeviceadvisor:UpdateSuiteDefinition,
iotdeviceadvisor:GetSuiteDefinition,
iotdeviceadvisor:UntagResource,
iotdeviceadvisor:TagResource,
iam:PassRole
```

### Delete
```json
iotdeviceadvisor:GetSuiteDefinition,
iotdeviceadvisor:DeleteSuiteDefinition
```

