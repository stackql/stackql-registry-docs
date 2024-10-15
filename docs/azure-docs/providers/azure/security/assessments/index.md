---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
  - security
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

Creates, updates, deletes, gets or lists a <code>assessments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.assessments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assessments', value: 'view', },
        { label: 'assessments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="partners_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of an assessment. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessmentName, resourceId" /> | Get a security assessment on your scanned resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get security assessments on all your scanned resources inside a scope |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assessmentName, resourceId" /> | Create a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assessmentName, resourceId" /> | Delete a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result |

## `SELECT` examples

Get security assessments on all your scanned resources inside a scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assessments', value: 'view', },
        { label: 'assessments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_data,
assessmentName,
display_name,
links,
metadata,
partners_data,
resourceId,
resource_details,
scope,
status,
type
FROM azure.security.vw_assessments
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.assessments
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assessments</code> resource.

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
INSERT INTO azure.security.assessments (
assessmentName,
resourceId,
properties
)
SELECT 
'{{ assessmentName }}',
'{{ resourceId }}',
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
        - name: status
          value:
            - name: code
              value: string
            - name: cause
              value: string
            - name: description
              value: string
        - name: resourceDetails
          value:
            - name: source
              value: string
        - name: displayName
          value: string
        - name: additionalData
          value: object
        - name: links
          value:
            - name: azurePortalUri
              value: string
        - name: metadata
          value:
            - name: displayName
              value: string
            - name: policyDefinitionId
              value: string
            - name: description
              value: string
            - name: remediationDescription
              value: string
            - name: categories
              value:
                - string
            - name: severity
              value: string
            - name: userImpact
              value: string
            - name: implementationEffort
              value: string
            - name: threats
              value:
                - string
            - name: preview
              value: boolean
            - name: assessmentType
              value: string
            - name: partnerData
              value:
                - name: partnerName
                  value: string
                - name: productName
                  value: string
                - name: secret
                  value: string
        - name: partnersData
          value:
            - name: partnerName
              value: string
            - name: secret
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>assessments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.assessments
WHERE assessmentName = '{{ assessmentName }}'
AND resourceId = '{{ resourceId }}';
```
