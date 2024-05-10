---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
  - licensemanager
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


Used to retrieve a list of <code>licenses</code> in a region or to create or delete a <code>licenses</code> resource, use <code>license</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LicenseManager::License</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.licenses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="license_arn" /></td><td><code>undefined</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
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
license_arn
FROM aws.licensemanager.licenses
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Issuer": {
  "Name": "{{ Name }}",
  "SignKey": "{{ SignKey }}"
 },
 "LicenseName": "{{ LicenseName }}",
 "ProductName": "{{ ProductName }}",
 "HomeRegion": "{{ HomeRegion }}",
 "Validity": {
  "Begin": "{{ Begin }}",
  "End": "{{ End }}"
 },
 "Entitlements": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}",
   "MaxCount": "{{ MaxCount }}",
   "Overage": "{{ Overage }}",
   "Unit": "{{ Unit }}",
   "AllowCheckIn": "{{ AllowCheckIn }}"
  }
 ],
 "ConsumptionConfiguration": {
  "RenewType": "{{ RenewType }}",
  "ProvisionalConfiguration": {
   "MaxTimeToLiveInMinutes": "{{ MaxTimeToLiveInMinutes }}"
  },
  "BorrowConfiguration": {
   "MaxTimeToLiveInMinutes": "{{ MaxTimeToLiveInMinutes }}",
   "AllowEarlyCheckIn": "{{ AllowEarlyCheckIn }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.licensemanager.licenses (
 Issuer,
 LicenseName,
 ProductName,
 HomeRegion,
 Validity,
 Entitlements,
 ConsumptionConfiguration,
 region
)
SELECT 
{{ Issuer }},
 {{ LicenseName }},
 {{ ProductName }},
 {{ HomeRegion }},
 {{ Validity }},
 {{ Entitlements }},
 {{ ConsumptionConfiguration }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ProductSKU": "{{ ProductSKU }}",
 "Issuer": {
  "Name": "{{ Name }}",
  "SignKey": "{{ SignKey }}"
 },
 "LicenseName": "{{ LicenseName }}",
 "ProductName": "{{ ProductName }}",
 "HomeRegion": "{{ HomeRegion }}",
 "Validity": {
  "Begin": "{{ Begin }}",
  "End": "{{ End }}"
 },
 "Entitlements": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}",
   "MaxCount": "{{ MaxCount }}",
   "Overage": "{{ Overage }}",
   "Unit": "{{ Unit }}",
   "AllowCheckIn": "{{ AllowCheckIn }}"
  }
 ],
 "Beneficiary": "{{ Beneficiary }}",
 "ConsumptionConfiguration": {
  "RenewType": "{{ RenewType }}",
  "ProvisionalConfiguration": {
   "MaxTimeToLiveInMinutes": "{{ MaxTimeToLiveInMinutes }}"
  },
  "BorrowConfiguration": {
   "MaxTimeToLiveInMinutes": "{{ MaxTimeToLiveInMinutes }}",
   "AllowEarlyCheckIn": "{{ AllowEarlyCheckIn }}"
  }
 },
 "LicenseMetadata": [
  {
   "Name": "{{ Name }}",
   "Value": "{{ Value }}"
  }
 ],
 "Status": "{{ Status }}"
}
>>>
--all properties
INSERT INTO aws.licensemanager.licenses (
 ProductSKU,
 Issuer,
 LicenseName,
 ProductName,
 HomeRegion,
 Validity,
 Entitlements,
 Beneficiary,
 ConsumptionConfiguration,
 LicenseMetadata,
 Status,
 region
)
SELECT 
 {{ ProductSKU }},
 {{ Issuer }},
 {{ LicenseName }},
 {{ ProductName }},
 {{ HomeRegion }},
 {{ Validity }},
 {{ Entitlements }},
 {{ Beneficiary }},
 {{ ConsumptionConfiguration }},
 {{ LicenseMetadata }},
 {{ Status }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.licensemanager.licenses
WHERE data__Identifier = '<LicenseArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>licenses</code> resource, the following permissions are required:

### Create
```json
license-manager:CreateLicense
```

### Delete
```json
license-manager:DeleteLicense
```

### List
```json
license-manager:ListLicenses
```

