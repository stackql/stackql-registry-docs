---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - spring_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.certificates" /></td></tr>
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
| <CopyableCode code="activate_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="issued_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="issuer" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Certificate resource payload. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, resourceGroupName, serviceName, subscriptionId" /> | Get the certificate resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List all the certificates of one user. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, resourceGroupName, serviceName, subscriptionId" /> | Create or update certificate resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, resourceGroupName, serviceName, subscriptionId" /> | Delete the certificate resource. |

## `SELECT` examples

List all the certificates of one user.

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
activate_date,
certificateName,
dns_names,
expiration_date,
issued_date,
issuer,
provisioning_state,
resourceGroupName,
serviceName,
subject_name,
subscriptionId,
thumbprint,
type
FROM azure.spring_apps.vw_certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
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
INSERT INTO azure.spring_apps.certificates (
certificateName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ certificateName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: type
          value: string
        - name: thumbprint
          value: string
        - name: issuer
          value: string
        - name: issuedDate
          value: string
        - name: expirationDate
          value: string
        - name: activateDate
          value: string
        - name: subjectName
          value: string
        - name: dnsNames
          value:
            - string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.certificates
WHERE certificateName = '{{ certificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
