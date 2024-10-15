---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - iot_hub
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

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificates', value: 'view', },
        { label: 'certificates', value: 'resource', },
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
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, resourceGroupName, resourceName, subscriptionId" /> | Returns the certificate. |
| <CopyableCode code="list_by_iot_hub" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns the list of certificates. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, resourceGroupName, resourceName, subscriptionId" /> | Adds new or replaces existing certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Deletes an existing X509 certificate or does nothing if it does not exist. |
| <CopyableCode code="generate_verification_code" /> | `EXEC` | <CopyableCode code="If-Match, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="If-Match, certificateName, resourceGroupName, resourceName, subscriptionId" /> | Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate. |

## `SELECT` examples

Returns the list of certificates.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificates', value: 'view', },
        { label: 'certificates', value: 'resource', },
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
resourceGroupName,
resourceName,
subject,
subscriptionId,
thumbprint,
type,
updated
FROM azure.iot_hub.vw_certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
type
FROM azure.iot_hub.certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificates</code> resource.

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
INSERT INTO azure.iot_hub.certificates (
certificateName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ certificateName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: created
          value: string
        - name: updated
          value: string
        - name: certificate
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_hub.certificates
WHERE If-Match = '{{ If-Match }}'
AND certificateName = '{{ certificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
