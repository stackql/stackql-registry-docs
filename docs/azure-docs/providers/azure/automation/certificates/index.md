---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - automation
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.certificates" /></td></tr>
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
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_exportable" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the certificate. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId" /> | Retrieve the certificate identified by certificate name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of certificates. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId, data__name, data__properties" /> | Create a certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId" /> | Delete the certificate. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, certificateName, resourceGroupName, subscriptionId" /> | Update a certificate. |

## `SELECT` examples

Retrieve a list of certificates.

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
description,
automationAccountName,
certificateName,
creation_time,
expiry_time,
is_exportable,
last_modified_time,
resourceGroupName,
subscriptionId,
thumbprint
FROM azure.automation.vw_certificates
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.certificates
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
INSERT INTO azure.automation.certificates (
automationAccountName,
certificateName,
resourceGroupName,
subscriptionId,
data__name,
data__properties,
name,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ certificateName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__name }}',
'{{ data__properties }}',
'{{ name }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: properties
      value:
        - name: base64Value
          value: string
        - name: description
          value: string
        - name: thumbprint
          value: string
        - name: isExportable
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificates</code> resource.

```sql
/*+ update */
UPDATE azure.automation.certificates
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND certificateName = '{{ certificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.certificates
WHERE automationAccountName = '{{ automationAccountName }}'
AND certificateName = '{{ certificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
