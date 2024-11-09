---
title: certificate_object_local_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_object_local_rulestacks
  - paloalto
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

Creates, updates, deletes, gets or lists a <code>certificate_object_local_rulestacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_object_local_rulestacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.certificate_object_local_rulestacks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_object_local_rulestacks', value: 'view', },
        { label: 'certificate_object_local_rulestacks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="audit_comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate_self_signed" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate_signer_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="localRulestackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | certificate used for inbound and outbound decryption |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, name, resourceGroupName, subscriptionId" /> | Get a CertificateObjectLocalRulestackResource |
| <CopyableCode code="list_by_local_rulestacks" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | List CertificateObjectLocalRulestackResource resources by LocalRulestacks |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localRulestackName, name, resourceGroupName, subscriptionId, data__properties" /> | Create a CertificateObjectLocalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localRulestackName, name, resourceGroupName, subscriptionId" /> | Delete a CertificateObjectLocalRulestackResource |

## `SELECT` examples

List CertificateObjectLocalRulestackResource resources by LocalRulestacks

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_object_local_rulestacks', value: 'view', },
        { label: 'certificate_object_local_rulestacks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
description,
audit_comment,
certificate_self_signed,
certificate_signer_resource_id,
etag,
localRulestackName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data
FROM azure_isv.paloalto.vw_certificate_object_local_rulestacks
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_isv.paloalto.certificate_object_local_rulestacks
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_object_local_rulestacks</code> resource.

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
INSERT INTO azure_isv.paloalto.certificate_object_local_rulestacks (
localRulestackName,
name,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ localRulestackName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: certificateSignerResourceId
          value: string
        - name: certificateSelfSigned
          value: []
        - name: auditComment
          value: string
        - name: description
          value: string
        - name: etag
          value: string
        - name: provisioningState
          value: []
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

Deletes the specified <code>certificate_object_local_rulestacks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.paloalto.certificate_object_local_rulestacks
WHERE localRulestackName = '{{ localRulestackName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```