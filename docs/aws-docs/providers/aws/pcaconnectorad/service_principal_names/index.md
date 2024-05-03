---
title: service_principal_names
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_names
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

Used to retrieve a list of <code>service_principal_names</code> in a region or create a <code>service_principal_names</code> resource, use <code>service_principal_name</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.service_principal_names" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
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
connector_arn,
directory_registration_arn
FROM aws.pcaconnectorad.service_principal_names
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>service_principal_names</code> resource, the following permissions are required:

### Create
```json
ds:UpdateAuthorizedApplication,
pca-connector-ad:GetServicePrincipalName,
pca-connector-ad:CreateServicePrincipalName
```

### List
```json
pca-connector-ad:ListServicePrincipalNames
```
