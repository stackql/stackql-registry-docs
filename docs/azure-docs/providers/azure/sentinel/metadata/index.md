---
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.metadata" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metadata', value: 'view', },
        { label: 'metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="categories" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_schema_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependencies" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="first_publish_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_publish_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadataName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="preview_images" /> | `text` | field from the `properties` object |
| <CopyableCode code="preview_images_dark" /> | `text` | field from the `properties` object |
| <CopyableCode code="providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_analysis_tactics" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_analysis_techniques" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Metadata property bag. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Get a Metadata. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List of all metadata |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Create a Metadata. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Delete a Metadata. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="metadataName, resourceGroupName, subscriptionId, workspaceName" /> | Update an existing Metadata. |

## `SELECT` examples

List of all metadata

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metadata', value: 'view', },
        { label: 'metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
author,
categories,
content_id,
content_schema_version,
custom_version,
dependencies,
etag,
first_publish_date,
icon,
kind,
last_publish_date,
metadataName,
parent_id,
preview_images,
preview_images_dark,
providers,
resourceGroupName,
source,
subscriptionId,
support,
threat_analysis_tactics,
threat_analysis_techniques,
version,
workspaceName
FROM azure.sentinel.vw_metadata
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.metadata
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metadata</code> resource.

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
INSERT INTO azure.sentinel.metadata (
metadataName,
resourceGroupName,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ metadataName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: contentId
          value: []
        - name: parentId
          value: []
        - name: version
          value: []
        - name: kind
          value: []
        - name: source
          value:
            - name: kind
              value: string
            - name: name
              value: string
            - name: sourceId
              value: string
        - name: author
          value:
            - name: name
              value: string
            - name: email
              value: string
            - name: link
              value: string
        - name: support
          value:
            - name: tier
              value: string
            - name: name
              value: string
            - name: email
              value: string
            - name: link
              value: string
        - name: dependencies
          value:
            - name: name
              value: string
            - name: operator
              value: string
            - name: criteria
              value:
                - - name: name
                    value: string
                  - name: operator
                    value: string
                  - name: criteria
                    value:
                      - - name: name
                          value: string
                        - name: operator
                          value: string
                        - name: criteria
                          value:
                            - - name: name
                                value: string
                              - name: operator
                                value: string
                              - name: criteria
                                value:
                                  - - name: name
                                      value: string
                                    - name: operator
                                      value: string
                                    - name: criteria
                                      value:
                                        - - name: name
                                            value: string
                                          - name: operator
                                            value: string
                                          - name: criteria
                                            value:
                                              - - name: name
                                                  value: string
                                                - name: operator
                                                  value: string
                                                - name: criteria
                                                  value:
                                                    - - name: name
                                                        value: string
                                                      - name: operator
                                                        value: string
                                                      - name: criteria
                                                        value:
                                                          - - name: name
                                                              value: string
                                                            - name: operator
                                                              value: string
                                                            - name: criteria
                                                              value:
                                                                - []
        - name: categories
          value:
            - name: domains
              value:
                - string
            - name: verticals
              value:
                - string
        - name: providers
          value: []
        - name: firstPublishDate
          value: []
        - name: lastPublishDate
          value: []
        - name: customVersion
          value: []
        - name: contentSchemaVersion
          value: []
        - name: icon
          value: []
        - name: threatAnalysisTactics
          value: []
        - name: threatAnalysisTechniques
          value: []
        - name: previewImages
          value: []
        - name: previewImagesDark
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>metadata</code> resource.

```sql
/*+ update */
UPDATE azure.sentinel.metadata
SET 
properties = '{{ properties }}'
WHERE 
metadataName = '{{ metadataName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>metadata</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.metadata
WHERE metadataName = '{{ metadataName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
