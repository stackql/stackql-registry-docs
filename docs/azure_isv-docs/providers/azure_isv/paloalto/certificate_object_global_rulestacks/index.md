---
title: certificate_object_global_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_object_global_rulestacks
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

Creates, updates, deletes, gets or lists a <code>certificate_object_global_rulestacks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_object_global_rulestacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.certificate_object_global_rulestacks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_object_global_rulestacks', value: 'view', },
        { label: 'certificate_object_global_rulestacks', value: 'resource', },
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
| <CopyableCode code="globalRulestackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName, name" /> | Get a CertificateObjectGlobalRulestackResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | List CertificateObjectGlobalRulestackResource resources by Tenant |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="globalRulestackName, name, data__properties" /> | Create a CertificateObjectGlobalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="globalRulestackName, name" /> | Delete a CertificateObjectGlobalRulestackResource |

## `SELECT` examples

List CertificateObjectGlobalRulestackResource resources by Tenant

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificate_object_global_rulestacks', value: 'view', },
        { label: 'certificate_object_global_rulestacks', value: 'resource', },
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
globalRulestackName,
provisioning_state,
system_data
FROM azure_isv.paloalto.vw_certificate_object_global_rulestacks
WHERE globalRulestackName = '{{ globalRulestackName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_isv.paloalto.certificate_object_global_rulestacks
WHERE globalRulestackName = '{{ globalRulestackName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_object_global_rulestacks</code> resource.

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
INSERT INTO azure_isv.paloalto.certificate_object_global_rulestacks (
globalRulestackName,
name,
data__properties,
properties
)
SELECT 
'{{ globalRulestackName }}',
'{{ name }}',
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

Deletes the specified <code>certificate_object_global_rulestacks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.paloalto.certificate_object_global_rulestacks
WHERE globalRulestackName = '{{ globalRulestackName }}'
AND name = '{{ name }}';
```
