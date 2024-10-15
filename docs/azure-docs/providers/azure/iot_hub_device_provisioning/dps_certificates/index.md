---
title: dps_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - dps_certificates
  - iot_hub_device_provisioning
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

Creates, updates, deletes, gets or lists a <code>dps_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dps_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.dps_certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dps_certificates', value: 'view', },
        { label: 'dps_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The name of the certificate. |
| <CopyableCode code="certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The entity tag. |
| <CopyableCode code="expiry" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_verified" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioningServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="updated" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The name of the certificate. |
| <CopyableCode code="etag" /> | `string` | The entity tag. |
| <CopyableCode code="properties" /> | `object` | The description of an X509 CA Certificate. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Get the certificate from the provisioning service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="provisioningServiceName, resourceGroupName, subscriptionId" /> | Get all the certificates tied to the provisioning service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Add new certificate or update an existing certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Deletes the specified certificate associated with the Provisioning Service |
| <CopyableCode code="generate_verification_code" /> | `EXEC` | <CopyableCode code="If-Match, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Generate verification code for Proof of Possession. |
| <CopyableCode code="verify_certificate" /> | `EXEC` | <CopyableCode code="If-Match, certificateName, provisioningServiceName, resourceGroupName, subscriptionId" /> | Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate. |

## `SELECT` examples

Get all the certificates tied to the provisioning service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dps_certificates', value: 'view', },
        { label: 'dps_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
certificate,
certificateName,
created,
etag,
expiry,
is_verified,
provisioningServiceName,
resourceGroupName,
subject,
subscriptionId,
system_data,
thumbprint,
type,
updated
FROM azure.iot_hub_device_provisioning.vw_dps_certificates
WHERE provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.iot_hub_device_provisioning.dps_certificates
WHERE provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dps_certificates</code> resource.

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
INSERT INTO azure.iot_hub_device_provisioning.dps_certificates (
certificateName,
provisioningServiceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ certificateName }}',
'{{ provisioningServiceName }}',
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
        - name: subject
          value: string
        - name: expiry
          value: string
        - name: thumbprint
          value: string
        - name: isVerified
          value: boolean
        - name: certificate
          value: string
        - name: created
          value: string
        - name: updated
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dps_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_hub_device_provisioning.dps_certificates
WHERE If-Match = '{{ If-Match }}'
AND certificateName = '{{ certificateName }}'
AND provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
