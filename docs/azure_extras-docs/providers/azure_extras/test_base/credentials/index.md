---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
  - test_base
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

Creates, updates, deletes, gets or lists a <code>credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.credentials" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credentials', value: 'view', },
        { label: 'credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentialName" /> | `text` | field from the `properties` object |
| <CopyableCode code="credential_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of test base credential |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a test base credential Resource |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the Credentials under a Test Base Account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Creates or replaces a Test Base Credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes an existing test base credential. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="credentialName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Updates an existing test base credential. |

## `SELECT` examples

Lists all the Credentials under a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credentials', value: 'view', },
        { label: 'credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
credentialName,
credential_type,
display_name,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_credentials
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.credentials
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>credentials</code> resource.

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
INSERT INTO azure_extras.test_base.credentials (
credentialName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties
)
SELECT 
'{{ credentialName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testBaseAccountName }}',
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
        - name: credentialType
          value: string
        - name: displayName
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>credentials</code> resource.

```sql
/*+ update */
UPDATE azure_extras.test_base.credentials
SET 
properties = '{{ properties }}'
WHERE 
credentialName = '{{ credentialName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```

## `DELETE` example

Deletes the specified <code>credentials</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.credentials
WHERE credentialName = '{{ credentialName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
