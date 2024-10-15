---
title: content_key_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies
  - media_services
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

Creates, updates, deletes, gets or lists a <code>content_key_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>content_key_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.content_key_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_key_policies', value: 'view', },
        { label: 'content_key_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="contentKeyPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="options" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the Content Key Policy. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Get the details of a Content Key Policy in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Content Key Policies in the account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Create or update a Content Key Policy in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Deletes a Content Key Policy in the Media Services account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, contentKeyPolicyName, resourceGroupName, subscriptionId" /> | Updates an existing Content Key Policy in the Media Services account |

## `SELECT` examples

Lists the Content Key Policies in the account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_key_policies', value: 'view', },
        { label: 'content_key_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
contentKeyPolicyName,
created,
last_modified,
options,
policy_id,
resourceGroupName,
subscriptionId,
system_data
FROM azure.media_services.vw_content_key_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.content_key_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>content_key_policies</code> resource.

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
INSERT INTO azure.media_services.content_key_policies (
accountName,
contentKeyPolicyName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ contentKeyPolicyName }}',
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
        - name: policyId
          value: string
        - name: created
          value: string
        - name: lastModified
          value: string
        - name: description
          value: string
        - name: options
          value:
            - - name: policyOptionId
                value: string
              - name: name
                value: string
              - name: configuration
                value:
                  - name: '@odata.type'
                    value: string
              - name: restriction
                value:
                  - name: '@odata.type'
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

## `UPDATE` example

Updates a <code>content_key_policies</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.content_key_policies
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND contentKeyPolicyName = '{{ contentKeyPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>content_key_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.content_key_policies
WHERE accountName = '{{ accountName }}'
AND contentKeyPolicyName = '{{ contentKeyPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
