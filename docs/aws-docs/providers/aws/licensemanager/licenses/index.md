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

Creates, updates, deletes or gets a <code>license</code> resource or lists <code>licenses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LicenseManager::License</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.licenses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="product_sku" /></td><td><code>string</code></td><td>ProductSKU of the license.</td></tr>
<tr><td><CopyableCode code="issuer" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="license_name" /></td><td><code>string</code></td><td>Name for the created license.</td></tr>
<tr><td><CopyableCode code="product_name" /></td><td><code>string</code></td><td>Product name for the created license.</td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td>Home region for the created license.</td></tr>
<tr><td><CopyableCode code="validity" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="entitlements" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="beneficiary" /></td><td><code>string</code></td><td>Beneficiary of the license.</td></tr>
<tr><td><CopyableCode code="consumption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="license_metadata" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="license_arn" /></td><td><code>string</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the license.</td></tr>
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
    <td><CopyableCode code="LicenseName, ProductName, Issuer, HomeRegion, Validity, ConsumptionConfiguration, Entitlements, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>licenses</code> in a region.
```sql
SELECT
region,
product_sku,
issuer,
license_name,
product_name,
home_region,
validity,
entitlements,
beneficiary,
consumption_configuration,
license_metadata,
license_arn,
status,
version
FROM aws.licensemanager.licenses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>license</code>.
```sql
SELECT
region,
product_sku,
issuer,
license_name,
product_name,
home_region,
validity,
entitlements,
beneficiary,
consumption_configuration,
license_metadata,
license_arn,
status,
version
FROM aws.licensemanager.licenses
WHERE region = 'us-east-1' AND data__Identifier = '<LicenseArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>license</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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
'{{ Issuer }}',
 '{{ LicenseName }}',
 '{{ ProductName }}',
 '{{ HomeRegion }}',
 '{{ Validity }}',
 '{{ Entitlements }}',
 '{{ ConsumptionConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ ProductSKU }}',
 '{{ Issuer }}',
 '{{ LicenseName }}',
 '{{ ProductName }}',
 '{{ HomeRegion }}',
 '{{ Validity }}',
 '{{ Entitlements }}',
 '{{ Beneficiary }}',
 '{{ ConsumptionConfiguration }}',
 '{{ LicenseMetadata }}',
 '{{ Status }}',
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
  - name: license
    props:
      - name: ProductSKU
        value: '{{ ProductSKU }}'
      - name: Issuer
        value:
          Name: '{{ Name }}'
          SignKey: '{{ SignKey }}'
      - name: LicenseName
        value: '{{ LicenseName }}'
      - name: ProductName
        value: '{{ ProductName }}'
      - name: HomeRegion
        value: '{{ HomeRegion }}'
      - name: Validity
        value:
          Begin: '{{ Begin }}'
          End: '{{ End }}'
      - name: Entitlements
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'
            MaxCount: '{{ MaxCount }}'
            Overage: '{{ Overage }}'
            Unit: '{{ Unit }}'
            AllowCheckIn: '{{ AllowCheckIn }}'
      - name: Beneficiary
        value: '{{ Beneficiary }}'
      - name: ConsumptionConfiguration
        value:
          RenewType: '{{ RenewType }}'
          ProvisionalConfiguration:
            MaxTimeToLiveInMinutes: '{{ MaxTimeToLiveInMinutes }}'
          BorrowConfiguration:
            MaxTimeToLiveInMinutes: '{{ MaxTimeToLiveInMinutes }}'
            AllowEarlyCheckIn: '{{ AllowEarlyCheckIn }}'
      - name: LicenseMetadata
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'
      - name: Status
        value: '{{ Status }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
license-manager:GetLicense
```

### Update
```json
license-manager:CreateLicenseVersion
```

### Delete
```json
license-manager:DeleteLicense
```

### List
```json
license-manager:ListLicenses
```

