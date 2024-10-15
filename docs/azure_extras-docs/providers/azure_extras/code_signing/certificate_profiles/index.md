---
title: certificate_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_profiles
  - code_signing
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>certificate_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.code_signing.certificate_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_profiles', value: 'view', },
        { label: 'certificate_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="city" /> | `text` | field from the `properties` object |
| <CopyableCode code="common_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="country" /> | `text` | field from the `properties` object |
| <CopyableCode code="enhanced_key_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_validation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="include_city" /> | `text` | field from the `properties` object |
| <CopyableCode code="include_country" /> | `text` | field from the `properties` object |
| <CopyableCode code="include_postal_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="include_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="include_street_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="organization" /> | `text` | field from the `properties` object |
| <CopyableCode code="organization_unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="postal_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="street_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the certificate profile. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId" /> | Get details of a certificate profile. |
| <CopyableCode code="list_by_code_signing_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List certificate profiles under a trusted signing account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId" /> | Create a certificate profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId" /> | Delete a certificate profile. |
| <CopyableCode code="revoke_certificate" /> | `EXEC` | <CopyableCode code="accountName, profileName, resourceGroupName, subscriptionId, data__effectiveAt, data__reason, data__serialNumber, data__thumbprint" /> | Revoke a certificate under a certificate profile. |

## `SELECT` examples

List certificate profiles under a trusted signing account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_profiles', value: 'view', },
        { label: 'certificate_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
certificates,
city,
common_name,
country,
enhanced_key_usage,
identity_validation_id,
include_city,
include_country,
include_postal_code,
include_state,
include_street_address,
organization,
organization_unit,
postal_code,
profileName,
profile_type,
provisioning_state,
resourceGroupName,
state,
status,
street_address,
subscriptionId
FROM azure_extras.code_signing.vw_certificate_profiles
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.code_signing.certificate_profiles
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_profiles</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure_extras.code_signing.certificate_profiles (
accountName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: profileType
          value: []
        - name: commonName
          value: string
        - name: organization
          value: string
        - name: organizationUnit
          value: string
        - name: streetAddress
          value: string
        - name: includeStreetAddress
          value: boolean
        - name: city
          value: string
        - name: includeCity
          value: boolean
        - name: state
          value: string
        - name: includeState
          value: boolean
        - name: country
          value: string
        - name: includeCountry
          value: boolean
        - name: postalCode
          value: string
        - name: includePostalCode
          value: boolean
        - name: enhancedKeyUsage
          value: string
        - name: identityValidationId
          value: string
        - name: provisioningState
          value: []
        - name: status
          value: []
        - name: certificates
          value:
            - - name: serialNumber
                value: string
              - name: subjectName
                value: string
              - name: thumbprint
                value: string
              - name: createdDate
                value: string
              - name: expiryDate
                value: string
              - name: status
                value: []
              - name: revocation
                value:
                  - name: requestedAt
                    value: string
                  - name: effectiveAt
                    value: string
                  - name: reason
                    value: string
                  - name: remarks
                    value: string
                  - name: status
                    value: []
                  - name: failureReason
                    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>certificate_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.code_signing.certificate_profiles
WHERE accountName = '{{ accountName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
